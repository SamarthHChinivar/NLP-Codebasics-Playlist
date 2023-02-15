import spacy

nlp = spacy.load("fr_core_news_sm")

doc = nlp("Tesla Inc va racheter Twitter pour 45 milliards de dollars")

for ent in doc.ents:
    print(ent," | ",ent.label_," | ",spacy.explain(ent.label_))