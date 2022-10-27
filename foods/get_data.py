"""Fetch data from API."""
import requests

def api_response():
    """Fetch the data from API."""
    url = "https://yummly2.p.rapidapi.com/feeds/list"

    querystring = {"limit":"24","start":"0"}

    headers = {
        "X-RapidAPI-Key": "5a76c79e3fmsh1f6d490c33d0eabp1033fejsnf4b585450f20",
        "X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }
    # get json 
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return response['feed']

