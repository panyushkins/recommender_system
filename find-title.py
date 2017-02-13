import urllib.request
import urllib.parse
import json


def read_from_file(path):
    with open(path, 'r') as file:
        read_json = json.loads(file.read())
    return read_json

path = input('Input path to file: ')
word = input('Input a word from film title: ')

films_dict = read_from_file(path)


for i in films_dict:
    if films_dict[i]['title'].find(word) >= 0:
        print(films_dict[i]['title'])