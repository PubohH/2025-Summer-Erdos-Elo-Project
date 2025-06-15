import numpy as np
import pandas as pd
import random

def get_K(rating, matches_played):
    if matches_played < 30:
        return 12
    elif rating<2000:
        return 3
    else: 
        return 3


def calculate_new_elo(R1, R2, score1, score2, K1, K2, best_of, r):
    """Calculate the new elo-rating after a match with given scores.
        Args:
            R1 (float) : player1's currrent elo-rating
            R2 (float) : player2's currrent elo-rating
            score1 (int) : player1's score
            score2 (int) : player2's score
            best_of (int) : max scores two playes can reach in total in this match
        Returns:
            R1_new (float) : player1's new elo-rating
            R2_new (float) : player2's new elo-rating
    """ 
    #Expected probability of winning a frame by each player
    E1 = 1 / (1 + np.exp((R2-R1)/400))
    E2 = 1 / (1 + np.exp((R1-R2)/400))

    #S - actual frame win percentage
    S1 = score1/(score1+score2)
    S2 = score2/(score1+score2)

    #calculate and update the new ratings
    # R1_new = round(R1 + K1 * (score1+score2) * (S1-E1))
    # R2_new = round(R2 + K2 * (score1+score2) * (S2-E2))

    # extra_factor = 1 + best_of//3
    # R1_new = round(R1 + extra_factor * K1 * (1-E1))
    # R2_new = round(R2 + extra_factor * K2 * (0-E2))
    
   
    extra_factor = best_of/2
    R1_new = R1 + 1 * extra_factor * K1 * (1-E1) + r * K1 * (score1+score2) * (S1-E1)
    R2_new = R2 + 1 * extra_factor * K2 * (0-E2) + r * K2 * (score1+score2) * (S2-E2)

    return R1_new, R2_new

def get_stats(matches, K_factor, r):
    """Established the elo_ratings and win rate.
        Args:
            matches : a pandas dataframe with matches 
                    (with columns format: ['player1', 'player2', 'score1', 'score2', 'best_of', 'year']).    
                    Notice that score1 is always greater than score2, so player1 is always the winner in the dataframe
            rating: a pandas series with existing elo-rating of players.
                    If not specified, all players set to 1000
            K_factor: a function that inputs the rating and outputs the K factor.
        Returns:
            df: a pandas dataframe indexed by players'name
                with columns ['elo_rating', 'matches_played', 'matches_won', 'win_rate']
    """ 
    #We assign the default rating 1000 to all the players.
    players = get_players(matches)
    ratings = initiate_elo(players)

    #Create a dataframe to stores the stats of players
    df = pd.DataFrame(columns = ['elo_rating', 'matches_played', 'matches_won', 'win_rate'], index = players)
    df['elo_rating'] = ratings
    df['matches_played'] = 0
    df['matches_won'] = 0
    df['win_rate'] = 0.0

    is_6743 = False
    after_6743 = False
    
    #update elo rating for each matches
    for i in range(len(matches)):
        #Store the match information in the following variables
        match = matches.loc[i]
        player1 = match['player1']
        player2 = match['player2'] 
        score1 = match['score1']
        score2 = match['score2']
        best_of = match['best_of']
        tournament_id = match['tournament_id']
        
        #Store the value of matches_played for player1 and player2
        matches_played1 = df.loc[player1, 'matches_played']
        matches_played2 = df.loc[player2, 'matches_played']

        #Store the current elo-ratings as R1 and R2
        R1 = df.loc[player1, 'elo_rating']
        R2 = df.loc[player2, 'elo_rating']

        #K - adjustment factor based on a player’s reliabilit
        K1 = K_factor
        K2 = K_factor
     
        R1_new, R2_new = calculate_new_elo(R1, R2, score1, score2, K1, K2, best_of, r)

        df.loc[player1, 'elo_rating'] = R1_new
        df.loc[player2, 'elo_rating'] = R2_new

        #Update matches_plaed and matches_won
        df.loc[player1, 'matches_played'] += 1
        df.loc[player2, 'matches_played'] += 1
        df.loc[player1, 'matches_won'] += 1


        #Zhao Xintong
        if (tournament_id == 6743) and not is_6743:
            is_6743=True
            print('Before 6743, Zhao Xintong\'s elo is:', df.loc['Zhao Xintong', 'elo_rating'])
        
        if (tournament_id != 6743) and is_6743:
            is_6743 = False
            print('After 6743, Zhao Xintong\'s elo is:',df.loc['Zhao Xintong', 'elo_rating'])

    #Cast the elo-rating to integers
    df['elo_rating'] = (np.rint(df['elo_rating'])).astype('Int64')

    return df

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


    