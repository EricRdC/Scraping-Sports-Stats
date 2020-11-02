import urllib.request
from bs4 import BeautifulSoup #Initializing libraries
import requests
import csv
import pandas as pd
url = "https://basketball.realgm.com/international/league/2/Eurocup/team-stats/2021/Averages" #URL with Team Stats
page = urllib.request.urlopen(url) #Requesting info
soup = BeautifulSoup(page, 'html.parser')
table=soup.find_all('table',class_='tablesaw tablesaw-swipe') #Finding specific table
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
TeamStats = FetchStats.drop(FetchStats.columns[0], axis = 1) #Removing Index
TeamStats[['GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB', 'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']] = TeamStats[['GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB', 'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']].astype(float) #Converting stats from string to float
print ("Tabela geral: \n")
print (FetchStats) #Printing table
Percentile = TeamStats.rank(pct=True)
Percentile_Round = Percentile.round(decimals = 2)
print ("Percentis \n")
print (Percentile_Round)
toRound = TeamStats.describe() #Rounding stats
roundingDF = toRound.round(decimals=2)
print ("Análise descritiva \n")
print (roundingDF)
print ("\n")

url = "https://basketball.realgm.com/international/league/2/Eurocup/team-stats/2021/Averages/Opponent_Totals" #URL with Team Stats
page = urllib.request.urlopen(url) #Requesting info
soup = BeautifulSoup(page, 'html.parser')
table=soup.find_all('table',class_='tablesaw tablesaw-swipe') #Finding specific table
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
TeamStats = FetchStats.drop(FetchStats.columns[0], axis = 1) #Removing Index
TeamStats[['GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB', 'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']] = TeamStats[['GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB', 'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']].astype(float) #Converting stats from string to float
print ("Tabela geral OPP: \n")
print (FetchStats) #Printing table
Percentile = TeamStats.rank(pct=True)
Percentile_Round = Percentile.round(decimals = 2)
print ("Percentis OPP \n")
print (Percentile_Round)
toRound = TeamStats.describe() #Rounding stats
roundingDF = toRound.round(decimals=2)
print ("Análise descritiva OPP \n")
print (roundingDF)
print ("\n")

url = "https://basketball.realgm.com/international/league/2/Eurocup/team-stats/2021/Advanced_Stats/Team_Totals" #URL with Team Stats
page = urllib.request.urlopen(url) #Requesting info
soup = BeautifulSoup(page, 'html.parser')
table=soup.find_all('table',class_='tablesaw tablesaw-swipe') #Finding specific table
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
TeamStats = FetchStats.drop(FetchStats.columns[0], axis = 1) #Removing Index
TeamStats[['TS%', 'eFG%', 'Total S%', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'TOV%', 'STL%', 'BLK%', 'PPS', 'FIC40', 'ORtg', 'DRtg', 'eDiff', 'Poss', 'Pace']] = TeamStats[['TS%', 'eFG%', 'Total S%', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'TOV%', 'STL%', 'BLK%', 'PPS', 'FIC40', 'ORtg', 'DRtg', 'eDiff', 'Poss', 'Pace']].astype(float) #Converting stats from string to float
print ("Tabela geral Advanced Stats: \n")
print (FetchStats) #Printing table
Percentile = TeamStats.rank(pct=True)
Percentile_Round = Percentile.round(decimals = 2)
print ("Percentis Advanced Stats \n")
print (Percentile_Round)
toRound = TeamStats.describe() #Rounding stats
roundingDF = toRound.round(decimals=2)
print ("Análise descritiva Advanced Stats \n")
print (roundingDF)
print ("\n")