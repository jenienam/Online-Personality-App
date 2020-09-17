# Dependencies
import numpy as np
from flask import Flask, request, render_template
import requests
from web_scraper import redditScraper, twitterScraper
from data_cleaning import calculateModelParameters
from model import personalityTypeResult

app = Flask(__name__)

@app.route('/')
def home():
    return (render_template('index.html'))

@app.route('/reddit',methods = ['POST', 'GET'])
def predict_reddit():
    if request.method == 'POST':
        username = request.form['reddit-username']

        comments = redditScraper(username)

        scores = calculateModelParameters(comments)

        personality = personalityTypeResult(comments)
        
        return (render_template('result.html', username=username, comments=comments, scores=scores, personality=personality))

@app.route('/twitter',methods = ['POST', 'GET'])
def predict_twitter():
    if request.method == 'POST':
        username = request.form['twitter-username']

        comments = twitterScraper(username)

        scores = calculateModelParameters(comments)

        personality = personalityTypeResult(comments)
        
        return (render_template('result.html', username=username, comments=comments, scores=scores, personality=personality))

@app.route('/data')
def data():
    return (render_template('data.html'))

@app.route('/about')
def about():
    return (render_template('about.html'))

if __name__ == "__main__":
    app.run(debug=True)