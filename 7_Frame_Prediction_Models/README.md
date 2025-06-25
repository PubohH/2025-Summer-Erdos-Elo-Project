This folder contains training and comparison of regression models used to predict percentage of frames player 1 wins in a match. The models are compared with Elo predictions and a baseline model. 

## Features and Train-test split

The models are trained, cross validated and compared on 3 feature sets.

**Feature Set 1**: features based on player statistics only (elo rankings and predictions omitted)

**Feature Set 2**: features based on player statistic differences

**Feature Set 3**: all available features

The dataset, consisting of matches from the last 300 tournaments, included 34,521 matches ordered chronologically from earliest to most recent. The most recent 20% of matches were set aside for testing the models.

## Test Performance
Model performances were compared using mean absolute error (MAE) on the test set.

<div style="display: flex; gap: 10px;">
  <img src="Assets/MAE_without_elo.png" alt="Performance Plot1" width="47%">
  <img src="Assets/MAE_with_elo.png" alt="Performance Plot2" width="47%">
</div>


