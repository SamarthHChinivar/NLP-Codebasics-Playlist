import spacy

nlp = spacy.load("en_core_web_sm")

#print(nlp.pipe_names)

doc = nlp("Captain america ate 100$ of samosa. Then he said I can do this all day.")

for token in doc:
    print(token," | ",token.pos_," | ",token.lemma_)