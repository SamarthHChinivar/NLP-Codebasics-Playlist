import spacy

nlp = spacy.blank("en")

with open("C:\\Users\\Samarth H Chinivar\\Desktop\\Engineering\\Internship\\RedTron-[Data-Science]\\NLP_Playlist-Week-1\\student.txt") as f:
    text = f.readlines()

text = ' '.join(text)
print(text)

doc = nlp(text)
emails = []

for token in doc:
    if(token.like_email):
        emails.append(token.text)

print(emails)