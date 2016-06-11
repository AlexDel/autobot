import nltk
from nltk.chunk import RegexpParser

testString = 'задняя стойка от honda accord speed'

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
    MODEL: {<MODEL>+}
    VENDOR: {<VENDOR>}
    CAR: {<VENDOR> <MODEL>}
    PART_NAME: {<PART_NAME>+}
''')

tree = chunker.parse(taggedRequest)

car = list(tree.subtrees(lambda t: t.label() == 'VENDOR'))
print(car[0].leaves())