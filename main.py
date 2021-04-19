from excel import gsheet
from fanzy_pull import points
from datetime import datetime
import pytz
from variables import leader_board_cell, earnings_list, player_information, date_time_cell
import variables

uid_data = points().score_pull(player_information)    #uid_data[key][1] updated with total points
sheet = gsheet().get_sheet()           #working gsheet obtained
col = gsheet().get_col(sheet,3)        #column to add data obtained
num_zeros = variables.number_of_players

def points_update(num_zeros):
    for key in uid_data:
        uid_data[key][2] = int(uid_data[key][1]) - int(sheet.cell(uid_data[key][3], 2).value) 
        #total points from api minus total in sheet. i.e. latest match points added to uid_data[key][2] 
        if uid_data[key][2] == 0:
            num_zeros = num_zeros - 1
    if num_zeros != 0:
        latest_points_column_update()
    return num_zeros

def latest_points_column_update():
    for key in uid_data:
        sheet.update_cell(uid_data[key][3], col, uid_data[key][2]) 

def latest_match_ranking_in_dict_format():
    sorted_dict = dict(sorted(uid_data.items(), key=lambda  x:-x[1][2])) 
    return sorted_dict

def earnings_update():
    sorted_d = latest_match_ranking_in_dict_format()
    for key in sorted_d:
        index = list(sorted_d.keys()).index(key) 
        sheet.update_cell(sorted_d[key][4], col, earnings_list[index]) 

def date_time_update():
    ist = pytz.timezone('Asia/Kolkata')
    dt_in_ist = datetime.now(ist)
    dt_string = dt_in_ist.strftime("%B %d,%Y %I:%M %p")
    sheet.update_cell(date_time_cell[0], date_time_cell[1], "The automation script last ran at " + dt_string + " IST")

def leader_board_update():
    for key in latest_match_ranking_in_dict_format():
        sheet.update_cell(leader_board_cell[0], leader_board_cell[1], key)
        leader_board_cell[0] = leader_board_cell[0] + 1

def medals_chart_update():
    sorted_d = latest_match_ranking_in_dict_format()
    column_to_update = 2 
    for i in range(3):
        medal = list(sorted_d.keys())[i] 
        medal_count = int(sheet.cell(uid_data[medal][5],column_to_update).value) + 1
        sheet.update_cell(uid_data[medal][5],column_to_update,medal_count)
        column_to_update = column_to_update + 1


def main():
    date_time_update()
    to_run = points_update(num_zeros)
    if to_run != 0:
        earnings_update()
        leader_board_update()
        medals_chart_update()

if __name__ == "__main__":
    main()

