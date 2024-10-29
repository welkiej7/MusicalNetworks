import os
import json 
import time
from tqdm import tqdm
from copy import deepcopy

from endpoints.tracks import get_audio_analysis, get_audio_features_track, get_multiple_tracks, get_track
from endpoints.artists import get_artist, get_artists_albums
from endpoints.albums import get_album, get_album_tracks
from authorization.generate_access import main


def generate_access():
    wd = os.getcwd()
    os.chdir('authorization')
    os.system('python generate_access.py')
    os.chdir(wd)

def grab_bearer_token():
    with open('authorization/bearer.json') as fd:
        token = json.load(fd)["access_token"]
    fd.close()
    return token


def get_all_songs_from_an_artist(artist_id:str, bearer_token:str):
    discography = {}
    albums = get_artists_albums(artist_id, bearer_token)
    print('--Retrieving the Albums--')
    for index,album in enumerate(albums['Album Ids']):
        songs = get_album_tracks(album, bearer_token)
        time.sleep(1)
        discography[albums['Album Names'][index]] =  songs
    return discography



def send_audio_features_to_analysis(discography_dict, token):
    response_dict = {}
    missing_count = 0
    for album in tqdm(discography_dict, ascii = "=#", desc = "Requesting Audio Analysis for Each Album"):
        track_ids = discography_dict[album]['track_ids']
        track_names = discography_dict[album]['tracks']
        features = []
        for index, id in enumerate(track_ids):
            try:
                time.sleep(5)
                tmp_features = get_audio_features_track(id, token)
                features.append(tmp_features)
            except:
                missing_count += 1
                continue
        response_dict[album] = [{i:j} for i,j in zip(track_names,features)]
    if missing_count != 0:
        print(f"Some Tracks are Lost: Total Lost Count for the Artist {missing_count}")
    return response_dict


def retrieve_all(artist_id, token):
    tmp_discography = get_all_songs_from_an_artist(artist_id, token)
    time.sleep(1)
    tmp_analysis = send_audio_features_to_analysis(tmp_discography, token)
    for i in tmp_discography:
        tmp_discography[i] = tmp_analysis[i]
    return tmp_discography
