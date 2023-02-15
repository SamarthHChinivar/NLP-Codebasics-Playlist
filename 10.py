import spacy
import nltk

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

words = ['eating','eats','eat','ate','adjustable','rafting','ability','meeting']

#for word in words:
    #print(word," | ",stemmer.stem(word))

nlp = spacy.load("en_core_web_sm")

ar = nlp.get_pipe('attribute_ruler')

ar.add([[{"TEXT":"Bro"}],[{"TEXT":"Brah"}]],{"LEMMA":"Brother"})

doc = nlp("Bro, you wanna go? Brah, don't say no! I am exhausted")

#print(nlp.pipe_names)

for token in doc:
    print(token," | ",token.lemma_," | ",token.lemma)