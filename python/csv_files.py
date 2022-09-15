import csv

#  write to csv using DictWriter
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

# read csv using DictReader
# parses 1st row as header by default
with open("mycsv.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        print(row["Date"], row["Description"], row["Amount"])


# read csv using csv.reader
with open('eggs.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader) # skips first row
    for row in reader:
        print((row))

