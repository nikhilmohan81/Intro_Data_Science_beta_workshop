# train_set = [({'contains_word_(organic)': True, 'contains_word_(fruity)': True, 'contains_word_(dark)': True, 'contains_word_(chocolate)': True, 'contains_word_(sweet)': True}, 'miss'),
#({'contains_word_(bitter)': True, 'contains_word_(spicy)': True, 'contains_word_(interesting)': True, 'contains_word_(dark)': True}, 'miss')]

# miss_words = {"contains_word_(organic)": 1, "contains_word(fruity)": 9, "miss": 10}
# match_words = {"contains_word_(organic)": 3, "contains_word(fruity)": 9, "match": 12}

class Susan_Classifier:
	def __init__(self):
		pass

	def create_dicts(self, train_set):
		# Hard-code the two dicts and init the total misses and total matches with 0.
		miss_words = {"miss":0}
		match_words = {"match":0}
		for sample_tuple in train_set:
			train_set_result = sample_tuple[-1]
			if train_set_result == "miss":
				results_dict = miss_words
			if train_set_result == "match":
				results_dict = match_words
			for description in sample_tuple:
				try:
					if dict(description):
						for k in description.iteritems():
							if k in results_dict:
								results_dict[k] += 1.0
							else:
								results_dict[k] = 1.0
				except:
					if description =="miss":
						results_dict["miss"] += 1.0
					if description == "match":
						results_dict["match"] += 1.0
		# print "miss_words:", miss_words
		# print "match_words:", match_words, "\n"
		return miss_words, match_words

	def predict_unknown_input(self, unknown_input, train_set):
		miss_words, match_words = self.create_dicts(train_set)
		prob_class_is = dict()
		for c in ["miss", "match"]:
				if c == "miss":
					prob_class_is[c] = float(miss_words["miss"])/ (float((miss_words["miss"] + match_words["match"])))
					for word in unknown_input:
		 				prob_class_is[c] = float(prob_class_is[c]) * (float(miss_words.get(word, 0.1))/miss_words["miss"])
	 			if c == "match":
	 				prob_class_is[c] = float(match_words["match"])/ (float((miss_words["miss"] + match_words["match"])))
	 				for word in unknown_input:
		 				prob_class_is[c] = float(prob_class_is[c]) * (float(match_words.get(word,0.1))/match_words["match"])
	 	print "miss P: ", prob_class_is["miss"], "match P: ", prob_class_is["match"]
 		if prob_class_is["miss"] > prob_class_is["match"]:
 			return "miss"
 		else:
 			return "match"

""""
unknown_input = "milky light sweet nutty"
for c in ["miss", "match"]:
	prob_class_is[c] = (misses/ (misses+matches))
			* (milky in misses / (total # of misses))
			* (light in misses/ (total # of misses))
			* (sweet in misses / total # of misses))
			* (nutty in misses)/ (total # of misses))

if prob_class_is["miss"] > prob_class_is["match"]: return "miss!"
"""