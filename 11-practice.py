import spacy

nlp = spacy.load("en_core_web_sm")

with open('C:\\Users\\Samarth H Chinivar\\Desktop\\Engineering\\Internship\\RedTron-[Data-Science]\\NLP_Playlist-Week-1\\news_story.txt','r') as f:
    text = f.readlines()

text = ' '.join(text)
#print(text)

doc = nlp(text)

nouns = []
numbers = []

for token in doc:
    if(token.pos_ in ['NOUN']):
        nouns.append(token)
    elif(token.pos_ in ['NUM']):
        numbers.append(token)

print(nouns,"\n",numbers)

count = doc.count_by(spacy.attrs.POS)
#print(count)

for k,v in count.items():
    print(doc.vocab[k].text," | ",v)