The Situation:
You are a data analyst working for a gaming company. Your boss wants to start a new project for a new video game to release.
But he doesn’t know what kind of game to make. You might consider, what genre is popular right now, what streamers are playing
right now, what kind of video games make the most money, etc.

We have gathered 3 different sources of information:
- Twitch.tv API (https://dev.twitch.tv/)
- IGDB Webscrape (https://www.igdb.com/)
- Kaggle Dataset (https://www.kaggle.com/gregorut/videogamesales,  https://www.kaggle.com/alex333/video-games-with-reviews-and-playtime-statistics?select=GamesDataset.csv)

First, gather information from Twitch.tv API to get live data from the top games being player at the moment.

Explaining the files:
The config.py has user information needed to run the python files.
The methods.py containes a function to to a get request of the the top 20 games.
The run.py will output a json response of the top 20 games being played at the time of the function.
The convert.py to convert the json file into a csv.
The read_csv.py  will convert the csv and input into a table on postgres SQL.

Steps Needed to Retrieve:
1. Before doing anything, edit the "config.py" file and add your username and password for postgres SQL.
2. Run "python run.py"
3. Run "python convert.py"
4. Before running the last python file, go into pgAdmin and create a database called "twitch_api"
4. Run "python read_csv.py"
5. Done! You will now have data available to view the top 20 games playing on Twitch.tv.

Second, webscrape from IGDB which contains information on top games rated by critics and reviews.

Steps Taken:
1. Retrieve top 100 games from any platform from 1958 to 2020
2. When looking at the website, first thought to use was panda scraping
3. Opened jupyter notebook, connected to the URL
4. Retrieved the table using panda scraping
5. Modified the column headers with the appropriate column names and dropped the ones that weren’t needed
6. Ran into issue where column data contained unnecessary information and had to use the split function to create more columns
7. Went to pg admin and created a sql table
8. Went back to jupyter notebook and connected to sql
9. Loaded the data using pandas
10. Lastly confirmed the data by querying the table

Lastly, download csv files from Kaggle dataset to get information on videogame sales and playtime.

Steps Taken:
1. Create Jupytner notebook file
2. Create config python file with your password for PG Admin
3. Import decencies Pandas, from sqlalchemy import create_engine, from config import password, import numpy as np
4. Read in CSV files and create DataFrames
5. Drop duplicates from the vg_playtime DataFrame
6. Create new DataFrame by dropping unwanted columns.
7. Inner join both DataFrames on "Name" of video game.
8. Create DB in PG Admin and create table using column names from the joined DB
9. Connect to PGAdmin  database and test connection
10. Complete .to_sql to push data into the PG Admin DB
11. Query DB table to confirm data populated

The final data are 3 different sql database table. Although sql is a relational database, these 3 databases
are not connected to each other.
