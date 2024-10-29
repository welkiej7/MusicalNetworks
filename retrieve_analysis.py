from utils import retrieve_all, generate_access, grab_bearer_token
import json 
import time 

generate_access()
token = grab_bearer_token()

with open("artists.json") as file:
  artists = json.load(file)
  artist_ids = artists["artist_ids"]
  artists = artists["artists"]
  


for index, artist in enumerate(artists):
  print(f'Artist: {artist}')
  response = retrieve_all(artist_ids[index], token=token)
  with open(f'Retrived_Artists/{artist}.json', 'w') as file:
    json.dump(response, file, indent= 2)
  file.close()
  generate_access()
  token = grab_bearer_token() # Refresh the Token
  time.sleep(30) # Wait for the API Limit

