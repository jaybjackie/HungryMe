"""Fetch data from API."""
import requests

def api_response():
    """Fetch the data from API."""
    url = "https://yummly2.p.rapidapi.com/feeds/list"

    querystring = {"limit":"24","start":"0"}

    headers = {
	"X-RapidAPI-Key": "ba05f816f4mshc4d14643084ca7bp11f8b3jsn8e14dd02719e",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }
    # get json 
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    # print(requests.request("GET", url, headers=headers, params=querystring).text)
    return response['feed']

