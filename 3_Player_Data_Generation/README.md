# Data Generation
We folder contains the code we wrote to generate matches dataset using the generate_stats method from [elo rating system v4](/2_Elo_Rating_System/elo_v4/elo_v4.py) and [match data](/1_Match_Data/matches.csv) from 1982 to 2025. The data contains the matches information for the last 50 tournaments together players's stats such as elo ratings, matches played, etc. The data generation process can be found in [data_generation.ipynb](/3_Player_Data_Generation/data_generation.ipynb).

## Final datasets 
[match_data_300_tourns_modified.csv](/3_Player_Data_Generation/match_data_300_tourns_modified.csv): match information of the matches from the last 300 tournaments together with players' statistics at the moment players enter the corresponding tournament. Since in the [original matches dataset](/1_Match_Data/matches.csv), player1 is always the winner, we swap the two player, their stats and match results for half of the matches for the convenience of later modeling.


## Columns of the datasets
**Player names:** ['player1', 'player2'].  
**Match information:** ['best_of'].  
**Players' elo_rating:** ['player1_elo', 'player2_elo'].  
**Players' win rate predicted by elo:** ['elo_match_win_rate', 'elo_frame_win_rate'].  
**Players' statistics:**  
['p1_matches_played', 'p1_matches_won','p1_frames_played', 'p1_frames_won',  
'p2_matches_played', 'p2_matches_won', 'p2_frames_played', 'p2_frames_won',  
**Players' statistics by yearss:**  
'p1_frames_played_1_year', 'p1_frames_won_1_year', 'p1_frames_played_3_years', 'p1_frames_won_3_years',  
'p2_frames_played_1_year', 'p2_frames_won_1_year', 'p2_frames_played_3_years', 'p2_frames_won_3_years'].   
**Match results:** ['score1', 'score2', 'match_result', 'win_percentage'].  
**Tournament id:** 'tournament_id'. 

Notice: 
1. In the 'match_result' column, 0 means player1 wins while 1 means player2 wins.
2. 'win_percentage' represent the proportion of frames player1 won. It is calculated as $\frac{\text{score1}}{\text{score1}+\text{score2}}$.