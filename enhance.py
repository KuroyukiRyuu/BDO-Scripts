import requests
from requests.structures import CaseInsensitiveDict
import json

url = "https://na-trade.naeu.playblackdesert.com/Trademarket/GetMarketPriceInfo"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["User-Agent"] = "BlackDesert"

wep_bs = 16001
arm_bs = 16002
wep_conc = 16004
arm_conc = 16005
memes = 44195


def getPrice(itemID, enhanceLevel):
    """Returns the latest price of an item with the given itemID and enhanceLevel

    Args:
        itemID (int): ID of the item (can be found on BDOCodex)
        enhanceLevel (int): Enhance level of the item (0-20, 0 being the base item, 16-20 for PRI-PEN)
    """    
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
    return(int(latestPrice))


def calculateEnhanceCost(itemID, initialEnhance, finalEnhance):
    """Returns the cost of enhancing an item from initialEnhance to finalEnhance

    Args:
        itemID (int): ID of the item (can be found on BDOCodex)
        initialEnhance (int): Initial enhance level of the item (0-20, 0 being the base item, 16-20 for PRI-PEN)
        finalEnhance (int): Final enhance level of the item (0-20, 0 being the base item, 16-20 for PRI-PEN)
    """    
    price = getPrice(itemID, initialEnhance) # Price of item at the initialEnhance level
    return(price)

print(getPrice(732313, 20))





"""
If Armor or Weapon Then
    If R < 70% Then BR * (1 + (0.1 x FS)) Else
        If R >= 70% And R < 90% Then RT + (BR * (1 + (.02 * (FS - FST)))) Else
            If R >= 90% Then 90%

If Accessory Then
    If PRI Then
        If R < 70% Then BR * (1 + (0.1 x FS)) Else
            If R >= 70% And R < 90% Then RT + (BR * (1 + (.02 * (FS - FST)))) Else
                If R >= 90% Then 90%
    If DUO Then
        If R < 50% Then BR * (1 + (0.1 x FS)) Else
            If R >= 50% And R < 90% Then RT + (BR * (1 + (.02 * (FS - FST)))) Else
                If R >= 90% Then 90%
    If TRI Then
        If R < 40% Then BR * (1 + (0.1 x FS)) Else
            If R >= 40% And R < 90% Then RT + (BR * (1 + (.02 * (FS - FST)))) Else
                If R >= 90% Then 90%
    If TET Then
        If R < 30% Then BR * (1 + (0.1 x FS)) Else
            If R >= 30% And R < 90% Then RT + (BR * (1 + (.02 * (FS - FST)))) Else
                If R >= 90% Then 90%
R = Rate
BR = BaseRate
FS = Failstack
RT = Rate Surpassing Threshold
FST = Last Failstack Where Rate < Threshold
"""