from nltk.metrics.distance import edit_distance
from statistics import mean
import operator


def get_closest_word(list, word):
		distances = {w: dist for (w, dist) in map(lambda x: (x, edit_distance(word, x.split()[0])), list)}
		# There should be 'min' but WTF?!
		return max(distances)

def calc_phrase_distance(phrase1, phrase2):
	tokens1 = phrase1.split()
	tokens2 = phrase2.split()

	tokens_distances = []
	for t1 in tokens1:
		tokens_distances.append(min(map(lambda token: edit_distance(t1, token), tokens2)))

	return sum(tokens_distances)/mean(map(len,[phrase1, phrase2]))

def get_closest_phrase(phrase, phrases_list):
	return True
