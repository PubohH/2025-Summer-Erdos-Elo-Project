# Elo Rating System
In this folder, we built 4 versions of elo rating system that rate the professional snooker players. The final version is version 4, which is in the [elo_v4 folder](elo_v4).  
  
In [version1](/2_Elo_Rating_System/elo_v1), we built a sequence of methods that returns elo rating after inputing histrocial snooker matches. These methods form the skeleton of later versions.

In [version2](/2_Elo_Rating_System/elo_v2), we tuned the parameter K-factor and update rules of the elo rating that returns a ranking very close to the [ranking](https://wpbsa.com/rankings/world-rankings/) provided by World Professional Billiards and Snooker Association (WPBSA). In this version, the update rules consider both match result and frames scores, but emphasize the former.  

In [version3](/2_Elo_Rating_System/elo_v3), the codes in version2 is rewritten in the form of a class. Futhuremore, we built the predict method, which, after updating the stats with historical matches, returns prection of match results and win rates for future matches.  

In [version4](/2_Elo_Rating_System/elo_v4), we refined the update rule from v3 after reconsidering what the elo rating should represent. In particular, the new update rule only considers frames scores (so that the difference between two players rating is correlated with their frame win rate). The match win rate can be calculated with frame win rate and binomial formula.  

We added a method generate_stats, which takes in historical matches and return the players statistics together with the match information. We will use it to generate dataset for modeling.  

We also tested different K-factors and chose K=8 as the K-factor for our elo rating system. The testing process is in [elo_v4_test.ipynb](/2_Elo_Rating_System/elo_v4/elo_v4_test.ipynb).

# Information about elo_v4
## Attributes
1. players: a numpy array of professional snooker players.
2. ratings: a pandas series of players elo_rating.
3. stats: a pandas dataframe with statistics of players such as elo_rating, winrate, etc.
4. stats_by_years: a pandas dataframes with statistics of players within three years and one year.

## Important methods
update_stats: After inputting historical matches (dataframe) and parameters (K-factor), this function updates all the above attributes.  
predict: input an array of pairs of players and best_of. Output the expected winner and expected match win rate and frame win rate.
generate_stats: input historical matches. Output these matches together with statistics of players at the momenet they attend the tournament.

## Elo update rule
Let R1 and R2 denote the elo-rating for player1 and player2. Then the expected winrate of player1 is $E1 = \frac{1}{1 + e^{(R2-R1)/400}}$.  
Suppose player1 and player2 play a match and the scores are score1 and score2. Then their actual frame win rate is $S1 = \frac{\text{score1}}{\text{score1}+\text{score2}}$ and $S2 = \frac{\text{score2}}{\text{score1}+\text{score2}}$.  
After this match, the elo-rating for player1 will be updated: 
$R1_{new} = R1 + K * (\text{score1}+\text{score2}) * (S1-E1)$,  
where K is the K-factor which we sets to 8, n denotes best_of. Notice that our update rule consider both match result and frame scores, but emphasize more on the former.
