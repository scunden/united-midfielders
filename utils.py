import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def player_data(filename, path):
    df = pd.read_csv('{}{}.csv'.format(path, filename))
    df = df.loc[(df['Standard Stats']!='Statistic')&(df['Standard Stats.1']!='Per 90')&(df['Standard Stats.2']!='Percentile')]
    df = df.dropna()
    df.columns = ['Statistic','Per 90','Percentile']
    df = df.drop_duplicates()
    df = df.set_index('Statistic')
    df['Percentile'] = df['Percentile'].astype(int)
    return df

def plot_radar(player_dict, categories, title):

  fig = go.Figure()

  for player in player_dict.keys():
    df_temp = player_dict[player]

    fig.add_trace(go.Scatterpolar(
          r=df_temp.loc[categories].Percentile.values,
          theta=categories,
          fill='toself',
          name=player,
          
    ))


  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,
        range=[0, 100]
      )),
    showlegend=True,
  )
  fig.update_layout(title_text=title, title_x=0.5)
  fig.update_layout(
    width=800,
    height=600,)
  fig.update_layout(polar = dict(radialaxis = dict(showticklabels = False)))
  fig.show()
  return fig
