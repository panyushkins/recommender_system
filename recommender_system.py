import json
import sys


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        read_json = json.loads(file.read())
    return read_json


def get_movie_id(movie_title):
    film_id = -1
    for i in films:
        if films[i]['title'] == movie_title:
            film_id = i
            break
    if film_id == -1:
        print('The film did not found, try again!')
        sys.exit(0)
    else:
        return film_id


def compare_films(dict_films, id_film1, id_film2):
    similar_rating = float(0)

    # count how many genres same with weight '2'
    for t in dict_films[id_film1]['genres']:
        for k in dict_films[id_film2]['genres']:
            if t['id'] == k['id']:
                similar_rating += 2

    # count how many production countries same with weight '1'
    for t in dict_films[id_film1]['production_countries']:
        for k in dict_films[id_film2]['production_countries']:
            if t['iso_3166_1'] == k['iso_3166_1']:
                similar_rating += 1

    # if 2 films in one list +5 to similar_rating
    for t in dict_films[id_film1]['results']:
        for k in dict_films[id_film2]['results']:
            if t['id'] == k['id']:
                similar_rating += 5

    # multiplication our rating to popularity
    # more popular - better
    similar_rating *= dict_films[id_film2]['popularity']
    return {similar_rating: dict_films[id_film2]['title']}


def print_rates(rate_dict, print_items):
    printed_items = 0
    for j in sorted(rate_dict, reverse=True):
        if printed_items < print_items:
            print(rates[j])
            printed_items += 1


if __name__ == '__main__':
    rates = {}
    films = read_from_file(input('Input path to file: '))
    title = input('Input a film title: ')

    try:
        number_of_recommend_films = int(input('Input a number of recommend films: '))
    except ValueError:
        print('Error with entered number. Will be shown 10 films')
        number_of_recommend_films = 10

    id_of_film = get_movie_id(title)

    for i in films:
        if i != id_of_film:
            rates.update(compare_films(films, id_of_film, i))

    print()
    print_rates(rates, number_of_recommend_films)
