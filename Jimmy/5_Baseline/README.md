# Baseline Models
We built several baseline models to predict match result or frame win percentage or both. We recorded the accuracy scores and mse respectively. 

## Baseline 1
This baseline model simply uses the World Snooker Rankings from 1981 to 2019 to predict the winner. For example, to predict a match in 2015, we use the ranking from 2014 and predict the winner to be the player with higher ranking. If both players' rankings are missing, we use random number generator to predict.  

The [ranking data](https://www.kaggle.com/datasets/sjenkins97/world-snooker-rankings-19812019) is provided by Kaggle user SCOTT JEMKINS.

We predicted the match results for the 750th, 800th, 999th and 1080th tournament, each happened in 2013, 2014, 2022 and 2025. We run each prediction five times. The average accuracy scores are around 0.570, 0.595, 0.609 and 0.5866. The prediction for the 1080th tournament is inconsistent for the reason that rankings information after 2019 is missing and random number generator is used in this model. For more details, see [baseline1.ipynb](/Baseline/baseline1/baseline1.ipynb).

## Baseline 2
We build a baseline model to predict the frames win percentage by player1. In particular, the model predict the player with higher elo rating to be the winner. Then it calculates the average frame win percentage p on the traininig set. It predicts the expected winner sto have frame win percentage p and losers to have 1-p.  

The dataset we use is [match_data_50_tourns_modified.csv](/3_Player_Data_Generation/match_data_50_tourns_modified.csv). It has the matches data of the last 20 professional snooker tournaments.

The rmse is 0.309.
