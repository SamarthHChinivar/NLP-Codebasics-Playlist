import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Tesla Inc is going to accquire twitter for $45 billion")

for ent in doc.ents:
    print(ent," | ",ent.label_," | ",spacy.explain(ent.label_))
