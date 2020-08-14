import methods
import json

#show top games (limit parameter for limiting how many top games)
limit = 20
top_game_url = methods.games_top(limit)
top_game_data = methods.get_requests_raw(top_game_url)
print(top_game_data)


with open('top_game_data.json', 'w') as json_file:
    json.dump(top_game_data, json_file)


#*********ADDITIONAL THINGS API CAN DO********

#show stream data based on streamer (user_id parameter for choosing which streamer)
    # user_id = "TFBlade"
    # query_url = methods.stream_info(user_id)
    # stream_data = methods.get_requests(query_url)
    #print(stream_data)

#show game analytics (doesn't work bc of authorization)
# game_id = 0
# game_analytics_url = methods.game_analytics(game_id)
# game_analytics_data = methods.get_requests(game_analytics_url)
#print(game_analytics_data)