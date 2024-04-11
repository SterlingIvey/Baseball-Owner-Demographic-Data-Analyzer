import pandas as pd

def get_team_recommendation(): 
    print("Welcome User! Which baseball team should you root for?")
    
    # Queetions and scoring logic
    questions = [{"question": "Are you a history buff? (Yes/No)", "weight": "history"}, 
                 {"question": "Are you passionate about other sports? (Yes/No)", "weight": "passionate"},
                 {"question": "Did you grow up playing baseball? (Yes/No)", "weight": "iq"},
                 {"question": "Do you want to be able to own a piece of your team? (Yes/No)", "weight": "public"}
                ]
    # Team data and weightings
    teams_data = {"Team":  "New York Mets": {"history": 2, "passionate": 1, "iq": 1}, 
                           "Atlanta Braves": {"history": 1, "passionate": 1, "iq": 2, "public": 1}, 
                           "Miami Marlins": {"history": 2, "passionate": 2, "iq": 2}, 
                           "Philadelphia Phillies": {"history": 1, "passionate": 1, "iq": 2}, 
                           "Washington Nationals": {"history": 2, "passionate": 2, "iq": 2}, 
                           "Chicago Cubs": {"history": 1, "passionate": 1, "iq": 1}, 
                           "Cincinnati Reds": {"history": 1, "passionate": 2, "iq": 2}, 
                           "Milwaukee Brewers": {"history": 1, "passionate": 2, "iq": 2},
                           "Pittsburgh Pirates": {"history": 1, "passionate": 1, "iq": 2}, 
                           "St Louis Cardinals": {"history": 1, "passionate": 1, "iq": 1}, 
                           "Arizona Diamondbacks": {"history": 2, "passionate": 2, "iq": 2},
                           "Colorado Rockies": {"history": 2, "passionate": 2, "iq": 2},
                           "San Diego Padres": {"history": 2, "passionate": 2, "iq": 2}, 
                           "San Francisco Giants": {"history": 1, "passionate": 1, "iq": 1}, 
                           "Baltimore Orioles": {"history": 1, "passionate": 1, "iq": 1},
                           "New York Yankees": {"history": 1, "passionate": 1, "iq": 1}, 
                           "Tampa Bay Rays": {"history": 2, "passionate": 2, "iq": 1}, 
                           "Boston Red Sox": {"history": 1, "passionate": 1, "iq": 1}, 
                           "Toronto Blue Jays": {"history": 2, "passionate": 2, "iq": 2, "public": 1},
                           "Chicago White Sox": {"history": 1, "passionate": 2, "iq": 2},
                           "Cleveland Guardians": {"history": 1, "passionate": 2, "iq": 2},
                           "Detroit Tigers": {"history": 1, "passionate": 2, "iq": 2},
                           "Kansas City Royals": {"history": 2, "passionate": 2, "iq": 2},
                           "Minnesota Twins": {"history": 1, "passionate": 2, "iq": 2}
                        }
                        
    # Convert to Data Frame for easier manipulation
    
    df_teams = pd.DataFrame.from_dict(teams_data, orient='index')
                        