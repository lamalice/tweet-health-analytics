import json
import os
import csv
import re
path = "/home/alice/Developer/tweet-health-analytics/data/20180503/extracted_tweets/"

def all_positive_tweets():
    positive = []
    positive_no_location = []
    for filename in os.listdir(path):
        full_path = path + filename
        with open(full_path,
                  encoding='utf-8') as data:
            tweets = json.load(data)

            for x in range(len(tweets)):
                if tweets[x]["classication"] == "positive":
                    if tweets[x]["location"]:
                        positive.append(tweets[x])
                    elif tweets[x]["location"] =="":
                        positive_no_location.append(tweets[x])
    return positive, positive_no_location


def group_by_state():
    path = "/home/alice/Developer/tweet-health-analytics/List-of-US-States-master/tweets_per_state/"
    positive_tweets, positive_no_location = all_positive_tweets()
    positive_location_invalid = []

    location_tweets = []
    with open('/home/alice/Developer/tweet-health-analytics/List-of-US-States-master/cleaned_states.json',encoding='utf-8') as data:
        states = json.load(data)

        for y in range(len(states)):
            with open(path + states[y]["state"]+'.json', "w")as out_state:
                for item in positive_tweets:
                    if states[y]["state"].lower() in item["location"].lower() or states[y]["abbreviation"].lower() in item["location"].lower()\
                            or item["location"] == "Los Angeles" or item["location"].lower().strip() == "texas":
                        popped_tweet = positive_tweets.pop(positive_tweets.index(item))
                        location_tweets.append(popped_tweet)
                        json.dump(popped_tweet,out_state)

        positive_location_invalid = positive_tweets





group_by_state()