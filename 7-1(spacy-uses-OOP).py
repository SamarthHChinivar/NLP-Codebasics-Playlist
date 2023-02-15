#Sentence tokenization using spacy
import spacy #spacy uses OOP
nlp = spacy.load("en_core_web_sm")

doc = nlp("Dr. Strange loves pav bhajji of mumbai. Hulk loves chaat of delhi")

#Sentence Tokenization
for sentence in doc.sents:
    print(sentence)

#Word Tokenization
for sentence in doc.sents:
    for word in sentence:
        print(word)