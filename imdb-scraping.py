import imdb
import json

# Create an instance of the IMDb class
ia = imdb.IMDb()

# Get the top 50 movies by rating
top250 = ia.get_top250_movies()

movies = []
for i in range(50):
    print("Hello")
    movie_id = top250[i].getID()
    movie = ia.get_movie(movie_id)
    title = movie.get('title')
    description = movie.get('plot outline')
    categories = [genre.strip() for genre in movie.get('genres', [])]
    image = movie.get('full-size cover url')
    actors = [actor['name'].strip() for actor in movie.get('cast', [])[:5]]
    rating = movie.get('rating')
    
    # Create the Movie object
    movie_data = {
        "movie_id": movie_id,
        "title": title,
        "description": description,
        "categories": categories,
        "image": image,
        "actors": actors,
        "current_recommended_rate": rating
    }
    movies.append(movie_data)
    with open("movie.json", "w") as f:
        json.dump(movies, f)

print(movies[0])
