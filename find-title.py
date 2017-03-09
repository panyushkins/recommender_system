import helpers


def print_titles(films):
    for i in films:
        if films[i]['title'].find(keyword) >= 0:
            print(films[i]['title'])

if __name__ == '__main__':
    path = input('Input path to file: ')
    keyword = input('Input a word from film title: ')
    films_dict = helpers.read_from_file(path)
    print_titles(films_dict)
