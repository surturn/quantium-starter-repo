from dash import Dash,html,dcc
import plotly.express as px
import pandas as pd
#Initializing the app
app=Dash(__name__)
#Load & Clean data(Workbench data)
files=[
    'quantium-starter-repo/data/daily_sales_data_0.csv',
    'quantium-starter-repo/data/daily_sales_data_1.csv',
    'quantium-starter-repo/data/daily_sales_data_2.csv'
]

try:
    #numeric_only=True,avoids messy data with strings
    all_dfs=[pd.read_csv(file) for file in files]
    #stacking them in one master dataframe,ignore_index=True resets the row numbers so they be sequential 0,1,2,3....
    df=pd.concat(all_dfs,ignore_index=True)
    df["price"]=df["price"].str.replace("$","").astype(float)
    df["sales"]=df["price"]*df["quantity"]#create sales column
    #sum sales for each product
    grouped_df=df.groupby("product",as_index=False)["sales"].sum()

#fallback dummy data
except FileNotFoundError:
    print("No data file found yet,using dummy data")
    df=pd.DataFrame({"Category":["A","B","C"],"Value":[10,20,30]})

#Creating graph
fig=px.bar(
    grouped_df,
    x="product",
    y="sales",
    color="product",
    title="Total sales by Product"

)
#Defining the layout
app.layout=html.Div(children=[
    html.H1(children="Quantum Data Dashboard"),
    html.Hr(),#A visual divider
    dcc.Graph(
        id="main-graph",
        figure=fig
    
    )

])
#Run
if __name__=="__main__":
    app.run(debug=True)
