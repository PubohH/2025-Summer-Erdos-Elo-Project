This is a summary of elo_v3.py. 

# Class
In the elo_v3.py, we build a class called elo_rating. 
This class can produce elo_ratings and make prediction for future games of professional snookers.

# Attributes.
1. players: a numpy array of professional snooker players.
2. ratings: a pandas series of players elo_rating.
3. stats: a pandas dataframe with statistics of players such as elo_rating, winrate, etc.
4. stats_by_years: a pandas dataframes with statistics of players within three years or one year.

# Important methods
update_stats: After inputting historical matches (dataframe) and parameters (K-factor, ratio)
              this function updates all the above attributes.
predict: input an array of pairs of players
         output the expected winner and expected winrate of player1. 

# Testing Notebooks
1. In 'elo_v3 test.ipynb', we tested the above functions and attributes.
2. In 'elo_v3 test2.ipynb', we use the 'predict' function to predict the winners of matches in certain years and compare them with the actual winners. Our prediciton algorithm performs better than simply look at the rankings from the previous year.
3. In 'elo_v3 test3.ipynb', we use the 'predict' function to predict the winrate of matches in certain tournaments and compare them with actual frames winrate.
4. In 'elo_v3 test4.ipynb', 

# Conclusions
1. The elo_rating systems have some flexibilities. For example, we can modify the K-factor, or the updating rules to get different results. 
2. Unlike the classic elo_rating system, our update rule consider both matches result (the winner) and the frames scores. For example, if player1 has 90% win rate against player2 and ends up having a match with a very closed score such as 9-8, then player1's elo increases since player1 is the winner and won't increase as much as the classic rating system as he is expected to win 90% of the frames.
3. Different K-factor(ranging from 2 to 30) won't affect too much of the accuracy of predictions of the winner. But large K-factors (those above 20) have poor performance in predicting the win rate. 
4. Since our data only contains matches starting from 1980 and all players are assigned with 1000 elo rating, their elo rating won't reflect their win rate that much in early years. However, it won't affect the prediciton in 2020 that much.
