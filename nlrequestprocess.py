import nltk
from nltk.chunk import RegexpParser

testString = 'honda accord задняя стойка'

tagPatterns = [
   (r'(honda)$','VENDOR'),
   (r'([a-zA-Z0-9]+)$','MODEL'),
   (r'(от|для)$','PREP'),
   (r'([а-яА-Я]+)$','PART_NAME'),
]

tagger = nltk.RegexpTagger(tagPatterns)
taggedRequest = tagger.tag(nltk.word_tokenize(testString))

chunker = RegexpParser(r'''
    S: {<CAR> <PREP>? <PART_NAME>}
    CAR: {<VENDOR> <MODEL>}
    PART_NAME: {<PART_NAME>+}
''')

tree = chunker.parse(taggedRequest)
print(tree)