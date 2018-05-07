import json

file_name = '/home/alice/Developer/tweet-health-analytics/data/20180503/cleaned_tweets11.json'
output_name = '/home/alice/Developer/tweet-health-analytics/data/20180503/extracted_tweets11.json'
training_file = '/home/alice/Developer/tweet-health-analytics/data/20180503/training_data.json'

with open(file_name, 'r') as file:
    data = json.load(file)


def attribute_extractor():
    tweets = []

    for item in data:
        new_item = {}
        try:
            new_item.update({
                            # "date": item["retweeted_status"]["created_at"],
                            #  "username":item["user"]["screen_name"],
                            #  "full_text": item['full_text'],
                            #  "location":item["user"]["location"],
                            #  "hashtags":item['entities']['hashtags'],
                            #  "retweets_count":item["retweeted_status"]["retweet_count"],
                            #  "favorite_count":item["retweeted_status"]["favorite_count"],
                             # "url":item["entities"]["media"][0]['expanded_url']
                               "classification": ""
                             })
            tweets.append(json.dumps(new_item))
        except:
            pass

# PRINTS OUT TO A JSON FILE
    with open(output_name, 'w') as outfile:
        outfile.write('[')
        for item in tweets:
            outfile.write("%s,\n" % item)
        outfile.write(']')

attribute_extractor()