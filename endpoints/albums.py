import requests



def get_album(album_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()


def get_album_tracks(album_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks?limit=50"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    tracks = response.json()["items"]
    track_names = [tracks[i]['name'] for i in range(len(tracks))]
    durations = [tracks[i]['duration_ms'] for i in range(len(tracks))]
    explicit = [tracks[i]['explicit'] for i in range(len(tracks))]
    track_ids = [tracks[i]['id'] for i in range(len(tracks))]

    return {"tracks":track_names, "durations":durations, "explicit":explicit, "track_ids":track_ids}

