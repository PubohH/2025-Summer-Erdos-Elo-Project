import numpy as np
import pandas as pd
import random

def get_K(rating):
    return 12

def get_elo(matches, rating=None, K_factor = get_K):
    """Established the elo_ratings and win rate.
        Args:
            matches : a pandas dataframe with matches 
                    (with columns format: ['player1', 'player2', 'score1', 'score2', 'best_of', 'year']).                  
            rating: a pandas series with existing elo-rating of players.
                    If not specified, all players set to 1000
            K_factor: a function that inputs the rating and outputs the K factor.
        Returns:
            df: a pandas series of elo-rating indexed by players' names.
    """ 
    #if no current rating is specified, use the default rating 1000.
    if rating is None:
        players = get_players(matches)
        ratings = initiate_elo(players)

    else: 
        players = np.array(rating.index)
        ratings = rating
    
    #update elo rating for each matches
    for i in range(len(matches)):
        #Store the match information in the following variables
        match = matches.loc[i]
        player1 = match['player1']
        player2 = match['player2'] 
        score1 = match['score1']
        score2 = match['score2']
        best_of = match['best_of']

        #Store the current elo-ratings as R1 and R2
        R1 = ratings[player1]
        R2 = ratings[player2]
     
        #Expected probability of winning a frame by each player
        E1 = 1/(1+np.exp((R2-R1)/400))
        E2 = 1/(1+np.exp((R1-R1)/400))

        #K - adjustment factor based on a player’s reliabilit
        K1 = K_factor(R1)
        K2 = K_factor(R2)

        #S - actual frame win percentage
        S1 = score1/(score1+score2)
        S2 = score2/(score1+score2)

        #calculate and  the new ratings
        R1_new = R1 + K1 * (score1+score2) * (S1-E1)
        R2_new = R2 + K2 * (score1+score2) * (S2-E2)
        
        ratings[player1] = R1_new
        ratings[player2] = R2_new
    return ratings

def initiate_elo(players, default_rating = 1000):
    """Assign all players with default elo-rating.
        Args:
            players : a numpy array of players' names
        Returns:
            rating : a pandas series with player's default elo-rating indexed by player names. 
                    Default is 1000.
        
    """ 
    rating = pd.Series(index = players, 
                       data = np.zeros(len(players)))
    rating = rating + default_rating
   
    return rating

def get_players(matches):
    """Get the list of players from historical matches.
        Args:
            matches : a pandas dataframe with matches 
            (with columns format: ['player1', 'player2', 'score1', 'score2', 'best_of']).
        Returns:
            players: a numpy array of players' names.
    """ 
    players = np.array(pd.concat([matches['player1'], matches['player2']]).unique())
    players.sort()
    return players

def predict_prob(player1, player2, rating):
    """Predict the probability of player1 winning a frame.
        Args:
            player1 (String) : player1's name.
            player2 (String) : player2's name.
            rating (pandas series): a series with players' rating
        Returns:
            E1 (float) : the probability of player1 winning a frame against player2. 
    """
    R1 = rating[player1]
    R2 = rating[player2]
    E1 = 1/(1+np.exp((R2-R1)/400))
    return E1

def predict(player1, player2, rating, best_of):
    """Predict.
        Args:
            player1 (string) : player1's name.
            player2 (string) : player2's name.
            rating (pandas series): a series with players' rating
            best_of (int) : max total score
        Returns:
            score1 (int) : prediction of player1's score
            score2 (int) : prediction of player1's score
            winner (string) : name of the winner
    """ 
    R1 = rating[player1]
    R2 = rating[player2]

    E1 = 1/(1+np.exp((R2-R1)/400))
    E2 = 1/(1+np.exp((R1-R2)/400))

    if E1 > E2: 
        winner = player1
        score1 = int((best_of+1)/2)
        score2_est = score1*E2/E1
        score2 = np.round(score2_est).astype(int)

    elif E1<E2:
        winner = player2
        score2 = int((best_of+1)/2)
        score1_est = score2*E1/E2
        score1 = np.round(score1_est).astype(int)

    else:
        rng = random.randint(0, 1)
        if rng == 0:
            score1 = int((best_of+1)/2)
            score2 = int((best_of-1)/2)
            winner = player1
        else: 
            score1 = int((best_of-1)/2)
            score2 = int((best_of+1)/2)
            winner = player2
        
    print(f'Our prediction: winner is {winner}. Score is {score1}-{score2}.')
    return score1, score2, winner

    

