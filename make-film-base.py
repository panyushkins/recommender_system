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


def save_to_file(file_name, save_file):
    with open(file_name, 'w') as file:
        file.write(save_file)
    print('Data saved to ' + file_name)


def download_films(token):
    films = dict()
    i = 1
    while len(films) < 10:
        try:
            films[i] = make_tmdb_api_request(method='/movie/' + str(i), api_key=token)
            get_lists = make_tmdb_api_request(method='/movie/' + str(i) + '/lists', api_key=token)
            films[i].update(get_lists)
            i += 1

        except urllib.error.HTTPError as e:
            if e.code == 404:  # если 404 - пропускаем этот ID
                i += 1
    print('Downloaded!')
    return films


if __name__ == '__main__':
    api_token = input('Input API key: ')
    filename = input('Input destination path to file: ')

    Films_dict = download_films(api_token)
    serialized_films = json.dumps(Films_dict)
    save_to_file(filename, serialized_films)
