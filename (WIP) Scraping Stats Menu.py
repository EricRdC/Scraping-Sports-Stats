import urllib.request
from bs4 import BeautifulSoup #Initializing libraries
import requests
import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestClassifier
def print_menu():
    print("1. EuroLeague.") 
    print("2. EuroCup.") 
    print("3. NBB.") 
    print("4. NBA.") 
    print("5. EPL.") 
    print("6. Italy Serie A.") 
    print("7. Bundesliga.") 
    print("8. NHL.")
    print ("9. Player Analyzer (NBA).")
    print ("10. Player Analyzer (NHL).")
    print ("11. (WIP) ML Testing Grounds.")
    print("0. Exit.") 
loop = True
while loop:
    print_menu()
    selection=input("Please Select:") 
    if selection =='1': 
        import urllib.request
        from bs4 import BeautifulSoup #Initializing libraries
        import requests
        import csv
        import pandas as pd
        url = "https://basketball.realgm.com/international/league/1/Euroleague/team-stats" #URL with Team Stats
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

        url = "https://basketball.realgm.com/international/league/1/Euroleague/team-stats/2021/Averages/Opponent_Totals" #URL with Team Stats
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

        url = "https://basketball.realgm.com/international/league/1/Euroleague/team-stats/2021/Advanced_Stats/Team_Totals" #URL with Team Stats
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
    elif selection == '2': 
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
    elif selection == '3':
        url = "https://basketball.realgm.com/international/league/59/Brazilian-NBB/team-stats" #URL with Team Stats
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

        url = "https://basketball.realgm.com/international/league/59/Brazilian-NBB/team-stats/2021/Averages/Opponent_Totals" #URL with Team Stats
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

        url = "https://basketball.realgm.com/international/league/59/Brazilian-NBB/team-stats/2021/Advanced_Stats/Team_Totals" #URL with Team Stats
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
    elif selection == '4':
        url = "https://sports.yahoo.com/nba/stats/team/?sortStatId=POINTS_PER_GAME&selectedTable=0" #URL with Team Stats
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
        TeamStats[['FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OR', 'DR', 'Reb', 'Ast', 'TO', 'Stl', 'Blk', 'PF', 'Pts']] = TeamStats[['FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OR', 'DR', 'Reb', 'Ast', 'TO', 'Stl', 'Blk', 'PF', 'Pts']].astype(float) #Converting stats from string to float
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

        url = "https://sports.yahoo.com/nba/stats/team/?sortStatId=POINTS_PER_GAME&selectedTable=1" #URL with Team Stats
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
        TeamStats[['FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OR', 'DR', 'Reb', 'Ast', 'TO', 'Stl', 'Blk', 'PF', 'Pts']] = TeamStats[['FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OR', 'DR', 'Reb', 'Ast', 'TO', 'Stl', 'Blk', 'PF', 'Pts']].astype(float) #Converting stats from string to float
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
        df = pd.read_csv("C:\\Users\\eric-\\Documents\\GitHub\\Análises\\Scraping-EuroLeague-Stats\\Advanced Stats NBA.txt")
        print (df)
        toRound = df.describe()
        roundingDF = toRound.round(decimals=2)
        print (roundingDF)
    elif selection == '5':
        url = "https://fbref.com/en/comps/9/Premier-League-Stats" #URL with Team Stats
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
    elif selection == '6':
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
    elif selection == '7':
        url = "https://fbref.com/en/comps/20/Bundesliga-Stats" #URL with Team Stats
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
        FetchStatsColumnsDT = FetchStats.copy()
        FetchStatsColumnsDT.iloc[:, 1:] = FetchStatsColumnsDT.iloc[:, 1:].astype(float)
        #print(FetchStatsColumnsDT.rank(pct=True).round(decimals=2))
        FetchStatsColumns = FetchStatsColumns.drop(FetchStatsColumns.columns[0], axis = 1)
        FetchStatsColumns= FetchStatsColumns.astype(float)
        toRound = FetchStatsColumns.describe()
        RoundingDF = toRound.round(decimals = 2)
        print (RoundingDF) 
    elif selection == '8':

        df = pd.read_csv("C:\\Users\\eric-\\Documents\\GitHub\\Análises\\Scraping-EuroLeague-Stats\\NHL.txt")
        df_AVG = df
        df_AVG[['PTS', 'GF', 'GA', 'EVGF', 'EVGA', 'PP', 'PPO', 'PPA', 'PPOA', 'S', 'SA']] = df_AVG[['PTS', 'GF', 'GA', 'EVGF', 'EVGA', 'PP', 'PPO', 'PPA', 'PPOA', 'S', 'SA']].div(df['GP'].values, axis = 0)
        toDrop = df_AVG[['OL', 'PTS', 'SOW', 'SOL', 'SH', 'SHA', 'SO', 'PP', 'PPO', 'PPA', 'PPOA', 'AvAge', 'Rk']]
        df_AVG = df_AVG.drop(toDrop.columns, axis = 1)
        df_AVG = df_AVG.dropna()
        roundingDF = df_AVG.round(decimals = 2)
        print (roundingDF)
        roundingDFD = roundingDF.describe()
        print (roundingDFD.round(decimals = 2))
        print (roundingDF.rank(pct=True).round(decimals=2))
    elif selection == '9':
        df = pd.read_csv("C:\\Users\\eric-\\Documents\\GitHub\\Análises\\Scraping-EuroLeague-Stats\\Player.txt")
        toRound = df.describe()
        roundingDF = toRound.round(decimals=2)
        print (roundingDF)
        cat = input("PTS, TRB ou AST?")
        plt.scatter(df.G, df[cat])
        plt.show()
        df.boxplot(column=[cat])
        plt.show()
        y = df[cat]
        x = df.G
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        print(model.summary())
        fig = plt.figure(figsize=(12,8))
        fig = sm.graphics.plot_regress_exog(model, 'G', fig=fig)
        res = model.resid
        fig = sm.qqplot(res, fit=True, line="45")
        plt.show()
        
        teste = df.loc[:, ['G', cat]]
        X = teste.iloc[:, :-1].values
        y = teste.iloc[:, 1].values
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        print(regressor.intercept_)
        print(regressor.coef_)
        y_pred = regressor.predict(X_test)
        df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
        print(df)
        from sklearn import metrics
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        teste1 = regressor.intercept_
        teste2 = regressor.coef_
        teste1 = float(teste1)
        teste2 = float(teste2)
        Xnew = [[teste1], [teste2]]
        ynew = regressor.predict(Xnew)
        print (ynew[0])   
    elif selection == '10':
        df = pd.read_csv("C:\\Users\\eric-\\Documents\\GitHub\\Análises\\Scraping-EuroLeague-Stats\\Player NHL.txt")
        toRound = df.describe()
        roundingDF = toRound.round(decimals=2)
        print (roundingDF)
        cat = input("G.1, A, S, +/- ou SV?")
        plt.scatter(df.G, df[cat])
        plt.show()
        df.boxplot(column=[cat])
        plt.show()
        y = df[cat]
        x = df.G
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        print(model.summary())
        fig = plt.figure(figsize=(12,8))
        fig = sm.graphics.plot_regress_exog(model, 'G', fig=fig)
        res = model.resid
        fig = sm.qqplot(res, fit=True, line="45")
        plt.show()
        teste = df.loc[:, ['G', cat]]
        X = teste.iloc[:, :-1].values
        y = teste.iloc[:, 1].values
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        print(regressor.intercept_)
        print(regressor.coef_)
        y_pred = regressor.predict(X_test)
        df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
        print(df)
        from sklearn import metrics
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        teste1 = regressor.intercept_
        teste2 = regressor.coef_
        teste1 = float(teste1)
        teste2 = float(teste2)
        Xnew = [[teste1], [teste2]]
        ynew = regressor.predict(Xnew)
        print (ynew[0])
    elif selection == '0': 
      break
    elif selection == '11':
        features = pd.read_csv("C:\\Users\\eric-\\Documents\\GitHub\\Análises\\Scraping-EuroLeague-Stats\\MLTG.txt")
        print(features.describe())
        cat = input("PTS, TRB ou AST? ")
        features = pd.get_dummies(features)
        labels = np.array(features[cat])
        features= features.drop(['Rk', cat], axis = 1)
        feature_list = list(features.columns)
        features = np.array(features)
        features = np.nan_to_num(features)
        train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)
        rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
        rf.fit(train_features, train_labels);
        predictions = rf.predict(test_features)
        errors = abs(predictions - test_labels)
        print('Mean Absolute Error:', round(np.mean(errors), 2), cat)
        mape = 100 * (errors / test_labels)
        accuracy = 100 - np.mean(mape)
        print('Accuracy:', round(accuracy, 2), '%.')
        #importances = list(rf.feature_importances_)
        #feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
        #feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
        #[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];
        y_pred = rf.predict(test_features)
        df = pd.DataFrame({'Actual': test_labels, 'Predicted': y_pred})
        print(df)
        #print(rf.predict(features))
        future = rf.predict(features[0:10])
        print (future)
        media = np.mean(future)
        print (media)
        
        #my_model = XGBRegressor()
        #my_model.fit(train_features, train_labels)
        #predictions = my_model.predict(X_valid)
        #print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))
        #my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
        #my_model.fit(train_features, train_labels, 
             #early_stopping_rounds=5, 
             #eval_set=[(X_valid, y_valid)],
             #verbose=False)
        #predictions = my_model.predict(X_valid)
        #print (predictions)
    else: 
      print("Unknown Option Selected!") 