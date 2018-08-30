import csv
import json

csvfile = open('player_10k.csv', 'r')
jsonfile = open('player_10k', 'w')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')