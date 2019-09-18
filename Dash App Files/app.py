import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import pandas as pd
import sqlite3



conn = sqlite3.connect('twitdata2.db')
df = pd.read_sql('SELECT * from scoreData',conn)
df['datetime'] = pd.to_datetime(df['createdat'],format='%a %b %d %H:%M:%S +%f %Y',errors='coerce')
# df['datetime_1'] = df['datetime'].dt.strftime('%d/%m/%Y %H:%M:%S')
df = df.set_index('datetime')
df = df.drop('index', axis=1)
available_indicators = ['flyspicejet','airindiain','goairlinesindia','airasiaind','IndiGo6E']
available_freq = ['Daily Data', 'Real-Time']
df_tweet = df[['createdat','handle','tweet']]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='airlinechoice',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Airlines'
            ),
            
        ],
        style={'width': '48%', 'display': 'inline-block'}),

    #     html.Div([
    #         dcc.Dropdown(
    #             id='frequency-choice',
    #             options=[{'label': i, 'value': i} for i in available_freq],
    #             value='Frequency'
    #         ),
            
    #     ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ], style={'display': 'inline-block', 'width': '99%'}),

    dcc.Graph(id='sentiment-score'),
    dcc.Graph(id='day-avg'),
    dcc.Graph(id='day-count'),
    dash_table.DataTable(
            id='tweet-table',
            # columns=[{"Time": i, "Handle": i,"Tweet":i} for i in df_tweet.columns],
            data=df_tweet.to_dict('records'),
        )

])

@app.callback(
    Output('sentiment-score','figure'),
    [Input('airlinechoice','value')])
    # Input('frequency-choice','value')])
def update_graph(airlinechoice):
    df_E = df[df['ent']==airlinechoice]
    df_E.index = pd.to_datetime(df_E.index, format='%a %b %d %H:%M:%S +%f %Y').strftime('%d/%m/%Y %H:%M:%S')
    df_E['avg'] = df_E['sentiment_score'].rolling(window=25).mean()

    return {
        'data': [go.Scatter(
            x=df_E.index,
            y=df_E['avg'].values,
            
            # text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='lines',
            
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 40, 'b': 30, 't': 25, 'r': 0},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': 'Real-time Sentiment Scores (Last 25 tweets: Moving Avg)'
            }],
            'yaxis': {'type': 'linear'},
            'xaxis': {'showgrid': False,'showticklabels':False}
        }
    }
    

@app.callback(
    Output('day-avg','figure'),
    [Input('airlinechoice','value')])
    # Input('frequency-choice','value')])
def update_day(airlinechoice):
    df_R = df[df['ent']==airlinechoice]
    df_R = df_R.resample('D').mean()

    return {
        'data': [go.Bar(
            x=df_R.index,
            y=df_R['sentiment_score'].values,
            
            # text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            # mode='bar',
            
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 50},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': 'Daily Avg. Sentiment Scores'
            }],
            'yaxis': {'type': 'linear'},
            'xaxis': {'showgrid': False}
        }
    }
    

@app.callback(
    Output('day-count','figure'),
    [Input('airlinechoice','value')])
    # Input('frequency-choice','value')])
def update_day(airlinechoice):
    df_R = df[df['ent']==airlinechoice]
    # df_R = df_R.resample('D').mean()
    df_R = df_R.resample('1D').agg({"sentiment_score":'mean',"tweet":'size'})

    trace1 = go.Bar(
    x=df_R.index,
    y=df_R['sentiment_score'].values,
    yaxis = 'y1',
    name='Daily Avg. Sentiment Score')

    trace2 = go.Bar(
    x=df_R.index,
    y=df_R['tweet'].values,
    yaxis='y2',
    name='Daily Tweet Count')   

    return {
        'data': [trace1, trace2],
        'layout': {
            'barmode':'group',
            'height': 225,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 50},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': 'Daily Avg. Sentiment Scores'
            }],
            'yaxis': {'type': 'linear'},
            'yaxis2':{'side':'right'},
            'xaxis': {'showgrid': False}
        }
    }
    


if __name__ == '__main__':
	app.run_server(debug=True)