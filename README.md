# Import film watchlist into Plex

## Usage
0. Make sure you have Python installed.

1. Download the `main.py` file in the repository and install, in the same directory, [PlexAPI](https://github.com/pkkid/python-plexapi/) and tqdm.

    pip install plexapi tqdm

2. Edit `user` and `token` with your Plex user and your [Plex token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/).

3. Edit the url so that you have a working API that returns a list of movies that have `title` and `release_year` as parameters, among others. If they have them but with a different name, edit them.
If you edit `<your_user>` with your Letterboxd user, it will automatically provide a list taken from your Letterboxd watchlist.
4. Run the script:
    python main.py
## Known errors
### Search
The `account.searchDiscover` is not accurate, does not, often, perform searches correctly, and gives wrong or repeated results.
## Debug
Errors should be shown in the file "errors.txt".
The most common error is  `"Film name" is already on the watchlist`, in that case don't worry: it is simply saying that the movie you are trying to add to the list is already there.
