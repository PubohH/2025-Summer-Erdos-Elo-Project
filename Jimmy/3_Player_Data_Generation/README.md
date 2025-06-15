# Data Generation
We folder contains the code we wrote to generate matches dataset using the generate_stats method from [elo rating system v4](/2_Elo_Rating_System/elo_v4/elo_v4.py) and [match data](/1_Match_Data/matches.csv) from 1982 to 2025. The data generation process can be found in [data_generation.ipynb](/3_Player_Data_Generation/data_generation.ipynb).

## Final datasets
1. [match_data_10_tourns.csv](/3_Player_Data_Generation/match_data_10_tourns.csv): match information together with players' statistics in the last 10 tournaments.  
2. [match_data_20_tourns.csv](/3_Player_Data_Generation/match_data_20_tourns.csv): match information together with players' statistics in the last 20 tournaments.
3. [match_data_20_tourns_modified.csv](/3_Player_Data_Generation/match_data_20_tourns_modified.csv): match information together with players' statistics obtain by swapping player1 and player2 for half of the matches from previous dataset (since in [match_data_20_tourns.csv](/3_Player_Data_Generation/match_data_20_tourns.csv), player1 is always the winner).

## Columns of the datasets
Player names: ['player1', 'player2'].  
Match information: ['best_of'].  
Players' statistics (before they attend the corresponding tournament):  
['p1_matches_played', 'p1_matches_won','p1_frames_played', 'p1_frames_won',  
'p2_matches_played', 'p2_matches_won', 'p2_frames_played', 'p2_frames_won',  
'p1_frames_played_1_year', 'p1_frames_won_1_year', 'p1_frames_played_3_years', 'p1_frames_won_3_years',  
'p2_frames_played_1_year', 'p2_frames_won_1_year', 'p2_frames_played_3_years', 'p2_frames_won_3_years'].   
Match results: ['match_result', 'win_percentage']. 

Notice: 
1. in the match_result column, 0 means player1 wins while 1 means player2 wins.
2. The 'win_percentage' represent the proportion of frames player1 won. It is calculated as $\frac{\text{score1}}{\text{score1}+\text{score2}}$.