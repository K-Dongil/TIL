import json

def max_revenue(movies):
    movieRevenue = []
    bestMovie = ''
    bestMovieRevenue = 0
    for i in movies:
        movie_id = i['id']
        budget_json = open('data/movies/{}.json'.format(movie_id), encoding='UTF8')
        budget_list = json.load(budget_json)
        movieRevenue.append((budget_list['revenue'], budget_list['title']))
    for i in range(len(movieRevenue)):
        if bestMovieRevenue < movieRevenue[i][0]:
            bestMovieRevenue = movieRevenue[i][0]
            bestMovie = movieRevenue[i][1]
    return bestMovie


    # 여기에 코드를 작성합니다.  
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))