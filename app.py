from sklearn.tree import DecisionTreeClassifier
import numpy as np 

dados_frutas = np.array([[149, 1], [130, 1], [150, 0], [170, 0]])
rotulos_frutas = np.array([0, 0, 1, 1])

classificador_arvore = DecisionTreeClassifier()
classificador_arvore.fit(dados_frutas, rotulos_frutas)

fruta_nova = np.array([[145, 0]])

previsao = classificador_arvore.predict(fruta_nova)

mapeamento_classe = {0: 'Maçã', 1: 'Laranja'}

descricao_previsao = mapeamento_classe[previsao[0]]

print(f"A fruta com peso {fruta_nova[0][0]}q e textura {'suave' if fruta_nova[0][1] == 1 else 'áspera'} é provavelmente uma {descricao_previsao}.")

laranja_teste = np.array([[160, 0]])

previsao_laranja = classificador_arvore.predict(laranja_teste)

descriçao_previsao_laranja = mapeamento_classe[previsao_laranja[0]]

print(f"A fruta com peso {laranja_teste[0][0]}q e textura {'suave' if laranja_teste[0][1] == 1 else 'áspera'} é provavelmente uma {descriçao_previsao_laranja}.")