import urllib.request
import urllib.parse
import json
import helpers


def save_to_file(file_name, save_file):
    with open(file_name, 'w') as file:
        json.dump(save_file, file)


def download_films(token):
    films = dict()
    for i in range(1, 11):
        try:
            films[i] = helpers.make_tmdb_api_request(method='/movie/' + str(i), api_key=token)
            get_lists = helpers.make_tmdb_api_request(method='/movie/' + str(i) + '/lists', api_key=token)
            films[i].update(get_lists)

        except urllib.error.HTTPError as error:
            if error.code == 404:  # если 404 - пропускаем этот ID
                i += 1
    return films


if __name__ == '__main__':
    api_token = input('Input API key: ')
    filename = input('Input destination path to file: ')

    films_dict = download_films(api_token)
    print('Downloaded!')
    save_to_file(filename, films_dict)
    print('Data saved to ' + filename)
