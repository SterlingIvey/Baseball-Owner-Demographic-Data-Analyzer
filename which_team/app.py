import pandas as pd

def get_team_recommendation(): 
    print("Welcome User! Which baseball team should you root for?")
    
    # Begin questions
    questions = [{"question": "Are you a history buff?"}, {"question": "Where do you live?"}, {"question": "Are you passionate about other sports?"}, {"question": "Big drinker?"}, {"question": "Did you grow up playing baseball?"}, 

teams_data = {"Team": ["New York Mets", "Atlanta Braves", "Miami Marlins", "Philadelphia Phillies", "Washington Nationals", "Chicago Cubs", "Cincinnati Reds", "Milwaukee Brewers", "Pittsburgh Pirates", "St Louis Cardinals", "Arizona Diamondbacks", "Colorado Rockies", "San Diego Padres", "San Francisco Giants", "Baltimore Orioles", "New York Yankees", "Tampa Bay Rays", "Boston Red Sox", 