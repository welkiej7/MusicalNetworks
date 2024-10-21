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


def get_audio_features_track(track_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()



def get_audio_analysis(track_id:str, bearer_token:str):

    url = f"https://api.spotify.com/v1/audio-analysis/{track_id}"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url = url, headers = headers)
    response.raise_for_status()

    return response.json()



get_audio_analysis("11dFghVXANMlKmJXsNCbNl","BQBRVZjW-ReX2ZfBUbtwyXHGbgVI0t3VOVmka_qRr71BMY3st7Gd0UEmATVIoeIpvs1vAZKO-qmTf31CBdUQd8n1EPF7SkHfZCDxGKH1Gl_KllmAtpY")
