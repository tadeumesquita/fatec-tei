import os
import csv
os.system("cls")

f = open("dias-de-marco.csv","r",encoding="iso-8859-1")
reader = csv.reader(f)
for row in reader:
    print(row)

f.close