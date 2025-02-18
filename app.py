
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import boto3
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


# AWS Configuration
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

#Made some fixes to the S3 container

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load data from S3
def load_data_from_s3():
    obj = s3.get_object(Bucket='netflix-dashboard-2024', Key='netflix_titles.csv')
    return pd.read_csv(obj['Body'])

df = load_data_from_s3()

# Create visualizations
def create_content_by_type():
    type_counts = df['type'].value_counts()
    fig = px.pie(values=type_counts.values, names=type_counts.index, title='Content Distribution by Type')
    return fig

def create_content_by_year():
    yearly_content = df['release_year'].value_counts().sort_index()
    fig = px.line(x=yearly_content.index, y=yearly_content.values, 
                  title='Content Added by Year')
    return fig

def create_top_genres():
    genres = df['listed_in'].str.split(',', expand=True).stack()
    top_genres = genres.value_counts().head(10)
    fig = px.bar(x=top_genres.index, y=top_genres.values,
                 title='Top 10 Genres')
    return fig

# App layout
app.layout = dbc.Container([
    html.H1("Netflix Content Dashboard", className="text-center my-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=create_content_by_type()), md=6),
        dbc.Col(dcc.Graph(figure=create_content_by_year()), md=6)
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=create_top_genres()), md=12)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
    

