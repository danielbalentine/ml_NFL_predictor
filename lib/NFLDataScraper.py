'''

Written by Daniel Balentine, 10/13/2023
email: dbalentine@mgh.harvard.edu

This module was written to intake NFL data from a variety of sources.
To be used upstream from a machine learning model to predict various 
NFL bets and game lines

FantasyData APIs are used, you need to sign up for an API key on their
website to have access, they offer a free option where they give you last
years data if you want to get started.


'''
import pandas as pd
import requests
import pickle

class DataScrape:


    def __init__(self):
        pass
    
    def pullStadiumData(self):
        # URL for FantasyData Stadium API
        url = "https://api.sportsdata.io/api/nfl/odds/json/Stadiums" 
        headers = { 
        "Ocp-Apim-Subscription-Key":"266a56c32dfc490a95c3a4acbd5dffa6"
        }
        response = requests.get(url, headers=headers) 
        stadiums = response.json()
        
        #pulling in data
        df1 = pd.DataFrame(stadiums)

        #dropping unneeded data
        # I wonder if GeoLat/GeoLong could be used for weather data.
        df1.drop(columns=['City', 'State', 'Country', 'Capacity', 'GeoLat', 'GeoLong'], inplace=True)

        #applying numeric details for playing  surface and type
        df1['PlayingSurface'] = df1['PlayingSurface'].replace({'Artificial': 1, 'Dome': 2, 'Grass': 3})
        df1['Type'] = df1['Type'].replace({'Dome': 1, 'Outdoor': 2, 'RetractableDome': 3})

        #renaming one of the columns
        df1.rename(columns = {'Name':'Stadium'}, inplace = True)
        
        #save stadiums data as pickle file
        with open('data/stadium.pickle', 'wb') as f:
            pickle.dump(df1, f)
        df1.to_csv('data/stadium.csv')

    def pullGameData(self):
        teamstats = pd.DataFrame()
        for i in range(1,19):
            url10 = f"https://api.sportsdata.io/api/nfl/odds/json/TeamGameStats/2021REG/{i}"
            url11 = f"https://api.sportsdata.io/api/nfl/odds/json/TeamGameStats/2022REG/{i}"
            headers = { 
                        "Ocp-Apim-Subscription-Key":"266a56c32dfc490a95c3a4acbd5dffa6"
            }
            response10 = requests.get(url10, headers=headers) 
            response11 = requests.get(url11, headers=headers)    

            bettingdata10 = response10.json() 
            bettingdata11 = response11.json()

            e10 = pd.DataFrame(bettingdata10)
            e11 = pd.DataFrame(bettingdata11)

            teamstats = pd.concat([teamstats,e10,e11], ignore_index = True)

        #bringing in regular season 2020 data
        for i in range(1,18):
            url12 = f"https://api.sportsdata.io/api/nfl/odds/json/TeamGameStats/2020REG/{i}"

            headers = { 
                        "Ocp-Apim-Subscription-Key":"266a56c32dfc490a95c3a4acbd5dffa6"
            }

            response12 = requests.get(url12, headers=headers)     

            bettingdata12 = response12.json() 

            e12 = pd.DataFrame(bettingdata12)

            teamstats = pd.concat([teamstats,e12], ignore_index = True)
                
                
        #bringing in regular season 2020, 2021 and 2022 data postseason
        for i in range(1,5):
            url13 = f"https://api.sportsdata.io/api/nfl/odds/json/TeamGameStats/2021POST/{i}"
            url14 = f"https://api.sportsdata.io/api/nfl/odds/json/TeamGameStats/2022POST/{i}"
            url15 = f"https://api.sportsdata.io/api/nfl/odds/json/TeamGameStats/2020POST/{i}"

            headers = { 
                        "Ocp-Apim-Subscription-Key":"266a56c32dfc490a95c3a4acbd5dffa6"
            }

            response13 = requests.get(url13, headers=headers) 
            response14 = requests.get(url14, headers=headers) 
            response15 = requests.get(url15, headers=headers) 

            bettingdata13 = response13.json() 
            bettingdata14 = response14.json()
            bettingdata15 = response15.json()

            e13 = pd.DataFrame(bettingdata13)
            e14 = pd.DataFrame(bettingdata14)
            e15 = pd.DataFrame(bettingdata15)

            teamstats = pd.concat([teamstats,e13,e14, e15], ignore_index = True)
        
        #dropping rows with NA's (ie bills/bengals game)
        teamstats.dropna(subset=['OpponentScore', 'TotalScore'],inplace=True)

        #changing some of the stadium detail as names in the stadium section are current
        teamstats['Stadium'] = teamstats['Stadium'].replace({'Paul Brown Stadium':'Paycor Stadium','Mercedes-Benz Superdome':'Caesars Superdome','Heinz Field':'Acrisure Stadium','CenturyLink Field':'Lumen Field','Bills Stadium':'Highmark Stadium'})

        #changing the date time column to date format allowing to create time based columns
        teamstats['Date'] = pd.to_datetime(teamstats['Date'])

        #adding time features
        teamstats['month'] = teamstats['Date'].dt.month
        teamstats['year'] = teamstats['Date'].dt.year
        teamstats['dayofyear'] = teamstats['Date'].dt.dayofyear
        teamstats.to_csv('data/teamstats.csv')
        # Save teamstats as a pickle file
        with open('data/teamstats.pickle', 'wb') as f:
            pickle.dump(teamstats, f)
                    

    def pullFantasyData(self) -> pd.DataFrame:
        pass
    
    def pullPenaltiesData(self) -> pd.DataFrame:
        pass

    def pullFiveThiryEightData(self) -> pd.DataFrame:
        pass

    def pullGoogleTrendData(self) -> pd.DataFrame:
        pass