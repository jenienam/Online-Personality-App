# You Are What You Type: Online Personality Analysis

Team Members:

Jenie Nam

Melanie Follett

Jonathan Wu

Jingchen Liu

# Project  Overview
People present themselves in many different ways online, but are they showing their true selves? Our application analyzes a user’s social media posts using a neural network model and determines their personality type based on the Myers-Briggs Type Indicator (MBTI) classification system.  By offering an interactive data-driven web application, we allow users to input their username for a variety of social media platforms in order to see how they are representing themselves online and if it is a reflection of their authentic selves.

# Part 1: Data Cleaning, Organization, and Visualization (My Contribution)

The dataset for this project was collected from Kaggle (https://www.kaggle.com/datasnaek/mbti-type).  This dataset contained over 8600 rows of data.  Each row indicated a user's personality type and 50 posts that had made to an online forum.

I cleaned the data using Python/Pandas and organized them using machine learning techniques.  A variety of characteristics were calculated including word count, word variance, number of nouns used, etc.  A average sentiment score for eahc user's posts was also calculated using vaderSentiment.  All of these parameters were used in the model.

# Part 2: Model Building

A team member tested 4 different machine learning models to determine which was the most accurate in classifying personality types.  The models tested were Logistic Regression, Decision Tree & Random Forest, Support Vector Machine (SVM) and Neural Network.  The SVM and Neural Network models were the most accurate, and the team decided to use the Neural Network model.

# Part 3: Web Scraping

A team member developed two web scrapers using Python.  One web scraper collected comments from Reddit and the other scraped posts from Twitter.

# Part 4: Web Application Development 

Once the code for all the previous steps were completed, a team member compiled and organized the code into three different modules (web scraping, data cleaning, and modelling) to build a Flask app that accepts a username from Reddit or Twiter as well as a neural network.   


# Part 5: Deploying the App 
The app was then deployed to Heroku (https://online-personality.herokuapp.com/).
