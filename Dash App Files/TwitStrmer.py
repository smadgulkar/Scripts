from twython import TwythonStreamer
from twython import Twython
import json
import csv
import sqlite3

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        conn = sqlite3.connect('twitdata2.db')
        c = conn.cursor()
        if 'text' in data:
           createdat = data['created_at']
           tweet = data['text']
           user = data['user']['name']
           handle = data['user']['screen_name']
           location = data['user']['location']
           timestamp = data['timestamp_ms']
           c.execute("CREATE TABLE IF NOT EXISTS tweets (createdat TEXT,tweet TEXT,user TEXT,handle TEXT,location TEXT,timestampms NUMERIC) ")
           c.execute('INSERT INTO tweets (createdat,tweet,user,handle,location,timestampms) VALUES (?,?,?,?,?,?)',(createdat,tweet,user,handle,location,timestamp))
           print('Comitted to db: {}'.format(tweet)) 
        conn.commit()

    def on_error(self, status_code, data):
        print(status_code)


# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)
    
stream = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],creds['ACCESS_TOKEN'],creds['ACCESS_SECRET'])
stream.statuses.filter(track=['flyspicejet','airindiain','goairlinesindia','airasiaind','IndiGo6E'])