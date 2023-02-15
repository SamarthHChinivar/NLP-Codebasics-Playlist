import spacy

nlp = spacy.blank("en")

doc = nlp("Tony gave two $ to Peter")

for token in doc:
    print(token, "==> index: ", token.i,
          " is_aplpha: ", token.is_alpha,
          " is_puncht: ", token.is_punct,
          " like_num: ", token.like_num,
          " is_currency: ", token.is_currency)

#print(doc[1:5])
#print(type(nlp))
#print(dir(nlp))
#print(token.is_alpha)

#token2 = doc[2]
#print(token2)
#print(token2.like_num)

#token2 = doc[3]
#print(token2)
#print(token2.is_currency)