import nltk
from nltk.chunk import RegexpParser

def parse_request(message):
	tagPatterns = [
	   (r'(honda)$','VENDOR'),
	   (r'([a-zA-Z0-9]+)$','MODEL'),
	   (r'(от|для)$','PREP'),
	   (r'([а-яА-Я]+)$','PART_NAME'),
	]

	tagger = nltk.RegexpTagger(tagPatterns)
	taggedRequest = tagger.tag(nltk.word_tokenize(message))

	chunker = RegexpParser(r'''
	    S: {<CAR> <PREP>? <PART_NAME>}
	    MODEL: {<MODEL>+}
	    VENDOR: {<VENDOR>}
	    CAR: {<VENDOR> <MODEL>}
	    PART_NAME: {<PART_NAME>+}
	''')

	tree = chunker.parse(taggedRequest)

	car = list(tree.subtrees(lambda t: t.label() == 'VENDOR'))
	parsed_request = {}

	# Hack with try except
	try:
		parsed_request['vendor'] = list(tree.subtrees(lambda t: t.label() == 'VENDOR'))[0].leaves()[0][0]
	except Exception:
		parsed_request['vendor'] = None
	try:
		parsed_request['model'] = ' '.join([leave[0] for leave in list(tree.subtrees(lambda t: t.label() == 'MODEL'))[0].leaves()])
	except Exception:
		parsed_request['model'] = None
	try:
		parsed_request['part_name'] = ' '.join([leave[0] for leave in list(tree.subtrees(lambda t: t.label() == 'PART_NAME'))[0].leaves()])
	except Exception:
		parsed_request['part_name'] = None

	return parsed_request