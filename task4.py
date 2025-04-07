from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import numpy as np

app = Dash()


df = pd.read_csv('./data/daily_sales_data_pm.csv')
df = df[df.date>'2020-07-01']
df = df[df.date<'2021-07-01']

colours={
    'background': '#1C1C1C',
    'text':'#F5E8D8',
    'accent-1':'#FF6F61',
    'accent-2' : '#DAA520',
    'radio' : '#FF4500'
}

#To illustrate the point more clearly one could fileter the list so that the figure only showed a few months preceeding 
# the price change.

app.layout = html.Div(style={'backgroundColor': colours['background'],'width':'100%'},children=[
    html.H1(id="header",children='Sales of Pink Morsels over time',
            style={'color':colours['accent-2'],
                   'fontFamily':'Arial',
                   'marginLeft':'5%',
                   'paddingTop':'2%',
                   'marginBottom': '0'}),
    dcc.Graph(
        id='example-graph',
    ),
    dcc.RadioItems(['All','North','South','East','West'],value='All',id='radio',inline=True,
                   style={
                       'accent-color':colours['radio'],
                        'color':colours['text'],
                        'font-family' : 'Arial',
                        'max-width':'fit-content',
                        'margin-left':'auto',
                        'margin-right':'auto',
                        'paddingBottom':'15%'
                          })
    

])

@callback(
    Output('example-graph','figure'),
    Input('radio','value')
)
def update_graph(selected_region):
    if(selected_region=="North"):
        filtered_df = df[df.region=='north']
    elif(selected_region=="South"):
        filtered_df = df[df.region=='south']
    elif(selected_region=="East"):
        filtered_df = df[df.region=='east']
    elif(selected_region=="West"):
        filtered_df = df[df.region=='west']
    else:
        filtered_df = df

    fig = px.line(filtered_df,x='date',y='Sales',
              labels={
                  'date' : 'Date',
                  'Sales' : 'Sales ($)'
              })
    fig.update_layout(
        title=dict(text=f'The graph below displays the sales figures of the snack `Pink Morsel` over time across {selected_region} region(s)', font=dict(size=20), 
                   automargin=True,yref='paper'),
        plot_bgcolor=colours['background'],
        paper_bgcolor=colours['background'],
        font_color=colours['text'],
        font_family='Arial',
        title_font_family="Arial",
        title_font_color=colours['text'],
    )
    fig.data[0].line.color = colours['radio']
    return fig

if __name__ == '__main__':
    app.run(debug=True)