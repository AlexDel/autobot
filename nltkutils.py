from nltk.metrics.distance import edit_distance
import operator


def get_closest_word(list, word):
		distances = {w: dist for (w, dist) in map(lambda x: (x, edit_distance(word, x)), list)}
		# There should be 'min' but WTF?!
		print(min(distances, key=distances.get))
		return max(distances)