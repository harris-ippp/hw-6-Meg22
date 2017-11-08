#!/usr/bin/env python

import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#open dataframe
dataframe = []
#get content
file = open('ELECTION_ID', 'r')

for line in file.readlines():
    source = line.split()
    year = source[0]+".csv"
#align headers
    header = pd.read_csv(year, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv(year, index_col = 0, thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = source[0]
    dataframe.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
#create Republican share
    all = pd.concat(dataframe)
    all["Republican Share"] = all["Republican"]/all["Total Votes Cast"]
    accomack = all.loc['Accomack County'].astype(float)
    albemarle = all.loc['Albemarle County'].astype(float)
    alexandria = all.loc['Alexandria City'].astype(float)
    alleghany = all.loc['Alleghany County'].astype(float)
#create graphs
    graph1 = accomack.plot(kind = "line", x = "Year" ,y = "Republican Share")
    graph1.get_figure().savefig('accomack_county.pdf')
    graph2 = albemarle.plot(kind = "line", x = "Year" ,y = "Republican Share")
    graph2.get_figure().savefig('albemarle_county.pdf')
    graph3 = alexandria.plot(kind = "line", x = "Year" ,y = "Republican Share")
    graph3.get_figure().savefig('alexandria_city.pdf')
    graph4 = alleghany.plot(kind = "line", x = "Year" ,y = "Republican Share")
    graph4.get_figure().savefig('alleghany_county.pdf')
