#THIS IS VARIABLES FILE WHERE WE NEED TO UPDATE VARIABLES

#api end point where total points per each player are obtained
link = 'https://a.fanzy.in/v5/tournaments/314/compareUsers?fUID='

#Name of google sheet used for this contest
google_sheet_name = 'Python_Automation'

#keys in "player_information" dictionary are names of players in the contest 
#values in the list in "player_information" are as below according to corresponding index
#0: fanzy id of corresponding person
#1: total points after api call
#2: latest match points
#3: row number of player for points table
#4: row number of player for earnings table
#5: row number of player for medals chart 
player_information = {"Mohith":["742873",0,0,3,15,26],"Chakri":["668570",0,0,4,16,27],"Alwala":["783789",0,0,5,17,28], 
            "Kaushik":["684745",0,0,6,18,29],"Chengal": ["212290",0,0,7,19,30],"Nagi":["738875",0,0,8,20,31],
            "Sankeerth":["224755",0,0,9,21,32]} 

#Total number of players participating in contest
number_of_players = 7

#The order in which earnings are split according to rank for each match 
#in this case, after every match top player gets 132/- second player gets 60/- and so on 
earnings_list = [132,60,8,-50,-50,-50,-50]

#The row and column in google sheet where leader board appears
leader_board_cell = [26,8]

#The row and column in google sheet where date and time the script last ran appears
date_time_cell = [11,1]

