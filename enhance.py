import requests
from requests.structures import CaseInsensitiveDict
import json

url = "https://na-trade.naeu.playblackdesert.com/Trademarket/GetMarketPriceInfo"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["User-Agent"] = "BlackDesert"


def getPrice(itemID, enhanceLevel):
    data = f"""
    {{
    "keyType": 0,
    "mainKey": {itemID},
    "subKey": {enhanceLevel}  
    }}
    """

    resp = requests.post(url, headers=headers, data=data)
    parsed_json = json.loads(resp.text)
    priceData = parsed_json['resultMsg']
    x = priceData.rfind("-")
    latestPrice = priceData[x + 1:len(priceData)]
    return(latestPrice)


print(getPrice(732313, 20))