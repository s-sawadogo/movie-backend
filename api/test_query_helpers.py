from database import SessionLocal
from query_helpers import *

db = SessionLocal()

movie = get_movie(db, movie_id=1)
print(movie.title, movie.genres)
print("------------------"*4)

movies = get_movies(db, limit=5)
for film in movies:
    print(f"ID : {film.movieId}, Titre : {film.title}, Genres : {film.genres}")

print("------------------"*4)
rating = get_rating(db, movie_id=1, user_id=1)
print(f"User ID : {rating.userId}, Movie ID : {rating.movieId}, Rating : {rating.rating}, Timestamp : {rating.timestamp}")

print("------------------"*4)
ratings = get_ratings(db, min_rating=3.5, limit=1)
for film in ratings:
    print(f" ID : {film.movieId}, Note : {film.rating}")

print("------------------"*4)
tag = get_tag(db, user_id = 2,movie_id=60756, tag_text="funny")
print(tag)
print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}")

print("------------------"*4)
n_movies = get_movie_count(db)
print(f"Nombre total de films : {n_movies}")

print("------------------"*4)
n_ratings = get_rating_count(db)
print(f"Nombre total d'évaluations : {n_ratings}")

print("------------------"*4)
n_tags = get_tag_count(db)
print(f"Nombre total de tags : {n_tags}")

print("------------------"*4)
n_links = get_link_count(db)
print(f"Nombre total de liens : {n_links}")



db.close()