# You Are What You Type: Online Personality Analysis

Team Members

Melanie Follett

Jonathan Wu

Jenie Name

Jingchen Liu

# Project  Overview
People present themselves in many different ways online, but are they showing their true selves? Our application analyzes a user’s social media posts using a neural network model and determines their personality type based on the Myers-Briggs Type Indicator (MBTI) classification system.  By offering an interactive data-driven web application, we allow users to input their username for a variety of social media platforms in order to see how they are representing themselves online and if it is a reflection of their authentic selves.

# Part 1: Data Cleaning

The dataset for this project was collected from Kaggle (https://www.kaggle.com/datasnaek/mbti-type).  This dataset contained over 8600 rows of data.  Each row indicated a user's personality type and 50 posts that had made to an online forum.

The data was cleaned by a team member using Python/Pandas.  A variety of characteristics were calculated including word count, word variance, number of nouns used, etc.  A average sentiment score for eahc user's posts was also calculated using vaderSentiment.  All of these parameters were used in the model.

# Part 2: Model Building

A team member tested 4 different machine learning models to determine which was the most accurate in classifying personality types.  The models tested were Logistic Regression, Decision Tree & Random Forest, Support Vector Machine (SVM) and Neural Network.  The SVM and Neural Network models were the most accurate, and the team decided to use the Neural Network model.

# Part 3: Web Scraping

A team member developed two web scrapers using Python.  One web scraper collected comments from Reddit and the other scraped posts from Twitter.

# Part 4: Web Application Development (My Contribution)

Once the code for all the previous steps were completed, I compiled and organized the code into three different modules (web scraping, data cleaning, and modelling).  Using these, I built a Flask app that accepts a username (for either Reddit or Twitter), then runs through the three modules: web scraping to collect posts, data cleaning to obtain model parameters, and neural network model to determine personality classification. The Flask app then returns the predicted personality type based on the user’s posts. I also built a front-end interactive dashboard using HTML/CSS that accepts the user input and displays the result. Finally, I deployed the app to Heroku (https://online-personality.herokuapp.com/).
