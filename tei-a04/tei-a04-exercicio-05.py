import os
import csv
import json

os.system("cls")

line = []

fcsv = open("output.csv","r",encoding="iso-8859-1")
reader = csv.reader(fcsv)
for row in reader:
    line.append(row)



print(line)

fcsv.close