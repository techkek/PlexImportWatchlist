import urllib, json

from plexapi.myplex import MyPlexAccount
account = MyPlexAccount('user', 'password')

open("errors.txt", "w")

# print(account.searchDiscover("Aftersun (2022)",libtype="movie"))

# plex = account.resource('ServerS').connect()

url = "https://letterboxd-list-radarr.onrender.com/<your_user>/watchlist/"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

name = [item['title'] for item in data]
year = [item['release_year'] for item in data]

for i in range(len(name)):
    result = account.searchDiscover(name[i]+" ("+year[i]+")",libtype="movie")[0]
    try:
        result.addToWatchlist()
    except Exception as e:
        with open("errors.txt", "a") as f:
            f.write(str(e) + "\n")