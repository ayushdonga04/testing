import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL (Data Analyst jobs on Naukri)
url = "https://www.coingecko.com/en/api"


res = requests.get(url)

soup=BeautifulSoup(res.text,'html')

print(soup.prettify)
