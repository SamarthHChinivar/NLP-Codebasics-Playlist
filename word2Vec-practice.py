import gensim
import pandas as pd

df = pd.read_json('C:\\Users\\Samarth H Chinivar\\Desktop\Engineering\\Internship\\RedTron-[Data-Science]\\Week-2\\reviews_Sports_and_Outdoors_5.json',lines=True)
review_text = df.reviewText.apply(gensim.utils.simple_preprocess)
#print(review_text)

model = gensim.models.Word2Vec(window=10, min_count=2, workers=4)
model.build_vocab(review_text,progress_per=1000)
model.train(review_text, total_examples=model.corpus_count,epochs=model.epochs)

text = input(str("Enter a string:"))
print(model.wv.most_similar(text))
print(model.wv.similarity(w1="good",w2="great"))
print(model.wv.similarity(w1="slow",w2="steady"))
model.save('C:\\Users\\Samarth H Chinivar\\Desktop\Engineering\\Internship\\RedTron-[Data-Science]\\Week-2\\reviews_sports_5.json')