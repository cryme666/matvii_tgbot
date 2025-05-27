import os
from dotenv import load_dotenv
load_dotenv()
import requests

giphy_api = os.getenv('GIPHY_API')

def get_gif_url(query, limit=1, rating='g'):
    url = 'https://api.giphy.com/v1/gifs/search'
    params = {
        'api_key': giphy_api,
        'q': query,
        'limit': limit,
        'rating': rating,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            gif_url = data['data'][0]['images']['original']['url']
            return gif_url
        else:
            return None
    else:
        return None

def main():
    query = input("Enter a search term for GIFs: ")
    
    gif_url = get_gif_url(query)
    print(gif_url)

if __name__ == "__main__":
    main()