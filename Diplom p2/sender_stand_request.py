import requests
import configuration          
import data   

def post_new_order(body):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.post(url, json=body, timeout=10)

def get_track_order(track):
    url = configuration.URL_SERVICE + configuration.GET_TRACK
    return requests.get(url, params={"t": str(track)}, timeout=10)