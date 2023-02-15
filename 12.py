import spacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")

#print(nlp.pipe_names)

doc = nlp("Tesla is going to accquire Twitter for $45 billion")

s1 = Span(doc,0,1,label="ORG")
s2 = Span(doc,5,6,label="ORG")

doc.set_ents([s1,s2],default="unmodified")

for ent in doc.ents:
    print(ent," | ",ent.label_) 