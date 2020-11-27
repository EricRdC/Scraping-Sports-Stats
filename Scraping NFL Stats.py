import urllib.request
from bs4 import BeautifulSoup #Initializing libraries
import requests
import csv
import pandas as pd
pd.set_option('display.max_rows', None)
url = "https://www.footballdb.com/stats/teamstat.html?group=O&cat=T" #URL with Team Stats
page = urllib.request.urlopen(url) #Requesting info
soup = BeautifulSoup(page, 'html.parser')
table=soup.find_all('table',class_='TableBase-table') #Finding specific table
thead = soup.table.find('thead')
head = thead.find_all('tr')
tbody = soup.table.find('tbody')
body = tbody.find_all('tr')
head_column = []
rowvalues = []
for tr in head:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    head_column.append(row)
for tr in body:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    rowvalues.append(row)

FetchStats = pd.DataFrame(rowvalues,columns=head_column[0]) #Preparing DataFrame with stats
FetchStatsOT = FetchStats.sort_values(by=['Team'])
FetchStatsOT.reset_index(drop = True, inplace = True)
print (FetchStatsOT)
FetchStatsColumns = FetchStats.copy()
FetchStatsColumns.iloc[:, 1:] = FetchStatsColumns.iloc[:, 1:].astype(float)
#print(FetchStatsColumns.rank(pct=True).round(decimals=2))
FetchStatsColumns = FetchStatsColumns.drop(FetchStatsColumns.columns[0], axis = 1)
FetchStatsColumns= FetchStatsColumns.astype(float)
toRound = FetchStatsColumns.describe()
RoundingDF = toRound.round(decimals = 2)
print (RoundingDF)


import urllib.request
from bs4 import BeautifulSoup #Initializing libraries
import requests
import csv
import pandas as pd
url = "https://www.footballdb.com/stats/teamstat.html?group=D&cat=T" #URL with Team Stats
page = urllib.request.urlopen(url) #Requesting info
soup = BeautifulSoup(page, 'html.parser')
table=soup.find_all('table',class_='TableBase-table') #Finding specific table
thead = soup.table.find('thead')
head = thead.find_all('tr')
tbody = soup.table.find('tbody')
body = tbody.find_all('tr')
head_column = []
rowvalues = []
for tr in head:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    head_column.append(row)
for tr in body:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    rowvalues.append(row)

FetchStats = pd.DataFrame(rowvalues,columns=head_column[0]) #Preparing DataFrame with stats
FetchStatsDT = FetchStats.sort_values(by=['Team'])
FetchStatsDT.reset_index(drop = True, inplace = True)
print (FetchStatsDT)
FetchStatsColumns = FetchStats.copy()
FetchStatsColumns.iloc[:, 1:] = FetchStatsColumns.iloc[:, 1:].astype(float)
#print(FetchStatsColumns.rank(pct=True).round(decimals=2))
FetchStatsColumns = FetchStatsColumns.drop(FetchStatsColumns.columns[0], axis = 1)
FetchStatsColumns= FetchStatsColumns.astype(float)
toRound = FetchStatsColumns.describe()
RoundingDF = toRound.round(decimals = 2)
print (RoundingDF)
teste1 = input ("Insira o index do primeiro time:")
teste1 = int(teste1)
teste2 = input ("Insira o index do segundo time:")
teste2 = int(teste2)
print (FetchStatsOT.iloc[teste1])
print (FetchStatsOT.iloc[teste2])
print (FetchStatsDT.iloc[teste1])
print (FetchStatsDT.iloc[teste2])