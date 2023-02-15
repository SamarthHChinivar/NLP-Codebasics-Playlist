import spacy
from spacy.symbols import ORTH

nlp = spacy.blank("en")

nlp.tokenizer.add_special_case('gimme', [{ORTH:"gim"},{ORTH:"me"}])

doc = nlp("gimme double cheese extra large healthy pizza")

tokens = [token.text for token in doc]
print(tokens) 