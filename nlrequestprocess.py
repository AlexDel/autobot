import nltk

testString = 'задняя стойка от honda accord '

tagPatterns = [
   (r'(honda)$','VENDOR'),
   (r'([a-zA-Z0-9]+)$','MODEL'),
   (r'(от|для)$','PREP'),
   (r'([а-яА-Я]+)$','PART_NAME'),
]

tagger = nltk.RegexpTagger(tagPatterns)
print (tagger.tag(nltk.word_tokenize(testString)))
