from nltk.metrics.distance import edit_distance
import operator


def get_closest_word(list, word):
		distances = {w: dist for (w, dist) in map(lambda x: (x, edit_distance(word, x.split()[0])), list)}
		# There should be 'min' but WTF?!
		return max(distances)