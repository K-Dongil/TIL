import json
from pprint import pprint

# 최대 재귀 깊이 에러 =>> 도대체 왜???
# def movie_info(movie, genres):
#     movie_list = []
#     movie_names = []
#     movie_id = movie['genre_ids']
#     for i in genres:
#         for j in range(len(movie_id)):
#             if i['id'] == movie_id[j]:
#                 movie_names.append(i['name'])
#     del movie['genre_ids']
#     movie['genres_names'] = movie_names
#     # print(movie)
#     for i in movie:
#         if i == 'id' or i == 'title' or i == 'poster_path' or i == 'vote_average' or i == 'overview' or i == 'genres_names':
#             movie_list.append((i, movie[i]))
#     return dict(movie_list)

# def movie_info(movies, genres):
#     moviesList = []
#     for i in movies:
#         moviesList.append(movie_info(i, genres))
#     return  moviesList

def movie_info(movies, genres):
    moviesList = []
    for movie in movies:
        movie_list = []
        movie_names = []
        movie_id = movie['genre_ids']
        for i in genres:
            for j in range(len(movie_id)):
                if i['id'] == movie_id[j]:
                    movie_names.append(i['name'])
        del movie['genre_ids']
        movie['genres_names'] = movie_names
        for i in movie:
            if i == 'id' or i == 'title' or i == 'poster_path' or i == 'vote_average' or i == 'overview' or i == 'genres_names':
                movie_list.append((i, movie[i]))
        moviesList.append(dict(movie_list))
    return  moviesList

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))