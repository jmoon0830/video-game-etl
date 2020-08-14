import requests
import json
import pprint
from config import client_id, authorization_token

#this is found in in new twitch api documentation
base_url = "https://api.twitch.tv/helix/"

#these params are for authorization to use the API
headers = {
        "Client-ID":client_id,
        "Authorization":f"Bearer {authorization_token}",
        "Accept":"application/vnd.v5+json"
    }
indent = 2

#function to do a requests using a url
def get_requests(query_url):
    response = requests.get(query_url,headers = headers).json()
    pretty_response = json.dumps(response, indent=indent)
    return(pretty_response)

def get_requests_raw(query_url):
    response = requests.get(query_url,headers = headers).json()
    return(response)

def games_top(limit):
    if limit > 0:
        query_url = base_url + 'games/top/?first=' + str(limit)
        return(query_url)
    if limit == 0:
        query_url = base_url + 'games/top/'
        return(query_url)

#*****ADDITIONAL METHODS FOR TWITCH API**********

#function for finding out url for stream info based on id
# def stream_info(login_id):
#     query_url = base_url+'streams?user_login='+login_id
#     return(query_url)
    
# def game_analytics(game_id):
#     if game_id > 0:
#         query_url = base_url + 'analytics/games/?game_id=' + str(game_id)
#         return (query_url)
#     if game_id == 0:
#         query_url = base_url + 'analytics/games/'
#         return (query_url)