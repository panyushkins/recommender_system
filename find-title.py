import json


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        read_json = json.loads(file.read())
    return read_json


def print_titles(films):
    for i in films:
        if films[i]['title'].find(word) >= 0:
            print(films[i]['title'])

if __name__ == '__main__':
    path = input('Input path to file: ')
    word = input('Input a word from film title: ')
    films_dict = read_from_file(path)
    print_titles(films_dict)