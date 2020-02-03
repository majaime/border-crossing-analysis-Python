# Importing the required modules
import csv
from collections import Counter
from itertools import groupby
from operator import itemgetter

# Reading data file (.csv) and establishing a dictionary for data storage
with open("./input/Border_Crossing_Entry_Data.csv", newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    myDictionary = {}

    # Reading the data to determine the desirable headers ["Port", "Border", "Date", "Measure", "Value"]
    for i, row in enumerate(csv_reader):
        myDictionary[i + 1] = row["Port Name"], row["Border"], row["Date"], row["Measure"], row["Value"]


# Building a class and methods to include the data for the dictionary
class border_crossing(dict):

    def __init__(self):
        self = dict()

    # Involving the desirable headers and keeping "port" as a key to the dictionary
    def add_port(self, port, border, date, measure, value):
        self[port] = border, date, measure, value

    # Determining the number of rows in the dictionary
    def len(self):
        return self.__len__()

    # Sorting the items in the dictionary
    def sort_items(self, sort_key=0, is_reverse=False, is_integer=False):
        '''
        sort_key argument is the index of the column to sort by.
        is_reverse=False if Ascending order, and True if Descending order.
        is_integer argument will ensure numeric data are treated as numeric.
        '''
        if is_integer:
            return sorted(self, key=lambda port: int(self[port][sort_key]), reverse=is_reverse)
        else:
            return sorted(self, key=lambda port: self[port][sort_key], reverse=is_reverse)

    # Deleting a row from the dictionary
    def del_row(self, row_key):
        self.pop(row_key, None)
        return self

    # Writing the method of the dictionary
    def __repr__(self):
        return repr(dict(self))


# Presenting the class as ports
ports = border_crossing()

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


def key_function(port):
    # Sorting by Date
    key1 = ports[port][1]
    # Sorting by Measure
    key2 = ports[port][2]
    # Sorting by Value
    return (key1, key2)


# Sorting the dictionary by the keys_function
ports_sorted = sorted(ports, key=lambda port: key_function(port), reverse=True)

# Appending the dictionary by Date and Measure
for m, g in groupby(ports_sorted, key=lambda port: key_function(port)):
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
            value_ = int(port[j])
            border_ = port[l]
            grouped_item.append((value_, border_))

        else:
            port = [ports[x[0]], ports[x[1]]]
            value_ = int(port[0][j]) + int(port[1][j])
            border_ = port[0][l]
            grouped_item.append((value_, border_))
    return grouped_item


grouped_items = group_items(3, 0)
group_length = len(grouped_items)

# Consolidating all groupings
grouped_dictrionary = {}
for i, n, y in zip(range(1, group_length + 1), keys, grouped_items):
    grouped_dictrionary[i] = list((n, y))

all_groups = [list(i[0]) + list(i[1]) for i in grouped_dictrionary.values()]

# Sort by Date and Value upon grouping
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

# Applying counters to record instances of the "Measure" columns
multiples = Counter(measures.values())
multiple_measure = {k: v for k, v in measures.items() if multiples[v] > 1}

date_min = min(dates.values())
date_max = max(dates.values())


# A rounding function
def rounding_fcn(num):
    if num < 0:
        add_num = num - 0.5
        return int(add_num)
    else:
        add_num = num + 0.5
        return int(add_num)


# use conditionals to populate the average column
count = 0
counter = 0
for i, n in multiple_measure.items():
    count += + values[i]
    counter += 1
    if dates[i] == date_min:
        sorted_group[i][4] = 0
    else:
        sorted_group[i][4] = rounding_fcn((count - values[i]) / (counter - 1))

# Final sorting of dictionary output
final_sort = sorted(sorted_group, key=itemgetter(0, 2, 1, 3), reverse=True)

# Converting to dictionary and adding columns names
final_output = {}
column_names = ["Date", "Measure", "Value", "Border", "Average"]
for i, r in zip(final_sort, range(len(final_sort))):
    column = {j: i[k] for k, j in enumerate(column_names)}
    final_output[r] = column

final = final_output.values()

# Preparing the output
with open("./output/report.csv", "w", newline='') as csvfile:
    field_names = ["Border", "Date", "Measure", "Value", "Average"]
    csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
    csv_writer.writeheader()

    for row in final:
        csv_writer.writerow(row)
