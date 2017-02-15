import helpers


if __name__ == '__main__':
    token = input('Input API key: ')
    film_id = int(input('Input film ID: '))
    budget = helpers.make_tmdb_api_request(method='/movie/'+str(film_id), api_key=token)['budget']
    print('The budget is: '+str(budget))
