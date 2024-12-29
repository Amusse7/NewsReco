import requests
import pandas as pd
from config import API_KEY, BASE_URL

def fetch_news(query="technology"):
    url = f"{BASE_URL}?q={query}&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return pd.DataFrame(articles)[['title', 'description', 'url']]
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return pd.DataFrame()
