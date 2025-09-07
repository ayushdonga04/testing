import requests

import pandas as pd

url= "https://api.coingecko.com/api"

res=requests.get(url)

html_content=res.text

df=pd.read_html(html_content)
