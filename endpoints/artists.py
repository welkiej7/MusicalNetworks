import requests


def get_artist(artist_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()

def get_artists_albums(artist_id:str, bearer_token:str):
    album_types = []
    total_tracks = []
    album_names = []
    album_ids = []
    release_dates = []
    release_date_precision = []
    artist = []

    nextt = "ls"
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?include_groups=album&limit=50"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    TOT  = 0
    while nextt != None:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        response = response.json()
        nextt = response['next']
        url = nextt
        album_types.extend([response["items"][i]["album_type"] for i in range(len(response["items"]))])
        total_tracks.extend([response["items"][i]["total_tracks"] for i in range(len(response["items"]))])
        album_names.extend([response["items"][i]["name"] for i in range(len(response["items"]))])
        album_ids.extend([response["items"][i]["id"] for i in range(len(response["items"]))])
        release_dates.extend([response["items"][i]["release_date"] for i in range(len(response["items"]))])
        release_date_precision.extend([response["items"][i]["release_date_precision"] for i in range(len(response["items"]))])
        artist.extend([[response["items"][i]["artists"][j]["name"] for j in range(len(response["items"][0]["artists"]))] for i in range(len(response["items"]))])
        TOT += 1
    some = {"Artists":[i[0] for i in artist],
            "Album Type":album_types,
            "Total Tracks":total_tracks,
            "Album Names":album_names,
            "Album Ids":album_ids,
            "Release Date":release_dates,
            "Release Date Precision":release_date_precision}



    return some




