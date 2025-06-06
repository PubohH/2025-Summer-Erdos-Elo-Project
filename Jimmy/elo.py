import numpy as np
import pandas as pd


def get_elo(matches, rating=None):
    """Established the elo_ratings and win rate.
        Args:
            matches : a pandas dataframe with matches 
            (with columns format: ['player1', 'player2', 'score1', 'score2', 'best_of']).
            rating: a panda dataframe with players name and their current rating.
                    If not specified, all players set to 400
        Returns:
            df: a dataframe indexed by player name 
            with columns ['elo_rating', 'matches_played', 'matches_won'].
    """ 
    if rating == None:
        

    return None

def initiate_elo(players, default_rating = 400):
    """Assign all players with default elo-rating.
        Args:
            players : a numpy array of players' names
        Returns:
            rating : a pandas data frame with player's default elo-rating. 
                    Default is 400.
        
    """ 
    rating = pd.DataFrame(columns = ['player', 'elo_rating'])
    rating['player'] = players
    rating['elo_rating'] = default_rating
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


