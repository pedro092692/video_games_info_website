import requests
from api_token import Token
import os


class VideoGame:

    def __init__(self):
        self.base_url = 'https://api.igdb.com/v4'
        self.client_id = os.environ.get('CLIENT_ID')
        self.token = Token()
        self.token_established = False
        self.data = None

        # get token info
        self.get_access_token()

        # setup header
        self.headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.data["access_token"]}',
        }

    def make_query(self, endpoint, fields, query='',  limit=''):
        url = self.base_url + f'/{endpoint}'
        try:
            response = requests.post(url, headers=self.headers,
                                     data=f'fields {fields}; {query};' + (f'limit {limit};' if limit else ''))

            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('Sorry there was an error: ', e)
            return False
        else:
            return response.json()


    def get_game_info(self, game_id):
        result = self.make_query(endpoint='games', fields='name, '
                                                          'aggregated_rating, '
                                                          'cover.image_id,'
                                                          'screenshots.image_id,'
                                                          'genres.name,'
                                                          'involved_companies.company.name,'
                                                          'platforms.name,'
                                                          'summary,'
                                                          'language_supports.language.name',
                                 query=f'where id = {game_id}')


        return result


    def get_game_cover(self, game_id, img_size):
        game_cover_url =  self.make_query(endpoint='covers', fields='image_id', query=f'where game = {game_id}')
        url_info = game_cover_url[0]['image_id']
        url = f'https://images.igdb.com/igdb/image/upload/t_{img_size}/{url_info}.jpg'
        return url

    def search_game(self, query, limit=''):
        search_results = self.make_query(endpoint='games',
                                         fields='name, cover.image_id', query=f'search "{query}"', limit=limit)
        return search_results

    def popular_games(self, category = '2'):
        popular_games = self.make_query(endpoint='popularity_primitives', fields='game_id,'
                                                                                 'popularity_type,'
                                                                                 'value; sort value desc',
                                                                          query=f'where popularity_type = {category}',
                                                                          limit='7')

        games_id = [games['game_id'] for games in popular_games]
        games_info = [self.make_query(endpoint='games', fields='name,'
                                                               'cover.image_id',
                                                        query=f'where id = {game_id}') for game_id in games_id]

        return games_info


    def get_access_token(self):
        if not self.token_established:
            new_token = self.token.get_token()
            self.data = new_token
            self.token_established = True
        else:
            if self.token['expires_in']  == 0:
                new_token = self.token.get_token()
                self.data = new_token


