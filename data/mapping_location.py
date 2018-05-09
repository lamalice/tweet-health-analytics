
import plotly.graph_objs as go
import plotly
import os
import json

path = "/home/alice/Developer/tweet-health-analytics/List-of-US-States-master/tweets_per_state/"
states=[]
tweets_per_state = []
state_data = []
for filename in os.listdir(path):
    try:
        with open(path+filename, "r", encoding='utf-8') as data:
            tweet_count = 0
            tweets = json.load(data)
            for item in tweets:
                tweet_count +=1
            # print(filename.replace(".json",""),",", tweet_count)
            states.append(filename.replace(".json",""))
            tweets_per_state.append(tweet_count)
            state_data.append(filename+": "+ tweet_count)
    except:
        pass

def bar_valid_location():
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
            title="States"
        ),
        yaxis=dict(
            title="Persons"
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='basic-bar.html')

def map_location_USmap():

    import pandas as pd

    df = pd.read_csv('/home/alice/Developer/tweet-health-analytics/data/20180503/states_tweets.csv')
    df.head()

    df["text"] = df["States"]+ " - Number reported sick: "+ (df["Tweets"]).astype(str) + ', Latitude: '+(df["Lat"]).astype(str)+ ', Longitude: '+(df["Lon"]).astype(str)
    limits = [(0, 20)]
    colors = ["rgb(255,65,54)","rgb(0,116,217)", "rgb(133,20,75)"]
    cities = []
    scale =.03

    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[lim[0]:lim[1]]
        city = dict(
            type='scattergeo',
            locationmode='USA-states',
            lon=df_sub['Lon'],
            lat=df_sub['Lat'],
            text=df_sub['text'],
            marker=dict(
                size=df["Tweets"]/scale,
                color=colors[i],
                line=dict(width=.5, color='rgb(40,40,40)'),
                sizemode='area'
            ),
            name="Size of label according to # of reported cases"
            )
        cities.append(city)

    layout = dict(
        title='May 2, 2018 Reported Sick <br>(Click legend to toggle traces)',
        showlegend=True,
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showland=True,
            landcolor='rgb(217, 217, 217)',
            subunitwidth=3,
            countrywidth=3,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )

    fig = dict(data=cities, layout=layout)
    plotly.offline.plot(fig, validate=False, filename='d3-bubble-map-populations.html')

map_location_USmap()