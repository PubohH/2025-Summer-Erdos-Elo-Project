# Data

This folder contains the datasets of historical matches of professional snookers from 1980 to 2025. The final dataset is matches.csv, which is obtained from combining Kaggle data from 1980 to 2020 and scraped data from 2020 to 2025

## Data Source
The first part of the data (1980-2020) is from Kaggle submitted by user rusiano. (Link: https://www.kaggle.com/datasets/rusiano/snooker-data-19822020). It is stored under folder 'Kaggle Data/Raw Data'. It contains the data of players, tournaments, scores and matches from 1980 to 2020. The data is scraped from [cuetracker.net](cuetracker.net), which is used by many parties including bookmakers and sport commentators.

The second part of the data (2020-2025) is directly scraped from cuetracker.net. Scraping scode is under the folder [Scrape](/1_Match_Data/Scraped%20Data/Scrape).

## Data Cleaning
For the Kaggle dataset, we drop the matches that are not needed for our use. In particular, we drop the walkover matches, those with score 0-0, and amateur and pro-am matches. We also sort the matches correctly by year and stages of the tournaments. Finally, we clean the 'name' feature by removing unnecessary numbers and country names from players' 'name'. Details can be found in [data_clearning](/1_Match_Data/Kaggle%20Data/data_cleaning.ipynb) and [data_cleaning2](/1_Match_Data/Kaggle%20Data/data_cleaning2.ipynb). 

For the scraped data, since matches dates are available for almost all matches, we sort the matches by tournament start time and dates. Details can be [found in data_clearning3](/1_Match_Data/Scraped%20Data/data_cleaning3.ipynb).

Finally, we combine two datasets and store it as [matches.csv](/1_Match_Data/matches.csv). We will use this dataset to generate player's statistics and final match data for analysis.

## Final dataset
The final dataset is [matches.csv](/1_Match_Data/matches.csv). It has 115,630 professional snooker matches. The matches are sorted in the order of tournament start date and, within a tournament, stages of the tournament. 

### Columns:  
1. player1: player1's name.  
2. player2: player2's name.  
3. score1: player1's score.  
4. score2: player2's score.  
5. tournament_id: the id of the tournament.  
6. date: date of the match as string.  
7. year: year of the corresponding tournament.  

Notice:   
1. 2/3 of matches don't have date information and they concentrate in early years. For those who have date information, they are in the correct order. 