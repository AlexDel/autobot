import nltk

testString = 'honda accord задняя стойка'

tagPatterns = [
   (r'(honda)$','VENDOR'),
   (r'([a-zA-Z0-9]+)$','MODEL')
]

tagger = nltk.RegexpTagger(tagPatterns)
print (tagger.tag(nltk.word_tokenize(testString)))