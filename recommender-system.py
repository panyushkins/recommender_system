import sys
import helpers


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


def compare_films(dict_films, id_film1, id_film2, weight):
    similar_rating = float(0)

    for first_genre in dict_films[id_film1]['genres']:
        for second_genre in dict_films[id_film2]['genres']:
            if first_genre['id'] == second_genre['id']:
                similar_rating += weight['similar_genre']

    for first_country in dict_films[id_film1]['production_countries']:
        for second_country in dict_films[id_film2]['production_countries']:
            if first_country['iso_3166_1'] == second_country['iso_3166_1']:
                similar_rating += weight['similar_countries']

    for first_list in dict_films[id_film1]['results']:
        for second_list in dict_films[id_film2]['results']:
            if first_list['id'] == second_list['id']:
                similar_rating += weight['similar_lists']

    similar_rating *= dict_films[id_film2]['popularity']
    return {similar_rating: [dict_films[id_film2]['title']]}


def print_rates(rate_dict, print_items):
    printed_items = 0
    for rate_position in sorted(rate_dict, reverse=True):
        for film in rates[rate_position]:
            if printed_items < print_items:
                print(film)
                printed_items += 1


rating_weight = {'similar_genre': 2, 'similar_countries': 1, 'similar_lists': 5}

if __name__ == '__main__':
    rates = {}
    films = helpers.read_from_file(input('Input path to file: '))
    title = input('Input a film title: ')

    number_of_recommend_films = input('Input a number of recommend films: ')
    if number_of_recommend_films.isdigit():
        number_of_recommend_films = int(number_of_recommend_films)
    else:
        number_of_recommend_films = 10

    id_of_film = get_movie_id(title)

    for film_number in films:
        if film_number != id_of_film:
            rate = compare_films(films, id_of_film, film_number, rating_weight)
            for key_rate in rate:
                if key_rate not in rates:
                    rates.update(rate)
                else:
                    rates[key_rate].append(rate[key_rate][0])

    print()
    print_rates(rates, number_of_recommend_films)
