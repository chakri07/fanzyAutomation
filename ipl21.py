from bs4 import BeautifulSoup
from scoreInterface import scoreInterface
from sheet import gsheets
import requests
import json

#0 = uid
#1 = latest tourni score
#2 = row in the score sheet
#3 = row_index in the money sheet
#4 = score of the latest match
uid_data = {"Mohith":["742873","0",3,100],"Chandan":["783789","0",5,200], "Chakri":["668570","0",4,0], "Chengal":["212290","0",7,0],"Sankeerth": ["224755","0",9,0],
            "Kaushik":["684745","0", 6,0],"Nagi":["738875","0",8,0]}

balancefor7 = [132,60,8,-50, -50, -50 , -50]

def scoreUpdate():
    si = scoreInterface()
    si.get_latest_tourni_score(uid_data)
    scoreSheet = gsheets().getscoreSheet()
    colToUpdate = gsheets().getColtoUpdate(scoreSheet,3)
    for key in uid_data:
        currentTourniScore = scoreSheet.cell(uid_data[key][2],2).value
        uid_data[key][3] = (int(uid_data[key][1]) - int(currentTourniScore))
        scoreSheet.update_cell(uid_data[key][2],colToUpdate,uid_data[key][3])

def playerMoneyUpdate(moneySheet,match_rankin,colToUpdate):
        keys =list(match_rankin.keys())
        for i in range(0,len(keys)):
            moneySheet.update_cell(match_rankin[keys[i]][2],colToUpdate,balancefor7[i])

def moneyUpdate():
    moneySheet = gsheets().getBalanceSheet()
    #same dict but sorted
    match_rankin=dict(sorted(uid_data.items(),key= lambda x:-x[1][3]))
    colToUpdate = gsheets().getColtoUpdate(moneySheet,3) 
    playerMoneyUpdate(moneySheet,match_rankin,colToUpdate)
    return

def main():
    scoreUpdate()
    moneyUpdate()
    return
   
if __name__ == "__main__":
    main()





