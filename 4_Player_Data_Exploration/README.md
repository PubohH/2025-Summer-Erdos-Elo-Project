# Data Exploration
This folder contains a notebook that we explore the [dataset](/3_Player_Data_Generation/match_data_300_tourns_modified.csv) generated from matches in the last 300 tournaments together with players' stats at the moment they enter the corresponding tournment. The data can be found in the folder [3_Player_Data_Generation](/3_Player_Data_Generation). We summarize our discoveries below.

1. We plot the rolling average of prediction result (accuracy) over 1000 and 2000 matches. 
we see that the performance of prediction by our elo rating system is fluctuating and drops significantly on the last 1000-2000 matches. We suspect that there are lots of matches that are not at the highest level are recorded and the players are not as experienced as the top players and don't have much professional matches record. Since the elo rating and their stats are not well established, their matches are harder to predict comparing to professional level players.  
For example, Pubo pointed out that Q school is a series of tournaments among amateurs happening in the early seaon every year which serves as qualification school for world snooker tour. These tournaments are among amateur players but still marked as professional level by our data source cuetracker.net. The first two graphs below shows the number of matches played by player1 before and after dropping Q school matches. We do see that lots of matches with exceptionally low p1_matches_played are excluded. However, after we dropped Q school matches, the prediction accuracy by elo rating is still not consistent. 

<p float="left">
<img src="/Users/tliu/Desktop/2025-Summer-Erdos-Elo-Project/4_Player_Data_Exploration/Assets/matches_played_before.png" alt="before" height =40% width=40%>
<img src="/Users/tliu/Desktop/2025-Summer-Erdos-Elo-Project/4_Player_Data_Exploration/Assets/matches_played_after.png" alt="after" height = 40% width=40%>
</p>.  

<p float="left">
<img src="/Users/tliu/Desktop/2025-Summer-Erdos-Elo-Project/4_Player_Data_Exploration/Assets/pre_1000_before.png" alt="before" height =40% width=40%>
<img src="/Users/tliu/Desktop/2025-Summer-Erdos-Elo-Project/4_Player_Data_Exploration/Assets/pred_1000_after.png" alt="after" height = 40% width=40%>  
</p>.  

2. From the heatmap, we see that one player's multiple stats can be highly correlated to themselves (e.g. p1_matches_played, e.g. p1_matches_won,  p1_matches_played_1_year,  p1_matches_won_1_year, etc).  
Also, from analysis in the elo rating system foler, we know for players with more than 100 matches, the elo rating has strong correlation with matches win rate and frames win rate. Therefore, PCA and other dimension reduction technique are necessary for modelings.  
We also see that the elo predicted matches win rates and frames win rate have the highest correlations 0.428 and 0.420 with win percentage, which makes them very strong features in later modeling.  

<img src="/Users/tliu/Desktop/2025-Summer-Erdos-Elo-Project/4_Player_Data_Exploration/Assets/heatmap.png" alt="heatmap" height = 50% width=50%>  
<img src="/Users/tliu/Desktop/2025-Summer-Erdos-Elo-Project/4_Player_Data_Exploration/Assets/elo_vs_matches.png" alt="heatmap" height = 50% width=50%>  
<img src="/Users/tliu/Desktop/2025-Summer-Erdos-Elo-Project/4_Player_Data_Exploration/Assets/elo_vs_frames.png" alt="heatmap" height = 50% width=50%>  