# Elo Rating System
In this folder, we built 4 versions of elo rating system that rate the professional snooker players. The final version is version 4, which is in the [elo_v4 folder](elo_v4).  
  
In [version1](/2_Elo_Rating_System/elo_v1), we built a sequence of methods that returns elo rating after inputing histrocial snooker matches. These methods form the skeleton of later versions.

In [version2](/2_Elo_Rating_System/elo_v2), we tuned the parameter K-factor and update rules of the elo rating that returns a ranking very close to the [ranking](https://wpbsa.com/rankings/world-rankings/) provided by World Professional Billiards and Snooker Association (WPBSA). In this version, the update rules consider both match result and frames scores, but emphasize the former.  

In [version3](/2_Elo_Rating_System/elo_v3), the codes in version2 is rewritten in the form of a class. Futhuremore, we built the predict method, which, after updating the stats with historical matches, returns prection of match results and win rates for future matches.  

In [version4](/2_Elo_Rating_System/elo_v4), we refined the update rule from v3 after reconsidering what the elo rating should represent. In particular, the new update rule only considers frames scores (so that the difference between two players rating is correlated with their frame win rate). The match win rate can be calculated with frame win rate and binomial formula. We made this update because we want our elo rating system to reflect the frames win rate so that we can use them to predict the scores for future matches.

We added a method generate_stats, which takes in historical matches and return the players statistics together with the match information. We will use it to generate dataset for modeling.  

We also tested different K-factors and chose K=8 as the K-factor for our elo rating system. The testing process is in [elo_v4_test.ipynb](/2_Elo_Rating_System/elo_v4/elo_v4_test.ipynb).
  
We also explore the relations between players' elo rating and their match win rate. In particular, for those who have played more than 100 matches, the elo rating is positively correlated to their match win rate and frame win rate as the diagrams below show. There seems to be a linear relation between them.

![elo rating vs matches win rate](/2_Elo_Rating_System/elo_v4/elo_rating_vs_match_win_rate.png 'Figure1')
![elo rating vs frame win rate](/2_Elo_Rating_System/elo_v4/elo_rating_vs_frame_win_rate.png 'Figure2')
***

# Information about elo_v4
## Attributes
1. players: a numpy array of professional snooker players.
2. ratings: a pandas series of players elo_rating.
3. stats: a pandas dataframe with statistics of players such as elo_rating, winrate, etc.
4. stats_by_years: a pandas dataframes with statistics of players within three years and one year.

## Important methods
update_stats: After inputting historical matches (dataframe) and parameters (K-factor), this function updates all the above attributes.  
predict: input an array of pairs of players and best_of. Output the expected winner and expected match win rate and frame win rate.  
generate_stats: input historical matches. Output these matches together with statistics of players at the moment they attended the tournaments.

## Elo update rule
Let R1 and R2 denote the elo-rating for player1 and player2. Then the expected winrate of player1 is $E1 = \frac{1}{1 + e^{(R2-R1)/400}}$.  
Suppose player1 and player2 play a match and the scores are score1 and score2. Then their actual frame win rate is $S1 = \frac{\text{score1}}{\text{score1}+\text{score2}}$ and $S2 = \frac{\text{score2}}{\text{score1}+\text{score2}}$.  
After this match, the elo-rating for player1 will be updated: 
$R1_{new} = R1 + K * (\text{score1}+\text{score2}) * (S1-E1)$,  
where K is the K-factor which we sets to 8, n denotes best_of.

## Tests of K-factors and results
In [elo_v4_test.ipynb](/2_Elo_Rating_System/elo_v4/elo_v4_test.ipynb), we use elo rating system version 4 with 5 different K-factors to predict match results of 4 tournaments. The following two arrays are the K-factors and the index of tournmament we tested:  
Ks = [4, 6, 8, 15, 20].  
nth = [750, 999, 1040, 1080].  

The average prediction accuracy score on match result:  
K=4:     0.698769   
K=6:     0.708306   
K=8:     0.705024  
K=15:    0.711233  
K=20:    0.700445  

The average mse of prediction on player1's frames win percentage:  
K=4:     0.044480   
K=6:     0.043825  
K=8:     0.043568  
K=15:    0.043630  
K=20:   0.043921  

They have very close test results. Finally, we decided to have K=8 as the K-factor of our elo rating system.  

Notice: 
1. From elo_v3, we know larger K-factors (e.g. K=30) still produce good ranking and prediction on match result but do poorly on predicting frames win rate. Also, each test needs to loop through around 100k matches and takes around 1 min. Therefore, we only test the above values for K-factors. 
2. A player named Zhao Xintong has been banned from 2023 to 2024 for match fixing but won 2025 World Snooker Championship after he returned. His elo rating difference before and after this tournament can reach 300 or even more depending on the K-factor. For large K-factor, he will be the rank one in our elo ranking and has elo rating at least 200 higher than all other top players, which makes it a bad ranking because we don't expect this much change of elo rating after only one tournament. Therefore, we have paid lots of attention to his ranking when tuning the K-factor.