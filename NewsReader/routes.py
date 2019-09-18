from flask import render_template
import sqlite3
import feedparser
import newspaper
import re

def check_link():
    visited_Links = [] 
    conn = sqlite3.connect('newsData.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS visitedLinks (urls TEXT)')
    c.execute('SELECT * FROM visitedLinks')
    for row in c.fetchall():
        visited_Links.append(row[])
    return visited_Links

def analyze_link(url):
    ent = ["Dewan Housing","IndiGo","Spicejet","DHFL","Dewan","Equitas","Federal Bank",
            "SpiceJet","ICICI Bank","HDFC Bank","Shriram Transport"]
    posts = {}
    article = Article(link)
    article.download()
    article.parse()
    news = article.text
    for i in ent:
        p = re.compile(r'(?:^|\W)'+i+'(?:$|\W)')
        if p.search(news):
            print(i)
            print(article.title)



@app.route("/")
@app.route("/home")
def home():
	# posts = mongo.db.posts.find().sort([("Datestamp",pymongo.DESCENDING)])
    posts = mongo.db.posts.find()
    return render_template('home.html', posts=posts)
