import requests
import json
import random
import asyncio

SERPAPI_API_KEY= '5064c30da2bc516831bd8720a04960253f3d15c5241486fac85e289a6e76aef5'
OPENAI_API_KEY = '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'

# Set up the request headers with your API key
headers = {
    "Content-Type": "application/json"
}

# define a post request method
def post_data(url, payload):
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.json())
    return response.json()
    # print(type(res)) IS requests.models.Response
    # return res

# Set up the API endpoint URL and request parameters
baixingurl = "https://gpt.baixing.com"