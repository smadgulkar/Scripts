import sqlite3
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

def sentiment_score(sentence):
	sid_obj = SentimentIntensityAnalyzer() 
	sentiment_dict = sid_obj.polarity_scores(sentence)
	return sentiment_dict['compound']

def find_ent(tweet):
	ent_list = ['flyspicejet','airindiain','goairlinesindia','airasiaind','IndiGo6E']
	for i in ent_list:
		if i in tweet:
			return i

# def make_score(): 
# 	conn = sqlite3.connect('twitdata2.db')
# 	df = pd.read_sql('SELECT * from tweets',conn)
# 	df['sentiment_score'] = df['tweet'].apply(sentiment_score)	
# 	df['ent'] = df['tweet'].apply(find_ent)
# 	df['datetime'] = pd.to_datetime(df["timestampms"], unit='ms')
# 	# df = df.resample('D', on='datetime').mean()
# 	# df2 = pd.DataFrame(index=df['datetime'],columns=['Airline','Score','Tweet'])
# 	df = df[['ent','sentiment_score','tweet']]
# 	return df

# print(make_score())


conn = sqlite3.connect('twitdata2.db')
c = conn.cursor()
df = pd.read_sql('SELECT * from tweets',conn)
df['sentiment_score'] = df['tweet'].apply(sentiment_score)	
df['ent'] = df['tweet'].apply(find_ent)
# df = df.resample('D', on='datetime').mean()
# df2 = pd.DataFrame(index=df['datetime'],columns=['Airline','Score','Tweet'])
# df = df[['timestampms','ent','sentiment_score','tweet']]
# c.execute("CREATE TABLE IF NOT EXISTS score_data (date_time TEXT,airline TEXT,score TEXT,tweet TEXT) ")
c.execute('DELETE FROM scoreData')
# c.execute('INSERT INTO score_data (createdat,tweet,user,handle,location,timestampms) VALUES (?,?,?,?,?,?)',(createdat,tweet,user,handle,location,timestamp))
df.to_sql('scoreData',con=conn,if_exists='append')
print('Commited scores to database')
# print(df.head(10))