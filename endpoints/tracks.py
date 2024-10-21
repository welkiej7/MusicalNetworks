import requests


def get_track(track_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()

def get_multiple_tracks(track_ids:list, bearer_token:str):
    
    if len(track_ids) > 50:
        raise ValueError('Track Id list can not be longer than 50')
    
    ids = ','.join(track_ids)
    url = f"https://api.spotify.com/v1/tracks?ids={ids}"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()






get_multiple_tracks(["7ouMYWpwJ422jRcDASZB7P","4VqPOruhp5EdPBeR92t6lQ"], bearer_token="BQDK2zNV6_mXAKnWzN16npgWA2B6aA8wmcswDrrFnkV2jbonN_g3A_OGLYJEL-EfknwkAaaQNLDtU9MFx7lMqmQ7WkgA25CDTjxSoeCEjzVQK5Oqblg")