import spacy

nlp = spacy.load("en_core_web_sm")

transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve and he recived 500 bugs"

doc = nlp(transactions)

for token in doc:
    if(token.like_num and doc[token.i+1].is_currency):
        print(token,doc[token.i+1])