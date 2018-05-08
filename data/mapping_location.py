import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import os
import json


path = "/home/alice/Developer/tweet-health-analytics/List-of-US-States-master/tweets_per_state/"
states=[]
tweets_per_state = []
for filename in os.listdir(path):
    try:
        with open(path+filename, "r", encoding='utf-8') as data:
            tweet_count = 0
            tweets = json.load(data)
            for item in tweets:
                tweet_count +=1
            print(filename,": ", tweet_count)
            states.append(filename.replace(".json",""))
            tweets_per_state.append(tweet_count)
    except:
        pass


data = [go.Bar(
            x=states,
            y=tweets_per_state,
            marker=dict(
                    color='rgb(158,202,225)',
            )
)]

layout = go.Layout(
    title="Number of sick per state",
    xaxis=dict(
        title="Persons"
    ),
    yaxis=dict(
        title="States"
    )
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='basic-bar.html')

