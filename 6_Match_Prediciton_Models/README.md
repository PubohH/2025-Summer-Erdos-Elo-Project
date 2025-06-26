This Folder contains different models that are trained to predict the match outcome when two players play head-to-head.
Note that this is different from the next folder, in which specific scores of each match is predicted. Here we simply predict whether
player1 wins or lose.

## Features and Train-Test Split
We trained the models using the match data [matches.csv](../1_Match_Data/matches.csv) . The most recent 20% of the matches are 
used as test set, and the rest are trained and cross-validated on 1. all features 2. all features except Elo.


we use the data from 
