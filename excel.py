import gspread
from oauth2client.service_account import ServiceAccountCredentials
from variables import google_sheet_name

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open(google_sheet_name).sheet1

class gsheet:
    def get_sheet(self):
        return sheet
    def get_col(self,sheet,row):
        temp = True
        col = 1
        while temp is True:
            if sheet.cell(row,col).value is not None:
                col = col + 1
            else:
                temp = False
        return col

