"""Fetch data from API."""
import requests

def api_response():
    """Fetch the data from API."""
    url = "https://yummly2.p.rapidapi.com/feeds/list"

    querystring = {"limit":"24","start":"0"}

    headers = {
	"X-RapidAPI-Key": "c30d446217mshbd21d002ec39140p13a905jsn5bdc6296359b",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }
    # get json 
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    # print(requests.request("GET", url, headers=headers, params=querystring).text)
    return response['feed']

