import json
import sys


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        read_json = json.loads(file.read())
    return read_json


def get_movie_id(movie_title):
    film_id = None
    for film in films:
        if films[film]['title'] == movie_title:
            film_id = film
            break
    if not film_id:
        print('The film did not found, try again!')
        sys.exit(1)
    else:
        return film_id


def compare_films(dict_films, id_film1, id_film2):
    similar_rating = float(0)

    for first_genre in dict_films[id_film1]['genres']:
        for second_genre in dict_films[id_film2]['genres']:
            if first_genre['id'] == second_genre['id']:
                similar_rating += 2

    for first_country in dict_films[id_film1]['production_countries']:
        for second_country in dict_films[id_film2]['production_countries']:
            if first_country['iso_3166_1'] == second_country['iso_3166_1']:
                similar_rating += 1

    for t in dict_films[id_film1]['results']:
        for k in dict_films[id_film2]['results']:
            if t['id'] == k['id']:
                similar_rating += 5

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

    number_of_recommend_films = input('Input a number of recommend films: ')
    if number_of_recommend_films.isdigit():
        number_of_recommend_films = int(number_of_recommend_films)
    else:
        number_of_recommend_films = 10

    id_of_film = get_movie_id(title)

    for film_number in films:
        if film_number != id_of_film:
            rates.update(compare_films(films, id_of_film, film_number))  # fix updating with similar key

    print()
    print_rates(rates, number_of_recommend_films)
