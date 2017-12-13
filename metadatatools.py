def filter_by_genre(d, genre):
    movies = []
    for movie in d.keys():
        if genre in d[movie]:
            movies.append(movie)    
    return movies