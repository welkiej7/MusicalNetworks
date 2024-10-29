import requests
import json
import time
import os 
import warnings

def get_client_info(path:str='client_info.json'):
    try:
        with open(path) as fd:
            temp_dict = json.load(fd)
            client_id = temp_dict['client_id']
            client_secret = temp_dict['client_secret']

        return client_id, client_secret
    except Exception as e:
        raise FileNotFoundError('Path is not correct to retrieve the client info.')


def request_access_token(client_id:str,client_secret:str,path_to_write:str = 'bearer.json'):
    url  = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    payload = {"grant_type":"client_credentials",
               "client_id":client_id,
               "client_secret":client_secret}
    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()
    response = response.json()
    response["expires_in"] = int(response["expires_in"]) + round(time.time()) - 1
    with open(path_to_write,'w') as fd:
        json.dump(response, fd)
    fd.close()

def check_validity(path_to_read:str = "bearer.json", client_path_to_read = 'client_info.json'):
    with open(path_to_read) as fd:
        bearer_info = json.load(fd)
        if int(bearer_info["expires_in"]) < (time.time() - 300):
            print('-- Requesting Authorization from SPOTIFY --')
            client_id, client_secret = get_client_info(client_path_to_read)
            request_access_token(client_id, client_secret, path_to_write= path_to_read)
            print("-- Retrieved Authorization --")
        else:
            print("-- Authorization is Already Valid --")


def main():
    print('--Checking .env--')
    env_variables = os.listdir()
    if 'client_info.json' not in env_variables:
        raise FileNotFoundError('There is no client info in the environment')
    if 'bearer.json' not in env_variables:
        warnings.warn('There is no previously produced bearer, generating the bearer token.')
        client_id, client_secret = get_client_info('client_info.json')
        request_access_token(client_id=client_id, client_secret=client_secret)
        print('--Successfully Wrote the Bearer in the .env')
    
    check_validity()
    
    print('Bearer token is ready in the environment!')

if __name__ == "__main__":
    main()