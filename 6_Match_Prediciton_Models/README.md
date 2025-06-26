This Folder contains different models that are trained to predict the match outcome when two players play head-to-head.
Note that this is different from the next folder, in which specific scores of each match is predicted. Here we simply predict whether
player1 wins or lose.

## Features and Train-Test Split
We trained the models using the data containing matches from the last 300 tournaments [match_data_300_tourns_modified.csv](../3_Player_Data_Generation/match_data_300_tourns_modified.csv).  The most recent 20% of the matches are 
used as test set, and the rest are trained and cross-validated on 1. all features and 2. all features except Elo.

## Accuracy Comparisons between different models.

The models we used are: Elo rating system, Logistic Regression, Random Forest, XGBoost, Linear Discriminant Analysis, and Support Vector Classification. The metric we used is accuracy, it is simply the ratio of number of correct predictions to the number of all predictions.

<div style="display: flex; gap: 25px;">
<img src="../6_Match_Prediciton_Models/assets/comparison with Elo.png" alt="comparison 1" width="47%"/>
<img src="../6_Match_Prediciton_Models/assets/comparison without elo.png" alt="comparison 1" width="47%"/>
</div>

We see that Elo already achieves 67.2% accuracy in predicting match outcomes. This accuracy is comparable to other models that use elo and many more other features. Thus Elo rating is a good feature in predicting match outcomes. In addition, with Elo rating feature included, all other models had, on average, a 2.0% accuracy boost.

Another thing to note here is that the Elo system, by definition, uses logistic function to calculate the frame winrate. In other words, the relationship between Elo difference (R2-R1) against the frame winrate of player1 is exactly logistic. We can also see that the accuracy of logistic regression is only slightly higher than the Elo model.
