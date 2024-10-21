import requests



def get_album(album_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/albums/{album_id}"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()


def get_album_tracks(album_id:str, bearer_token:str):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = {"Authorization":f"Bearer {bearer_token}"}
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    return response.json()





print(get_album_tracks("4aawyAB9vmqN3uQ7FjRGTy","BQBRVZjW-ReX2ZfBUbtwyXHGbgVI0t3VOVmka_qRr71BMY3st7Gd0UEmATVIoeIpvs1vAZKO-qmTf31CBdUQd8n1EPF7SkHfZCDxGKH1Gl_KllmAtpY"))