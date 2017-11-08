#!/usr/bin/env python
import requests


#open file
file = open('ELECTION_ID', 'r')

#for every line get link
for line in file.readlines():
    source = line.split()
    year = source[0]
    link = ["http://historical.elections.virginia.gov/elections/download/" + str(source[1]) + "/precincts_include:0/"]
#output in csv file
    for url in link:
       resp=requests.get(url)
       file_name = year + ".csv"
       with open(file_name, "w") as out:
            out.write(resp.text)
