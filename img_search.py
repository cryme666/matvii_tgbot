import os
from dotenv import load_dotenv
load_dotenv()
import requests

key = os.getenv('KEY')
cx = os.getenv('CX')


def get_photo_url(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": key,
        "cx": cx,
        "searchType": "image",
        "q": query,
        "num": 1,
        "safe": "active"
    }

    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            img_url = data['items'][0]['link']
            return img_url
        else:
            return None
    else:
        return None

def main():
    query = input("Enter a search term for GIFs: ")
    
    img_url = get_photo_url(query)
    print(img_url)

if __name__ == "__main__":
    main()