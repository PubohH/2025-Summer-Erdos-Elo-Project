import numpy as np
import pandas as pd
import random

class elo_rating:
    def __init__(self):
        self.players = None
        self.ratings = None
        self.stats = None
        self.stats_by_years = None


    # def get_K(self, rating, matches_played):
    #     if matches_played < 30:
    #         return 5
    #     else: 
    #         return 5
    

    def calculate_new_elo(R1, R2, score1, score2, K1, K2, best_of, ratio):
        """Calculate the new elo-rating after a match with given scores.
            Args:
                R1 (float) : player1's currrent elo-rating
                R2 (float) : player2's currrent elo-rating
                score1 (int) : player1's score
                score2 (int) : player2's score
                best_of (int) : max scores two playes can reach in total in this match
                get_K (function) : a function that inputs the elo-rating and output the K-factor
            Returns:
                R1_new (float) : player1's new elo-rating
                R2_new (float) : player2's new elo-rating
        """ 
        #Expected probability of winning a frame by each player

        E1 = 1 / (1 + np.exp((R2-R1)/400))
        E2 = 1-E1

        #S - actual frame win percentage
        S1 = score1/(score1+score2)
        S2 = score2/(score1+score2)

        #calculate and update the new ratings
        # R1_new = round(R1 + K1 * (score1+score2) * (S1-E1))
        # R2_new = round(R2 + K2 * (score1+score2) * (S2-E2))

        # extra_factor = best_of//5
        # R1_new = R1 + extra_factor * K1 * (1-E1)
        # R2_new = R2 + extra_factor * K2 * (0-E2)  

        #We consider both match result and scores when calculating the new elo
        
        extra_factor = best_of/2
        R1_new = R1 + 1 * extra_factor * K1 * (1-E1) + ratio * K1 * (score1+score2) * (S1-E1)
        R2_new = R2 + 1 * extra_factor * K2 * (0-E2) + ratio * K2 * (score1+score2) * (S2-E2)


            
        return R1_new, R2_new

    def initialize_elo(players, default_rating = 1000):
        """Assign all players with default elo-rating.
        Args:
            players : a numpy array of players' names
        Returns:
            rating : a pandas series with player's default elo-rating indexed by player names. 
                    Default is 1000.
        """
        rating = pd.Series(index = players, 
                                data = np.zeros(len(players)))
        ratings = rating + default_rating

        return ratings
            

        

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

    

    def update_stats(self, matches, K_factor = 6, ratio = 0.1):
        """Established the elo_ratings and win rate.
            Args:
                matches : a pandas dataframe with matches 
                        (with columns format: ['player1', 'player2', 'score1', 'score2', 
                        'best_of', 'tournament_id', 'date', 'year']).    
                        Notice that score1 is always greater than score2, so player1 is always the winner in the dataframe
                rating: a pandas series with existing elo-rating of players.
                        If not specified, all players set to 1000
                K_factor: a function that inputs the rating and outputs the K factor.
            Returns:
                df: a pandas dataframe indexed by players'name
                    with columns ['elo_rating', 'matches_played', 'matches_won', 'matches_win_rate',
                                    'frames_played', 'frame_won', 'frames_win_rate']
        """ 
        current_year = matches.year.max()

        

        #Step 1: update self.players and self.ratings
        #We assign the default rating 1000 to all the players.
        self.players = elo_rating.get_players(matches)
        self.ratings = elo_rating.initialize_elo(self.players)

        #Step 1.5 : initialize self.stats_by_years
        self.stats_by_years = pd.DataFrame(columns = ['matches_played_3_years', 'matches_won_3_years',
                                                      'matches_played_1_year', 'matches_won_1_year', 
                                                      'frames_played_3_years', 'frames_won_3_years',
                                                      'frames_played_1_year', 'frames_won_1_year'], index = self.players)
        self.stats_by_years.fillna(0, inplace = True)

        #Step 2: Create a dataframe df to store the stats of players. It will be a placeholder for self.stats.
        df = pd.DataFrame(columns = ['elo_rating', 'matches_played', 'matches_won', 'matches_win_rate',
                                    'frames_played', 'frames_won', 'frames_win_rate'], index = self.players)
        df['elo_rating'] = self.ratings
        df['matches_played'] = 0
        df['matches_won'] = 0
        df['matches_win_rate'] = 0.0
        df['frames_played'] = 0
        df['frames_won'] = 0
        df['frames_win_rate'] = 0.0


        #Step 3: Create dataframe stats_by_years. It will be a placeholder for stats_by_years
        stats_by_years = pd.DataFrame(columns = [], index = self.players)


        #update elo rating for each matches
        for ind in matches.index:
            #Step 4: Update df
            #Store the match information in the following variables (those except for date and tournament id)
            match = matches.loc[ind]
            player1 = match['player1']
            player2 = match['player2'] 
            score1 = match['score1']
            score2 = match['score2']
            best_of = match['best_of']
            year = match['year']
            
            #Store the value of matches_played for player1 and player2
            matches_played1 = df.loc[player1, 'matches_played']
            matches_played2 = df.loc[player2, 'matches_played']

            #Store the current elo-ratings as R1 and R2
            R1 = df.loc[player1, 'elo_rating']
            R2 = df.loc[player2, 'elo_rating']

            #K - adjustment factor based on a player’s reliabilit
            K1 = K_factor
            K2 = K_factor
        
            R1_new, R2_new = elo_rating.calculate_new_elo(R1, R2, score1, score2, K1, K2, best_of, ratio)

            df.loc[player1, 'elo_rating'] = R1_new
            df.loc[player2, 'elo_rating'] = R2_new

            #Update matches_played and matches_won
            df.loc[player1, 'matches_played'] += 1
            df.loc[player2, 'matches_played'] += 1
            df.loc[player1, 'matches_won'] += 1
             
            #Update frames_played and frames_won
            df.loc[player1, 'frames_played'] += score1 + score2
            df.loc[player2, 'frames_played'] += score1 + score2
            df.loc[player1, 'frames_won'] += score1
            df.loc[player2, 'frames_won'] += score2

            #Update self.stats_by_years
            if current_year - year<3:
                self.stats_by_years.loc[player1, 'matches_played_3_years'] += 1
                self.stats_by_years.loc[player2, 'matches_played_3_years'] += 1
                self.stats_by_years.loc[player1, 'matches_won_3_years'] += 1

                self.stats_by_years.loc[player1, 'frames_played_3_years'] += score1+score2
                self.stats_by_years.loc[player2, 'frames_played_3_years'] += score1+score2
                self.stats_by_years.loc[player1, 'frames_won_3_years'] += score1
                self.stats_by_years.loc[player2, 'frames_won_3_years'] += score2


            if current_year - year<1:
                self.stats_by_years.loc[player1, 'matches_played_1_year'] += 1
                self.stats_by_years.loc[player2, 'matches_played_1_year'] += 1
                self.stats_by_years.loc[player1, 'matches_won_1_year'] += 1

                self.stats_by_years.loc[player1, 'frames_played_1_year'] += score1+score2
                self.stats_by_years.loc[player2, 'frames_played_1_year'] += score1+score2
                self.stats_by_years.loc[player1, 'frames_won_1_year'] += score1
                self.stats_by_years.loc[player2, 'frames_won_1_year'] += score2


        #Cast the elo-rating to integers
        df['elo_rating'] = (np.rint(df['elo_rating'])).astype('Int64')

        #Update matches_win_rate
        df.loc[:, 'matches_win_rate'] = df.loc[:, 'matches_won']/(df.loc[:, 'matches_played'])

        #Update frames_win_rate
        df.loc[:, 'frames_win_rate'] = df.loc[:, 'frames_won']/(df.loc[:, 'frames_played'])

        #Update self.ratings
        self.ratings = df['elo_rating']

        #Store df in self.stats
        self.stats = df

        return self.stats
    
    
    def predict(self, df):
        """Predict multiple matches
            Args:
               df : pandas dataframe with columns ['player1', 'player2', 'best_of']
            Returns:
                prediction : a numpy array with 0/1 (or True/False) where 0 means player1 wins.
        """ 
        #Handle players with no match record
        df.reset_index(inplace = True)
        players = pd.concat([df['player1'], df['player2']], ignore_index=True)
        for player in players.values:
            if player not in self.players:
                self.players = np.append(self.players, player)
                self.ratings[player] = 1000
                self.stats.loc[player] = [1000, 0, 0, 0, 0, 0, 0]

        ratings1 = np.array(self.ratings[df['player1']])
        ratings2 = np.array(self.ratings[df['player2']])

        win_rates = 1 / (1 + np.exp((ratings2-ratings1)/400))
        prediction = np.array(win_rates<=0.5)


        return prediction , win_rates