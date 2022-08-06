# Library 

from urllib import response
from requests import get
from matplotlib import pyplot as plt
from datetime import datetime


API_KEY = "RHGBK83TRM4Q8Q99G3N9IJCVKFV9ZUMU9Y"
BSC_VALUE = 10 ** 18
# https://api.bscscan.com/api
#    ?module=account
#    &action=balance
#    &address=0x70F657164e5b75689b64B7fd1fA275F334f28e18
#    &apikey=YourApiKeyToken
BASE_URL = "https://api.bscscan.com/api"
    
def make_api_url(module,action,address, **kwargs):
    KwargsItems = kwargs.items()
    SingleAddres = f"?module={module}&action={action}&address={address}&apikey={API_KEY}"
    URL = BASE_URL + SingleAddres
        
    for key, value in kwargs.items():
        URL += f"&{key} = {value}"
        return URL
    
def get_account_balance(address):
    get_balance_url = make_api_url("account", "balance",address,tag="latest")
    response = get(get_balance_url)
    data = response.json()
    value = int(data["result"]) / BSC_VALUE
    return value

def get_transactions(address):
    transactions_url = make_api_url("account","balance", address,tag="latest")
    response = get(transactions_url)
    data = response.json()["result"]
    
    return data
    
    
address="0x70F657164e5b75689b64B7fd1fA275F334f28e18"
bsc = get_transactions(address)
    
if __name__ == "__main__":
    print(bsc)