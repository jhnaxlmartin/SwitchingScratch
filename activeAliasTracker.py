import requests
import json

cleanindex_pattern = "accenturedotcom"

def getactive_index():

    url = "https://searchcleanindex2.accenture.com/amz/active/_alias"

    payload = {}
    # headers = {
    #     'Authorization': 'Basic ZGlyXGpvaG4uYXhsLnMubWFydGluOm1ZaWdOMXNMYWxhNw=='
    # }

    # response = requests.request("GET", url, headers=headers, data=payload)
    response = requests.post(url, auth=("dir\\" + login["eid"], login["password"]), json=payload)
    json_response = response.json()

    activeindices = json_response.keys()

    return activeindices

allActive = getactive_index()

# searching for the active index
currentIndex = next((s for s in allActive if cleanindex_pattern in s), None)




