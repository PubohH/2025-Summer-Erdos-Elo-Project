This Folder contains different models that are trained to predict the match outcome when two players play head-to-head.
Note that this is different from the next folder, in which specific scores of each match is predicted. Here we simply predict whether
player1 wins or lose.

## Features and Train-Test Split
We trained the models using the match data [matches.csv](../1_Match_Data/matches.csv) . The most recent 20% of the matches are 
used as test set, and the rest are trained and cross-validated on 1. all features 2. all features except Elo.

## Accuracy Comparisons between different models.

The models we used are: Elo rating system, Logistic Regression, Random Forest, XGBoost, Linear Discriminant Analysis, and Support Vector Classification. The metric we used is accuracy, it is simply the ratio of number of correct predictions to the number of all predictions.

<div style="display: flex; gap: 25px;">
<img src="../6_Match_Prediciton_Models/assets/comparison with Elo.png" alt="comparison 1" width="50%"/>
<img src="../6_Match_Prediciton_Models/assets/comparison without elo.png" alt="comparison 1" width="50%"/>
</div>
