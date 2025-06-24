# Project Name?

## Group Membters: Pubo Huang, Tianxiang (Jimmy) Liu, Rubaiyat Bin Islam  

## Project Overview. 


## Elo Rating System  
The Elo Rating System assign each player a number that represents the skill levels in a zero-sum games. We built a elo rating system for professional snooker players so that the difference of two players rating predicts the win rate of one player in one frame. If we let R1 and R2 denote the elo-rating for player1 and player2, then the expected winrate of player1 is $E1 = \frac{1}{1 + e^{(R2-R1)/400}}$.  

We update players' elo ratings after each match. The update rule is the following:  
Suppose player1 and player2 play a match and the scores are score1 and score2. Then their actual frame win rate is $S1 = \frac{\text{score1}}{\text{score1}+\text{score2}}$ and $S2 = \frac{\text{score2}}{\text{score1}+\text{score2}}$.  
After this match, the elo-rating for player1 will be updated: 
$R1_{new} = R1 + K * (\text{score1}+\text{score2}) * (S1-E1)$,  
where K is the K-factor which we sets to 8. We picked this K-factor after [experimenting](/2_Elo_Rating_System/elo_v4/elo_v4_test2.ipynb) a broad range of values from 4 to 30. 

## Dataset (Acquisition, Cleaning and Generation):
We acquired snooker [match data (1982-2020)](https://www.kaggle.com/datasets/rusiano/snooker-data-19822020) from Kaggle submitted by user rusiano. The data comes from [cuetracker.net](cuetracker.net), which is used by many parties including bookmakers and sport commentators. We scaped the data from 2020 to 2025 directly from [cuetracker.net](cuetracker.net).  

We dropped the walkover matches, those with score 0-0, and amateur and pro-am matches. We cleaned the players' names columns by removing the unnecessary numbers and country names to prevent duplication of players. We also sorted the matches by tournament start date and , within a tournament, by the order of stages. Finally, we combined two datasets to form a dataset of 115,630 professional snooker matches from 1982 to 2025 and store it as [matches.csv](/1_Match_Data/matches.csv).  

Since the above data only contains the match result, we need to generate features for modelings. To generate the data for future modeling, we used our [elo rating system](/2_Elo_Rating_System/elo_v4). In particular, for the matches in the last 300 tournaments, we calculated the elo ratings and statistics (such as matches played, frames played) at the moment the players entered the tournament. We also calculated the win rates of player1 predicted by elo rating system and append them to each match data. Finally, we get the data of matches in the last 300 tournmaents (34,521 matches) together with players' names, players' elo ratings, elo predicted win rate, players' statistics and match results. The data is stored as [match_data_300_tourns_modified.csv](/3_Player_Data_Generation/match_data_300_tourns_modified.csv).