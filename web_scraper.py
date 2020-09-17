import requests
import json
import GetOldTweets3 as got

# Scrape Reddit posts
def redditScraper(username):
    
    comments = []

    data = getPushshiftData(username)

    for comment in data:
        comments.append(comment['body'])
        #data = getPushshiftData(username)

    # obj = {}
    # obj['username'] = username
    # obj['comments'] = reddit_comments

    #print(reddit_comments)
    return(comments)

    # with open("comments.json", "w") as jsonFile:
    #     json.dump(obj, jsonFile)

def getPushshiftData(username):
    url = f"https://api.pushshift.io/reddit/search/comment/?author={username}&sort=desc&size=50"
    r = requests.get(url)
    data = json.loads(r.text)
    return(data['data'])

    #comments = getPushshiftData(username)
    #print(comments)

def twitterScraper(username):
    
    tweeter = username
    count = 50

    tweetCriteria = got.manager.TweetCriteria().setUsername(tweeter).setMaxTweets(count)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    comments = []

    for tweet in tweets:
        comments.append(tweet.text)

    #print(users_tweets)
    return(comments)

    # obj = {}
    # obj['author'] = tweeter
    # obj['comments'] = users_tweets

    # with open("tweeter_comments.json", "w") as jsonFile:
    # json.dump(obj, jsonFile)

#username = input("Input username:")
#twitterScraper(username)