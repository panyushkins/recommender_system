import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)

print('Input API key: ')
api_token = input()  # 7af57f1d1d0dc0d0b5193a0a5317021c

print('Input film ID: ')
film_number = int(input())

print('The budget is: '+str(make_tmdb_api_request(method='/movie/'+str(film_number), api_key=api_token)['budget']))