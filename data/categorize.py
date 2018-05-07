import json
import os
import csv

def all_positive_tweets():
    path = "/home/alice/Developer/tweet-health-analytics/data/20180503/extracted_tweets/"
    for filename in os.listdir(path):
        full_path = path +filename
        with open(full_path,
                  encoding='utf-8') as data:
            tweets = json.load(data)

            for x in range(len(tweets)):
                if tweets[x]["classication"] == "positive":

                    if tweets[x]["location"] is not "":
                        print(tweets[x])

# all_positive_tweets()

with open('/home/alice/Developer/tweet-health-analytics/List-of-US-States-master/states.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(' '.join(row))

