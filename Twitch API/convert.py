import json 
import csv 


# Opening JSON file and loading the data 
# into the variable data 
with open('top_game_data.json') as json_file: 
    data = json.load(json_file) 

game_data = data['data'] 

# now we will open a file for writing 
data_file = open('top_game_data_csv.csv', 'w') 

# create the csv writer object 
csv_writer = csv.writer(data_file) 

# Counter variable used for writing  
# headers to the CSV file 
count = 0

for game in game_data: 
    if count == 0: 

        # Writing headers of CSV file 
        header = game.keys() 
        csv_writer.writerow(header) 
        count += 1

    # Writing data of CSV file 
    csv_writer.writerow(game.values()) 

data_file.close() 