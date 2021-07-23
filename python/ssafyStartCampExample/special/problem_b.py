import json
from pprint import pprint


# def movie_info(movie):
#     movie_list = []
#     for i in movie:
#         if i == 'id' or i == 'title' or i == 'poster_path' or i == 'vote_average' or i == 'overview' or i == 'genre_ids':
#             movie_list.append((i, movie[i]))
#     return dict(movie_list)

def movie_info(movie, genres):
    movie_list = []
    movie_names = []
    movie_id = movie['genre_ids']
    for i in genres:
        for j in range(len(movie_id)):
            if i['id'] == movie_id[j]:
                movie_names.append(i['name'])
    del movie['genre_ids']
    movie['genres_names'] = movie_names
    # print(movie)
    for i in movie:
        if i == 'id' or i == 'title' or i == 'poster_path' or i == 'vote_average' or i == 'overview' or i == 'genres_names':
            movie_list.append((i, movie[i]))
    return dict(movie_list)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))