import requests
from bs4 import BeautifulSoup
import pandas as pd



#This function return the matches information from one tournament with given url
def scrape_one_tourn(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #The following scrapes all matches using the keyword "match" since they are split into "match row odd" and "match row even"

    #Create a pandas dataframe with the following column names.
    matches_df = pd.DataFrame(
        columns = ['Player1', 'Player2', 'Score1','Score2','Best Of', 'Round Name', 'Match Date','Tournament Name'])

    #All matches are stroed under div, class name "match row even" or "match row odd".
    #In any case .find_all("div", class_ = "match") will find all class names containing the string "match"
    all_matches = soup.find_all("div", class_ = "match")

    #Get the tournament name.
    tournament_name = soup.find("h1", class_ = "text-center")
    #Get rid of all invisible characters
    #A small thing to note is that .find_all returns a list and doesn't have .text method, so we have to loop through it to use 
    #.text method
    tournament_name_str = [tournament_name.text.strip()]
    #Couter for writing row data into dataframe row-by-row.
    count = 0


    #.find_all returns a list, we are looping through this list
    for match in all_matches:
    #Initialize empty list, which is going to hold data from each match
        match_data = []

        #Players names are under this class name, I took a portion of the class name because it is common for both players.
        #You can F12 check the website to see specific names
        players_names = match.find_all("div", class_ = "matchResultText")

        for player_name in players_names:
            # Turn the string into a list, so .extend works properly, o.w. it extends character-by-character
            player = [player_name.text.strip()]
            match_data.extend(player)

        #Same thing here, the actual scores are under 'span'
        players_scores = match.find_all("span", class_ = "matchResultText")

        for scores in players_scores:
            score = [scores.text.strip()]
            score = int(score[0])
            match_data.append(score)
            
        #If the score is 0-0 (which means it's a walkover match), we will skip this match. 
        if match_data[2] == 0 and match_data[3] == 0:
            continue

        #The parentheses () is interpreted as negative sign in excel, so just get rid of "()"
        best_of = [match.find("span", class_ = "best_of").text.strip("()")]
        match_data.extend(best_of)

        #This for getting the stage, e.g., Final, Semi-Final, etc.
        round_name = [match.find("h5").text.strip()]
        match_data.extend(round_name)

        
        
        #Collect the date. 
        match_date = match.find("div", class_ = "col-12 played_on")
        if match_date is None:
            match_data.append(None)
        else:
            match_date_str = [match_date.text.strip()]
            match_data.extend(match_date_str)
        

        

        #Put the tournament name in the last column
        match_data.extend(tournament_name_str)
        #Write this data into one row in the dataframe
        matches_df.loc[count] = match_data
        count+=1

    #Add columns 'Tournament id' and 'Year'
    url_list = url.split('/')
    matches_df['Tournament id'] = url_list[-1]
    matches_df['Year'] = url_list[-2]

    #Reverse the order of the matches so that they are in the order of stages.
    old_index = matches_df.index.tolist()
    new_index = old_index[::-1]
    matches_df['new_index'] = new_index
    matches_df.set_index('new_index', inplace=True)
    matches_df = matches_df.rename_axis(None)
    matches_df = matches_df.sort_index()

    return matches_df