import gensim
import pandas as pd

df = pd.read_json("C:\\Users\\Samarth H Chinivar\\Desktop\Engineering\\Internship\\RedTron-[Data-Science]\\Week-2\\reviews_Cell_Phones_and_Accessories_5.json",lines=True)

#print(df.head())
#print(df.shape)

#print(df.reviewText[0])
#print(gensim.utils.simple_preprocess('''They look good and stick good! I just don't like the rounded shape because I was always bumping it and Siri kept popping up and it was irritating. I just won't buy a product like this again'''))

review_text = df.reviewText.apply(gensim.utils.simple_preprocess)
#print(review_text)

model = gensim.models.Word2Vec (window = 10 , min_count = 2, workers = 4)

model.build_vocab(review_text,progress_per=1000)

model.train(review_text, total_examples=model.corpus_count, epochs=model.epochs)

#model.save("C:\\Users\\Samarth H Chinivar\\Desktop\Engineering\\Internship\\RedTron-[Data-Science]\\Week-2\\word2vec-amazon-cell-accessories-reviews-short.model")

#print(model.wv.most_similar("bad"))
print(model.wv.similarity(w1='phone',w2='great'))