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
        json.dump(save_file, file)


def download_films(token):
    films = dict()
    for i in range(1, 1001):
        try:
            films[i] = make_tmdb_api_request(method='/movie/' + str(i), api_key=token)
            get_lists = make_tmdb_api_request(method='/movie/' + str(i) + '/lists', api_key=token)
            films[i].update(get_lists)

        except urllib.error.HTTPError as e:
            if e.code == 404:  # если 404 - пропускаем этот ID
                i += 1
    return films


if __name__ == '__main__':
    api_token = input('Input API key: ')
    filename = input('Input destination path to file: ')

    films_dict = download_films(api_token)
    print('Downloaded!')
    save_to_file(filename, films_dict)
    print('Data saved to ' + filename)