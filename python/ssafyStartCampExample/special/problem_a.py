import json
from pprint import pprint


def movie_info(movie):
    movie_list = []
    for i in movie:
        if i == 'id' or i == 'title' or i == 'poster_path' or i == 'vote_average' or i == 'overview' or i == 'genre_ids':
            movie_list.append((i, movie[i]))
    return dict(movie_list)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('./data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))