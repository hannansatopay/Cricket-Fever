import flask
import os
from flask import jsonify
import time
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from datetime import datetime

app = flask.Flask(__name__)
port = int(os.getenv("PORT", 9099))

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gs = gspread.authorize(creds)


def check_update_result():
    if time.time() > int(match_details[1][-1]):
            url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/match.php"
            querystring = {"seriesid":match_details[1][1],"matchid":match_details[1][0]}
            headers = {
                'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com",
                'x-rapidapi-key': "5tbeW0NGcNmshtlihbKNyagO5qA6p1Y6JBXjsnsJMXDoHCm19n"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            result = response.json()
            if (result['match']['currentMatchState'] == "COMPLETED"):
                winner_name = result['match']['matchSummaryText'].split("win")[0].strip()
                winner = "Team A" if winner_name == result['match']['homeTeam']['name'] else "Team B"
                sheet = gs.open('Cricket Fever')
                user_details = sheet.get_worksheet(0).get_all_values()
                df = pd.DataFrame(user_details)
                df.columns = df.iloc[0]
                df = df[1:]
                for index, row in df.iterrows(): 
                    if row["Bet"] != 0:
                        if row["Bet"] == winner:
                            sheet.get_worksheet(0).update_cell(index+1, 4, int(row["Coins"]) + 20)
                            sheet.get_worksheet(0).update_cell(index+1, 5, 0) 
                        else:
                            sheet.get_worksheet(0).update_cell(index+1, 5, 0)
                url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/matches.php"
                headers = {
                    'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com",
                    'x-rapidapi-key': "5tbeW0NGcNmshtlihbKNyagO5qA6p1Y6JBXjsnsJMXDoHCm19n"
                    }
                response = requests.request("GET", url, headers=headers)
                result = response.json()
                match = result['matchList']['matches'][-int(result['meta']['upcomingMatchCount'])]
                sheet.get_worksheet(2).update_cell(2, 1, str(match['id']))
                sheet.get_worksheet(2).update_cell(2, 2, str(match['series']['id']))
                sheet.get_worksheet(2).update_cell(2, 3, match['series']['shortName'])
                sheet.get_worksheet(2).update_cell(2, 4, match['venue']['name'])
                sheet.get_worksheet(2).update_cell(2, 5, match['homeTeam']['name'])
                sheet.get_worksheet(2).update_cell(2, 6, match['awayTeam']['name'])
                dt = datetime.strptime(match['startDateTime'],'%Y-%m-%dT%H:%M:%SZ')
                sheet.get_worksheet(2).update_cell(2, 7, str(dt.day) + dt.strftime("%B"))
                sheet.get_worksheet(2).update_cell(2, 8, str(dt.hour))
                sheet.get_worksheet(2).update_cell(2, 9, round(dt.timestamp()))
                dt = datetime.strptime(match['endDateTime'],'%Y-%m-%dT%H:%M:%SZ')
                sheet.get_worksheet(2).update_cell(2, 10, str(dt.day) + dt.strftime("%B"))
                sheet.get_worksheet(2).update_cell(2, 11, str(dt.hour))
                sheet.get_worksheet(2).update_cell(2, 12, round(dt.timestamp()))

scheduler = BackgroundScheduler()
scheduler.add_job(func=check_update_result, trigger="interval", minutes=5)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

@app.route('/')
def index():
        sheet = gs.open('Cricket Fever')
        user_details = sheet.get_worksheet(1).get_all_values()
        df = pd.DataFrame(user_details)
        df.columns = df.iloc[0]
        df = df[1:]
        table = df[['Name', 'Coins']].to_html().replace("dataframe", "w3-table-all w3-hoverable")
        return flask.render_template('index.html', table = table)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
