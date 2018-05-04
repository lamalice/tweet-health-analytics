import json

file = '/Users/alicelam/Kstate_Classes/CIS598/tweetf0rm/data/20180502/a4a2837cd4e241968c49496a8791dfce.json'

data = open(file, 'r')

json_decode=json.load(file)

def extractor():
    for item in json_decode:
        my_dict = {}
        my_dict['title'] = item.get('labels').get('en').get('value')
        my_dict['description'] = item.get('descriptions').get('en').get('value')
        my_dict['id'] = item.get('id')
        print(my_dict)

extractor()