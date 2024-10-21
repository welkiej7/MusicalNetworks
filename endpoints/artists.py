import requests


def get_artist(artist_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()

def get_artists_albums(artist_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json

get_artist(bearer_token= "BQBRVZjW-ReX2ZfBUbtwyXHGbgVI0t3VOVmka_qRr71BMY3st7Gd0UEmATVIoeIpvs1vAZKO-qmTf31CBdUQd8n1EPF7SkHfZCDxGKH1Gl_KllmAtpY", artist_id="0TnOYISbd1XYRBk9myaseg")