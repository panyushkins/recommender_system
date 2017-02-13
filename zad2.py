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

Films = dict()
print('Введите API key: ')
api_token = input()

print('Введите путь (название) файла: ')
filename = input()

i = 1
while len(Films) < 1000:
    try:
        Films[i] = make_tmdb_api_request(method='/movie/' + str(i), api_key=api_token)
        getlists = make_tmdb_api_request(method='/movie/' + str(i) + '/lists', api_key=api_token)
        Films[i].update(getlists)
        i += 1

    except urllib.error.HTTPError as e:
        if e.code == 404:  # если 404 - пропускаем этот ID
            i += 1

print('Все скачалось')
k = json.dumps(Films)

with open(filename, 'w') as file:
    file.write(k)
print('Данные сохранены в файл ' + filename)