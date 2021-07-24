import json


def dec_movies(movies):
    movieList = []
    for i in movies:
        movie_id = i['id']
        budget_json = open('data/movies/{}.json'.format(movie_id), encoding='UTF8')
        budget_list = json.load(budget_json)
        if budget_list['release_date'][5] == '1' and budget_list['release_date'][6] == '2':
            movieList.append(budget_list['title'])
    return movieList
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))