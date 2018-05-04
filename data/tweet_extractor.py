import json

file = '/home/alice/Developer/tweet-health-analytics/data/20180503/sample.json'
data = json.loads(file)

unique_data = { each['full_text'] : each for each in data }.values()