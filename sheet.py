import gspread
from oauth2client.service_account import ServiceAccountCredentials

class gsheets:
    url = "https://docs.google.com/spreadsheets/d/1jJYPz_SjvImLkQqFGT-jYDGk2L73nqGGyLZBgRaB4V4/edit#gid=0"
    gc = gspread.service_account(filename='auth_credentials.json')

    def getscoreSheet(self):
        scoreSheet = self.gc.open_by_url(self.url).worksheet("score")
        return scoreSheet
    
    def getBalanceSheet(self):
        BalanceSheet = self.gc.open_by_url(self.url).worksheet("money")
        return BalanceSheet

    def getColtoUpdate(self,scoreSheet,row_index):
        emptyCell = False
        col = 1
        while emptyCell is not True:
            if scoreSheet.cell(row_index,col).value is not None:
                col = col+1
            else:
                emptyCell = True
        return col
