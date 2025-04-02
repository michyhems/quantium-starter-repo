from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('./data/daily_sales_data_pm.csv')

#To illustrate the point more clearly one could fileter the list so that the figure only showed a few months preceeding 
# the price change.

fig = px.line(df,x='date',y='Sales',
              labels={
                  'date' : 'Date (YYYY-MM-DD)',
                  'Sales' : 'Sales ($)'
              })

app.layout = html.Div(children=[
    html.H1(children='Sales of Pink Morsels over time'),

    html.Div(children='''
        A graph displaying the changes in sales of the Pink Morsel snack over the period of time including before and after the price change.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)