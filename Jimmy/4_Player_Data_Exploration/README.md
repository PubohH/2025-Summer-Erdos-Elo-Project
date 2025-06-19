# Data Exploration
This folder contains a notebook that we explore the dataset generated from matches in the last 50 tournaments together with players' stats at the moment they enter the corresponding tournment. The data can be found in the folder [3_Player_Data_Generation](/3_Player_Data_Generation). We summarize our discoveries below.

1. We plot the rolling average of prediction result (accuracy) over 1000 and 2000 matches. 
we see that the performance of prediction by our elo rating system drops significantly on the last 1000-2000 matches. We suspect that there are lots of matches that are not at the highest level are recorded and the players are not as experienced as the top players and don't have much professional matches record. Since the elo rating and their stats are not well established, their matches are harder to predict comparing to professional level players. For example, Pubo pointed out that Q school is a series of tournaments among amateurs happening in the early seaon every year which serves as qualification school for world snooker tour. These tournaments are among amateur players but still marked as professional level by our data source cuetracker.net. The graphs below shows the number of matches played by player1 before and after dropping Q school matches. We do see that matches with exceptionally low p1_matches_played are excluded.  

!['before'](/4_Player_Data_Exploration/match_played_before.png)  
!['after'](/4_Player_Data_Exploration/match_played_after.png)


However, after we drop Q school matches, the prediction accuracy by elo rating is still not consistent. 
!['before'](/4_Player_Data_Exploration/pred_1000_before.png) 
!['after'](/4_Player_Data_Exploration/pred_1000_after.png)  

2. In the correlation analysis, we see that one player's multiple stats can be highly correlated to themselves (e.g. p1_matches_played, e.g. p1_matches_won,  p1_matches_played_1_year,  p1_matches_won_1_year, etc). Therefore, PCA and other dimensional reduction technique might be necessary for modelings.  

Also, we see that the elo predicted win rates have the highest correlation 0.42 with win percentage, which makes them very strong features in later modeling.

