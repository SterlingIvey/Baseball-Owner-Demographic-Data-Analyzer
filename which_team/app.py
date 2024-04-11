import pandas as pd

def get_team_recommendation(): 
    print("Welcome User! Which baseball team should you root for?")
    
    # Begin questions
    questions = [{"question": "Are you a history buff?"}, {"question": "Where do you live?"}, {"question": "Are you passionate about other sports?"}, {"question": "Big drinker?"}, {"question": "Did you grow up playing baseball?"}, {"question": "Do you want to be able to own a piece of your team?"}]
    # Team data and weightings
    teams_data = {"Team": ["New York Mets": {"history": 2}, "Atlanta Braves": {"history": 1}, "Miami Marlins": {"history": 2}, "Philadelphia Phillies": {"history": 1}, "Washington Nationals": {"history": 2}, "Chicago Cubs": {"history": 1}, "Cincinnati Reds": {"history": 1}, "Milwaukee Brewers": {"history": 1}, "Pittsburgh Pirates", "St Louis Cardinals", "Arizona Diamondbacks", "Colorado Rockies", "San Diego Padres", "San Francisco Giants", "Baltimore Orioles", "New York Yankees", "Tampa Bay Rays", "Boston Red Sox", 