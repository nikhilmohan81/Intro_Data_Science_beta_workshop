"""
This collaborative filter takes in any given user and any given unlistened song and makes predictions on how the given user would rate
that unlistened song.
"""
from pymongo import MongoClient

# Do MongDB setup
d = MongoClient("mongodb://zeus:hera@ds057128-a0.mongolab.com:57128/anesidora_datascience_workshop")
songs_collection = d['anesidora_datascience_workshop']['songs']
users_collection = d['anesidora_datascience_workshop']['users']
total_songs = songs_collection.count()
total_users =users.users_collection.count()

def get_user_average(total_user_ratings, total_songs):
	""" Get the average of all the ratings (or plays) for this user """
	user_average = float(total_user_ratings / total_songs)
	return user_average

def get_similarity(predict_user_rating, user_rating, song_id, max_plays_ever):
	"""
	Sim_score MUST be between 0 and 1. There are at least 2 different ways to calculate this:
	1) abs(subtract 2 ratings)/max_plays_ever
	2) Get fraction between 2 ratings, make sure never to divide by 0!
	"""
	sim_score = float((predict_user_rating - user_rating)/max_plays_ever)
	return sim_score

def get_max_plays_ever(users_collection):
	""" Get the maximum # of plays that any user has listened."""
	max_plays_ever = 0
	for  user in users_collection.find():
		if user['songs'][0]['plays'] > max_plays_ever:
			max_plays_ever = user['songs'][0]['plays']
	return max_plays_ever


def predict_user_tastes(user_id,sim_score,song, users_collection, songs_collection):
	""" The massive algorithm. Status: incomplete."""
	max_plays_ever = get_max_plays_ever(users_collection)
	for song_played in users_collection:
		pass
