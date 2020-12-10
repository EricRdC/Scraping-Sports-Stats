def print_menu():
    print("1. EuroLeague.") 
    print("2. EuroCup.") 
    print("3. NBB.") 
    print("4. CBA.") 
    print("5. EPL.") 
    print("6. Italy Serie A.") 
    print("7. Bundesliga.") 
    print("8. NCAAF.") 
    print("9. NFL.") 
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
    elif selection == '3':
        import urllib.request
        from bs4 import BeautifulSoup #Initializing libraries
        import requests
        import csv
        import pandas as pd
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
        import urllib.request
        from bs4 import BeautifulSoup #Initializing libraries
        import requests
        import csv
        import pandas as pd
        url = "https://basketball.realgm.com/international/league/40/Chinese-CBA/team-stats" #URL with Team Stats
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

        url = "https://basketball.realgm.com/international/league/40/Chinese-CBA/team-stats/2021/Averages/Opponent_Totals" #URL with Team Stats
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

        url = "https://basketball.realgm.com/international/league/40/Chinese-CBA/team-stats/2021/Advanced_Stats/Opponent_Totals" #URL with Team Stats
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
    elif selection == '5':
        import urllib.request
        from bs4 import BeautifulSoup #Initializing libraries
        import requests
        import csv
        import pandas as pd
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
    elif selection == '7':
        import urllib.request
        from bs4 import BeautifulSoup #Initializing libraries
        import requests
        import csv
        import pandas as pd
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
    elif selection == '8':
        import urllib.request
        from bs4 import BeautifulSoup #Initializing libraries
        import requests
        import csv
        import pandas as pd
        pd.set_option('display.max_rows', None)
        url = "https://www.footballdb.com/college-football/stats/teamstat.html?group=O&cat=T&yr=2020&lg=FBS" #URL with Team Stats
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
        #print (FetchStats)
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
        url = "https://www.footballdb.com/college-football/stats/teamstat.html?group=D&cat=T&yr=2020&lg=FBS" #URL with Team Stats
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
        #print (FetchStats)
        FetchStatsColumns = FetchStats.copy()
        FetchStatsColumns.iloc[:, 1:] = FetchStatsColumns.iloc[:, 1:].astype(float)
        #print(FetchStatsColumns.rank(pct=True).round(decimals=2))
        FetchStatsColumns = FetchStatsColumns.drop(FetchStatsColumns.columns[0], axis = 1)
        FetchStatsColumns= FetchStatsColumns.astype(float)
        toRound = FetchStatsColumns.describe()
        RoundingDF = toRound.round(decimals = 2)
        print (RoundingDF) 
    elif selection == '9':
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
        FetchStatsColumnsDT = FetchStats.copy()
        FetchStatsColumnsDT.iloc[:, 1:] = FetchStatsColumnsDT.iloc[:, 1:].astype(float)
        #print(FetchStatsColumnsDT.rank(pct=True).round(decimals=2))
        FetchStatsColumns = FetchStatsColumns.drop(FetchStatsColumns.columns[0], axis = 1)
        FetchStatsColumns= FetchStatsColumns.astype(float)
        toRound = FetchStatsColumns.describe()
        RoundingDF = toRound.round(decimals = 2)
        print (RoundingDF) 
    elif selection == '0': 
      break
    else: 
      print("Unknown Option Selected!") 