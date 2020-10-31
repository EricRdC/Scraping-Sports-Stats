import urllib.request
from bs4 import BeautifulSoup #Initializing libraries
import requests
import csv
import pandas as pd
url = "https://fbref.com/en/comps/11/Serie-A-Stats" #URL with Team Stats
page = urllib.request.urlopen(url) #Requesting info
soup = BeautifulSoup(page, 'html.parser')
table=soup.find_all('table',class_='min_width sortable stats_table now_sortable sticky_table re2 le2', id = 'results107281_overall') #Finding specific table
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
Colunas = ['Attendance','Top Team Scorer','Goalkeeper','Notes']
FetchStatsColumns = FetchStats
FetchStatsColumns = FetchStats.drop(FetchStats.columns[[15,16, 17,18]], axis = 1) #Removing Index
FetchStatsColumns[['MP', 'W', 'D', 'L', 'GF', 'GA', 'GDiff', 'Pts', 'xG', 'xGA', 'xGDiff', 'xGDiff/90']] = FetchStatsColumns[['MP', 'W', 'D', 'L', 'GF', 'GA', 'GDiff', 'Pts', 'xG', 'xGA', 'xGDiff', 'xGDiff/90']].astype(float) #Converting stats from string to float
AveragePG = FetchStatsColumns.copy()
AveragePG[['W', 'D', 'L', 'GF', 'GA', 'GDiff', 'Pts', 'xG', 'xGA']] = AveragePG[['W', 'D', 'L', 'GF', 'GA', 'GDiff', 'Pts', 'xG', 'xGA']].div(AveragePG['MP'].values, axis = 0)
AveragePG = AveragePG.drop(AveragePG.columns[12], axis = 1)
AveragePGRound = AveragePG.round(decimals=2)
print ("Tabela geral \n")
print (FetchStatsColumns)
print ("Tabela média por jogos jogados \n")
print (AveragePGRound)
toRound = AveragePGRound.describe() #Rounding stats
roundingDF = toRound.round(decimals=2)
print ("Análise descritiva \n")
print (roundingDF)
Percentile = AveragePGRound.rank(pct=True)
Percentile_Round = Percentile.round(decimals = 2)
print ("Percentis Advanced Stats \n")
print (Percentile_Round)
