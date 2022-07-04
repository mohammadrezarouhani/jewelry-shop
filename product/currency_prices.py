import requests
import json
from datetime import datetime
import pdb 

def get_currency_prices():
    header = {
        'Cookie': 'tgju-popup=true; analytics_campaign={%22source%22:%22direct%22%2C%22medium%22:null}; analytics_session_token=291d0f6d-88a5-e67d-c9fd-6e39abfa3507; analytics_token=1ab5284f-5b45-75f9-d32d-03e859573dbc; yektanet_session_last_activity=8/1/2021; _yngt_iframe=1; _yngt=b098836c-ce658-80380-06b94-4ffb62a39fd6b; _gcl_au=1.1.622868567.1627828992',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Connection': 'close',
        'cache':'false'
    }



    url='https://call5.tgju.org/ajax.json'
    data = requests.get(url,headers=header).text

    data = json.loads(data)
    prices = data.get('current')

    geram18 = prices.get('geram18', 'none')
    geram24 = prices.get('geram24', 'none')
    gold_740k = prices.get('gold_740k', 'none')

    dollor = prices.get('price_dollar_rl', 'none')
    gold_melted_transfer = prices.get('gold_melted_transfer', 'none')

    coin_emami = prices.get('sekee', 'none')
    coin_bahar_azadi = prices.get('sekeb', 'none')
    coin_half = prices.get('retail_nim', 'none')
    coin_quarter = prices.get('retail_rob', 'none')
    coin_gerami = prices.get('retail_gerami', 'none')

    currency = {
        'carat18': geram18['p'],
        'carat24': geram24['p'],
        'carat740': gold_740k['p'],
        'dollor': dollor['p'],
        'melted_gold_transfer': gold_melted_transfer['p'],
        'coin_emami': coin_emami['p'],
        'coin_bahar_azadi': coin_bahar_azadi['p'],
        'half_coin': coin_half['p'],
        'quarter_coin': coin_quarter['p'],
        'gerami_coin': coin_gerami['p']
    }
    
    return currency



if __name__=='__main__':
    data=get_currency_prices()
    pdb.set_trace()    