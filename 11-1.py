import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("He quit the job")

for token in doc:
    print(token," | ",token.pos_," | ",token.tag_," | ",spacy.explain(token.tag_))