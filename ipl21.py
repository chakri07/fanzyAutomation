from bs4 import BeautifulSoup
from scoreInterface import scoreInterface
from sheet import gsheets
import requests
import json
import time

#0 = uid
#1 = latest tourni score
#2 = row in the score sheet
#3 = current match score
uid_data = {"Mohith":["742873","0",3,100],"Chandan":["783789","0",5,200], "Chakri":["668570","0",4,0], "Chengal":["212290","0",7,0],"Sankeerth": ["224755","0",9,0],
            "Kaushik":["684745","0", 6,0],"Nagi":["738875","0",8,0]}

balancefor7 = [132,60,8,-50, -50, -50 , -50]
balancefor6= [116,44,0,-50, -50, -50]
dailyLeaderBoardCell = [16,4]

def updateScoreinSheet(scoreSheet,colToUpdate):
    for key in uid_data:
        scoreSheet.update_cell(uid_data[key][2],colToUpdate,uid_data[key][3])

def dailyRanking():
    match_rankin=dict(sorted(uid_data.items(),key= lambda x:-x[1][3]))
    return match_rankin

def scoreUpdate(players):
    si = scoreInterface()
    si.get_latest_tourni_score(uid_data)
    scoreSheet = gsheets().getscoreSheet()
    colToUpdate = gsheets().getColtoUpdate(scoreSheet,3)
    for key in uid_data:
        currentTourniScore = scoreSheet.cell(uid_data[key][2],2).value
        uid_data[key][3] = (int(uid_data[key][1]) - int(currentTourniScore))
        if uid_data[key][3] == 0:
            players = players-1
    if players!= 0 :
        updateScoreinSheet(scoreSheet,colToUpdate)
    return players


def playerMoneyUpdate(moneySheet,match_rankin,colToUpdate):
        keys =list(match_rankin.keys())
        for i in range(0,len(keys)):
            moneySheet.update_cell(match_rankin[keys[i]][2],colToUpdate,balancefor7[i])

def moneyUpdate():
    moneySheet = gsheets().getBalanceSheet()
    #same dict but sorted
    match_rankin=dailyRanking()
    colToUpdate = gsheets().getColtoUpdate(moneySheet,3) 
    playerMoneyUpdate(moneySheet,match_rankin,colToUpdate)
    return

def leaderBoardUpdate():
    scoreSheet = gsheets().getscoreSheet()
    for key in dailyRanking():
        scoreSheet.update_cell(dailyLeaderBoardCell[0],dailyLeaderBoardCell[1],key)
        dailyLeaderBoardCell[0] = dailyLeaderBoardCell[0] + 1

def main(): 
    players =7
    players = scoreUpdate(players)
    if players!=0:
        moneyUpdate()
        leaderBoardUpdate()
    
    now = time.asctime( time.localtime(time.time()) )
    gsheets().getscoreSheet().update_acell('A13', "script ran last at " + now)
    return
   
if __name__ == "__main__":
    main()
