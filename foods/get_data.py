"""Fetch data from API."""
import requests

def api_response():
    """Fetch the data from API."""
    url = "https://yummly2.p.rapidapi.com/feeds/list"

    querystring = {"limit":"24","start":"0"}

    headers = {
        "X-RapidAPI-Key": "8c2fbd63b6msh0cb0f06d6eefb0bp195126jsn7230d0695123",
        "X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }
    # get json 
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return response['feed']

