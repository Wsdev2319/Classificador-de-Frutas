from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB 
from sklearn.pipeline import make_pipeline

palavras = ["maça", "banana", "uva", "cachorro", "gato", "carro"]

rotulos = [1, 1, 1, 0, 0, 0]

modelo = make_pipeline(CountVectorizer(), MultinomialNB())

modelo.fit(palavras, rotulos)

nova_palavra = ["banana"]

previsao = modelo.predict(nova_palavra)

print("Previsão:", "Fruta" if previsao[0] == 1 else "Não é uma fruta")