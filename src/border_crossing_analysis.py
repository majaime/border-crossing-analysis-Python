# Reading (scanning) the data from an input folder
import csv
import operator

with open('../input/Border_Crossing_Entry_Data.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    print("Border," + "Date," + "Measure," + "Value," + "Average")

    count_1 = 0
    count_2 = 0
    count_3 = 0

    for row in csv_reader:

        # Finding the first criteria
        if row[3] == "US-Mexico Border":
            if row[4] == "03/01/2019 12:00:00 AM":
                if row[5] == "Pedestrians":
                    new = int(row[6])
                    count_1 += new

        # Finding the second criteria
        if row[3] == "US-Mexico Border":
            if row[4] == "02/01/2019 12:00:00 AM":
                if row[5] == "Pedestrians":
                    count_2 = count_2 + int(row[6])

        # Finding the third criteria
        if row[3] == "US-Mexico Border":
            if row[4] == "01/01/2019 12:00:00 AM":
                if row[5] == "Pedestrians":
                    count_3 = count_3 + int(row[6])

first = (row[3] + "," + "03/01/2019 12:00:00 AM" + "," + row[5] + "," + str(count_1))
second = (row[3] + "," + "02/01/2019 12:00:00 AM" + "," + row[5] + "," + str(count_2))
third = (row[3] + "," + "01/01/2019 12:00:00 AM" + "," + row[5] + "," + str(count_3))
outputs = [first,second,third]
list1 = sorted(outputs,reverse=True)
print(list1)

