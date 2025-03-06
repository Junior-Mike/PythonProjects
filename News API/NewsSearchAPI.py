import requests

API_KEY = 'd486fdb95a164cf09aa3cf676c235209'

URL = 'https://newsapi.org/v2/top-headlines'

# Dictionary with query parameters
params = {
    "country": "us",
    "category": "business",
    "apikey":  API_KEY
}

# Sends an HTTP GET request to the NewsAPI.
response = requests.get(URL, params=params) 

# Checking the response status
if response.status_code == 200:
    data = response.json() # Converts the API response to JSON format (dict)
    articles = data.get("articles", []) # Retrieves the list of articles from the JSON response

    # Checks if there are articles in the articles list.
    if articles:
        print("Last news:")
        for i, article in enumerate(articles[:5], 1): #It goes through the articles list (where the news is stored) and outputs the first 5 items.
            print(f"\n{i}. {article['title']}") 
            print(f"{article['description']}")
            print(f"{article['url']}")
    else:
        print('News is not found')
else:
    print(f"Error {response.status_code}: {response.text}")