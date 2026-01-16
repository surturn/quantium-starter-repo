from dash import Dash,html,dcc,Input,Output,callback
import plotly.express as px
import pandas as pd


#Initialize the Dash app
app = Dash(__name__)

#Load and sort in the cleaned data

df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by='date')

app.layout = html.Div([
    html.H1("Sales of Pink Morsel Over Time",style={'textAlign':'center'}),
    html.Div([
        dcc.RadioItems(
            id='region-selector',
            options=['north','south','all','west'],
            value='all',
            inline=True
        )
    ],style={'textAlign':'center'}),
    dcc.Graph(id='sales-graph')


])

@callback(
    Output('sales-graph','figure'),
    Input('region-selector','value')
)

def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df=df[df['region']==selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f'Sales Over Time - {selected_region.capitalize()} Region')


    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

