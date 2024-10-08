import requests
from dotenv import load_dotenv
import os

# load env
load_dotenv()


class Token:

    def __init__(self):
        # get client_id and client_secret from environ
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')

        # prepare url to get access token
        self.url = (f'https://id.twitch.tv/oauth2/token?'
                    f'client_id={self.client_id}&client_secret={self.client_secret}&grant_type=client_credentials')



    def get_token(self):
        try:
            response = requests.post(url=self.url)
            response.raise_for_status()
            result = response.json()
        except requests.exceptions.HTTPError:
            print('Sorry there was a problem obtaining access token')
            return False
        else:
            return result

