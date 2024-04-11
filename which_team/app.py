import pandas as pd

def get_team_recommendation(): 
    print("Welcome User! Which baseball team should you root for?")
    
    # Queetions and scoring logic
    questions = [{"question": "Are you a history buff? (Yes/No)", "weight": {"Yes": 1, "No": 2}}, 
                 {"question": "Are you passionate about other sports? (Yes/No)", "weight": {"Yes": 1, "No": 2}},
                 {"question": "Big drinker? (Yes/No)", "weight": {"Yes": 1, "No": 2}},
                 {"question": "Did you grow up playing baseball? (Yes/No)", "weight": {"Yes": 1, "No": 2}},
                 {"question": "Do you want to be able to own a piece of your team? (Yes/No)", "weight": {"Yes": 1, "No": 2}}
                ]
    # Team data and weightings
    teams_data = {"Team":  "New York Mets": {"history": 2, "passionate": 1}, 
                           "Atlanta Braves": {"history": 1, "passionate": 1}, 
                           "Miami Marlins": {"history": 2, "passionate": 2}, 
                           "Philadelphia Phillies": {"history": 1, "passionate": 1}, 
                           "Washington Nationals": {"history": 2, "passionate": 2}, 
                           "Chicago Cubs": {"history": 1, "passionate": 1}, 
                           "Cincinnati Reds": {"history": 1, "passionate": 2}, 
                           "Milwaukee Brewers": {"history": 1, "passionate": 2},
                           "Pittsburgh Pirates": {"history": 1, "passionate": 1}, 
                           "St Louis Cardinals": {"history": 1, "passionate": 1}, 
                           "Arizona Diamondbacks": {"history": 2, "passionate": 2},
                           "Colorado Rockies": {"history": 2, "passionate": 2},
                           "San Diego Padres": {"history": 2, "passionate": 2}, 
                           "San Francisco Giants": {"history": 1, "passionate": 1}, 
                           "Baltimore Orioles": {"history": 1, "passionate": 1},
                           "New York Yankees": {"history": 1}, 
                           "Tampa Bay Rays": {"history": 2}, 
                           "Boston Red Sox": {"history": 1}, 
                           "New York Yankees": {"history": 1}, 
                           "Tampa Bay Rays": {"history": 2},
                           "Toronto Blue Jays": {"history": 2},
                           "Chicago White Sox": {"history": 1},
                           "Cleveland Guardians": {"history": 1},
                           "Detroit Tigers": {"history": 1},
                           "Kansas City Royals": {"history": 2},
                           "Minnesota Twins": {"history": 1}
                        }
                        