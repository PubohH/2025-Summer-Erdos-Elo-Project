import numpy as np
import pandas as pd


def get_elo(matches, rating=None):
    """Established the elo_ratings and win rate.
        Args:
            matches : a pandas dataframe with matches 
            (with columns format: ['player1', 'player2', 'score1', 'score2', 'best_of', 'year']).
            rating: a panda dataframe with players name and their current rating.
                    If not specified, all players set to 1000
        Returns:
            df: a pandas series indexed by player name 
            with one column ['elo_rating']
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
        K1 = get_K(R1)
        K2 = get_K(R2)

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


def get_K(rating):
    if rating <= 2200:
        return 12
    elif rating >= 2700:
        return 3
    else: 
        return 12 - (rating-2200)/ (500/9)