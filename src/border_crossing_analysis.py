# This code decrypts a .csv file initially for reading the data.
# Then dictionary is defined using the data previously read.
# Finally, data meeting the criteria are extracted, sorted, and outputted.

# Importing the required modules
import csv
from operator import itemgetter
from collections import Counter
from itertools import groupby

# Reading data file (.csv) and establishing a dictionary for data storage
with open("../input/Border_Crossing_Entry_Data.csv", newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    myDictionary = {}

    # Reading the data to determine the desirable headers ["Port", "Border", "Date", "Measure", "Value"]
    for i, row in enumerate(csv_reader):
        myDictionary[i + 1] = row["Port Name"], row["Border"], row["Date"], row["Measure"], row["Value"]


# Building a class and methods to include the data for the dictionary
class BorderCrossing(dict):

    # Involving the desirable headers and keeping "port" as a key to the dictionary
    def add_port(self, port, border, date, measure, value):
        self[port] = border, date, measure, value


# Presenting the class as ports
ports = BorderCrossing()

# Iterating through the dictionary to add each row to the class
for m, n in myDictionary.items():
    port = n[0]
    border = n[1]
    date = n[2]
    measure = n[3]
    value = n[4]
    ports.add_port(port, border, date, measure, value)

# Creating a list and a function to store and sort the dictionary by Date and Measure
groups = []
keys = []


# Establishing customized keys (Date, Value, and Measure) according to the problem statement
def keys_function(port):
    key1 = ports[port][1]
    key2 = ports[port][2]
    return key1, key2


# Sorting the dictionary by the keys_function
ports_sorted = sorted(ports, key=lambda port: keys_function(port), reverse=True)

# Appending the dictionary by Date and Measure
for m, g in groupby(ports_sorted, key=lambda port: keys_function(port)):
    groups.append(list(g))
    keys.append(m)

# Grouping Border and Measure
grouping = [x for x in groups]


# Grouping Values and Border
def group_items(j, l):
    grouped_item = []
    for x in grouping:
        if len(x) == 1:
            port = ports[x[0]]
            value2 = int(port[j])
            border2 = port[l]
            grouped_item.append((value2, border2))
        else:
            port = [ports[x[0]], ports[x[1]]]
            value2 = int(port[0][j]) + int(port[1][j])
            border2 = port[0][l]
            grouped_item.append((value2, border2))
    return grouped_item


grouped_items = group_items(3, 0)
group_length = len(grouped_items)

# Consolidating all groupings
grouped_dictionary = {}
for i, n, y in zip(range(1, group_length + 1), keys, grouped_items):
    grouped_dictionary[i] = list((n, y))

all_groups = [list(i[0]) + list(i[1]) for i in grouped_dictionary.values()]

# Sorting by Date and Value upon grouping
sorted_group = sorted(all_groups, key=itemgetter(0, 2), reverse=False)

# Casting another column for the "average"
for i in sorted_group:
    i.append(0)

# Creating new dictionaries from the columns in the sorted dictionary
dates = Counter()
measures = Counter()
values = Counter()
borders = Counter()
average = Counter()

for i, n in enumerate(sorted_group):
    dates[i] = n[0]
    measures[i] = n[1]
    values[i] = n[2]
    borders[i] = n[3]
    average[i] = n[4]

# Applying counter to record instances of the "Measure" columns
multiples = Counter(measures.values())
multiple_measure = {k: v for k, v in measures.items() if multiples[v] > 1}

date_min = min(dates.values())
date_max = max(dates.values())

# Generating the "average" column and rounding the sorted values
count = 0
counter = 0
for i, n in multiple_measure.items():
    count += + values[i]
    counter += 1
    if dates[i] == date_min:
        sorted_group[i][4] = 0
    else:
        sorted_group[i][4] = round((count - values[i]) / (counter - 1))

# Sorting the dictionary output according to the problem statement
output_sorted = sorted(sorted_group, key=itemgetter(0, 2, 1, 3), reverse=True)

# Converting to dictionary and adding names to the columns
output_final = {}
columns_names = ["Date", "Measure", "Value", "Border", "Average"]
for i, r in zip(output_sorted, range(len(output_sorted))):
    column = {j: i[k] for k, j in enumerate(columns_names)}
    output_final[r] = column

output = output_final.values()

# Preparing the output
with open("../output/report.csv", "w", newline='') as csvfile:
    headers = ["Border", "Date", "Measure", "Value", "Average"]
    csv_writer = csv.DictWriter(csvfile, fieldnames=headers)
    csv_writer.writeheader()

    for o in output:
        csv_writer.writerow(o)
