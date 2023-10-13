'''

Written by Daniel Balentine, 10/13/2023
email: dbalentine@mgh.harvard.edu

This module was written to intake NFL data from a variety of sources.
To be used upstream from a machine learning model to predict various 
NFL bets and game lines

'''
import pandas as pd
import requests

class DataScrape:


    def __init__(self):
        pass
    
    def pullStadiumData(self) -> pd.DataFrame:
        url = "https://api.sportsdata.io/api/nfl/odds/json/Stadiums" 
        headers = { 
        "Ocp-Apim-Subscription-Key":"266a56c32dfc490a95c3a4acbd5dffa6"
        }
        response = requests.get(url, headers=headers) 
        stadiums = response.json()
        print(stadiums)


    def pullFantasyData(self) -> pd.DataFrame:
        pass
    
    def pullPenaltiesData(self) -> pd.DataFrame:
        pass

    def pullFiveThiryEightData(self) -> pd.DataFrame:
        pass

    def pullGoogleTrendData(self) -> pd.DataFrame:
        pass