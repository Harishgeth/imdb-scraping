import pymongo
import json
# Set the MongoDB connection parameters
host = 'localhost'
port = 27017
username = 'user'
password = 'pass'
database_name = 'movies'

# Create a MongoClient object
db = pymongo.MongoClient(f'mongodb://{username}:{password}@{host}:{port}/{database_name}?authMechanism=SCRAM-SHA-256')

# Access the 'movies' database


# Access the 'movies' collection
movies_collection = db['movies']

# Load the movie data from 'movie.json'
with open('movie.json', 'r') as f:
    movie_data = json.load(f)

# Insert the movie data into the 'movies' collection
movies_collection.insert_many(movie_data)
