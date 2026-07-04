# json lets us pretty-print the raw data if we ever want to inspect it
import json
# requests lets us make HTTP calls to a website/API
import requests
# sys gives us access to command-line arguments (sys.argv)
import sys

# sys.argv[0] is the script name, sys.argv[1] would be the search term
# so if the user didn't type exactly one extra argument, quit the program
if len(sys.argv) != 2:
    sys.exit()


# Call the iTunes Search API, searching for songs matching what the user typed
# sys.argv[1] is whatever the user typed after the script name, e.g. "python itunes.py adele"
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# Uncomment this line to see the full raw JSON response, nicely formatted
# print(json.dumps(response.json(), indent=2))

# Storing the json data inside a variable named o
# response.json() turns the API's JSON text into a Python dictionary
o = response.json()

# The dictionary has a "results" key holding a list of songs (each song is its own dictionary)
# so we loop through that list one song ("result") at a time
for result in o["results"]:
    # each result dictionary has a "trackName" key with the song's title
    print(result["trackName"])