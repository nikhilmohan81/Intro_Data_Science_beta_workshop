"""
Expected document input to MongoDB:
one_collection = {"klass_name": "miss", "organic": 1, "light": 5}
Insert one_collection one at a time into MongoDB
"""
from pymongo import MongoClient

class Susan_Mongo:
	def __init__(self):
		# Do MongDB setup
		pass

	def insert_all_collections(self, known_data_points):
		# Do MongDB setup
		c = MongoClient()
		dbase_name = "naive"
		db = c[dbase_name]
		call = db["bayes_counts"]

		# Parse input  data and create a collection to insert into MongoDB.
		one_collection = dict()
		for sample_tuple in known_data_points:
			train_set_result = sample_tuple[1]
			sample_tuple = sample_tuple[0].split(" ")
			one_collection["klass_name"] = train_set_result
			for word in sample_tuple:
				if word not in one_collection:
					one_collection[word] = 1.0
				# Ignore any duplicate words in same review  ie: "sweet sweet" is counted as 1
				# else:
					# one_collection[word] += 1.0
			print one_collection
			call.save(one_collection)
			one_collection = dict()

	def predict_unknown_input(self, unknown_input):
		# Do MongDB setup
		c = MongoClient()
		dbase_name = "naive"
		db = c[dbase_name]
		call = db["bayes_counts"]

		unknown_input = unknown_input.split(" ")
		total_misses= call.find({"klass_name":"miss"}).count()
		total_matches =call.find({"klass_name":"match"}).count()
		# Get the P(miss) and P(match) overall
		P_miss = float(total_misses)/float(total_misses+total_matches)
		P_match = float(total_matches)/float(total_matches+total_matches)
		for unknown_word in unknown_input:
			total_unknown_words =  call.find({unknown_word:1.0}).count()
			# Avoid zeros by hard-coding zero to a small decimal value.
			if total_unknown_words == 0:
				total_unknown_words = 0.1
			# Get P(Miss) for the unknown word.
			P_miss= float(P_miss) *(float(total_unknown_words)/(float(total_misses)))
			# Get P(Match) for the unknown word.
			P_match= float(P_match) *(float(total_unknown_words)/(float(total_matches)))
		if P_miss>P_match:
			return "miss"
		else:
			return "match"

