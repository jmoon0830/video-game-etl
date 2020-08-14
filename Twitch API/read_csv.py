import pandas as pd
import csv
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from config import postgres_name, postgres_password

#import csv to df
df = pd.read_csv("top_game_data_csv.csv")
#print(df)

#create connection to postgres/pgadmin after creating db twitch_api
engine = create_engine(f'postgresql://{postgres_name}:{postgres_password}@localhost/twitch_api')

#insert data into sql table
df.to_sql('top_games2',con=engine)

#if you want to drop the table
#engine.execute("DROP TABLE top_games")