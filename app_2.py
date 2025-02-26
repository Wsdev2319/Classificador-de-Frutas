import tkinter as tk 
from tkinter import ttk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline 
import os 


def carregar_dados():
    
   palavras = []
   rotulos = []
   
   if os.path.exists('C:\\Users\\weses\\OneDrive\\Documentos\\teste.python\\aprednizado_de_maquina\\perguntas.txt'):
       
       with open('C:\\Users\weses\\OneDrive\\Documentos\\teste.python\\aprednizado_de_maquina\\perguntas.txt', 'r') as f:
            
            for linha in f:
                
                try:
                    
                    palavras, rotulos = linha.strip().split(',')
                    
                    palavras.append(palavras)
                    rotulos.append(int(rotulos))
                    
                except ValueError:
                    
                    print(f"Erro ao processar a linha: {linha.strip()}")
                    
                return palavras, rotulos

def salvar_dados(palavras, rotulos):
    
    with open('C:\\Users\\weses\\OneDrive\\Documentos\\teste.python\\aprednizado_de_maquina\\perguntas.txt', 'w') as f:
        
        for palavras, rotulos in zip(palavras, rotulos):
            
            f.write(f"{palavras},{rotulos}\n")

def treinar_modelo(palavra, rotulos):
    
    modelo = make_pipeline(CountVectorizer(), MultinomialNB())
    modelo.fit(palavras, rotulos)
    
    return modelo

palavras, rotulos = carregar_dados()

if palavras and rotulos:
    
    modelo = treinar_modelo(palavras, rotulos)
else:
    
    print("O conjunto de treinamento está vazio. Adicione algumas palavras o rótulos primeiro.")


def adicionar_palavra():
    
    global modelo 
    global palavras, rotulos
    
    nova_palavra = entrada_palavra.get()
    novo_rotulo = var_rotulo.get()
    
    if nova_palavra and (novo_rotulo == 0 or novo_rotulo == 1):
        
        if nova_palavra not in palavras:
            
            palavras.append(nova_palavra.lower())
            rotulos.append(novo_rotulo)
            
            salvar_dados(palavras, rotulos)
            
            modelo = treinar_modelo(palavras, rotulos)
            
            lbl_resultado['text'] = f"A palavra '{nova_palavra}' foi adicionada eo modelo foi atualizado."
            
        else:
            
            lbl_resultado['text'] = f"A palavra '{nova_palavra}' já está no conjunto de treinamento"
            
            
    
def verificar_palavra():
    
    global modelo
    global palavras, rotulos 
    
    palavras, rotulos = carregar_dados()
    modelo = treinar_modelo(palavras, rotulos) 
    
    consulta_palavra = entrada_palavra.get().lower()
    
    if consulta_palavra in palavras:
        
        previsao = modelo.predict([consulta_palavra])
        
        lbl_resultado['text'] = f"Previsão para '{consulta_palavra}': {'é uma Fruta' if previsao[0] == 1 else 'Não é uma fruta'}"
        
    else:
        
        lbl_resultado['text'] = f"Palavra '{consulta_palavra}' não encontrada."

# Criar janela Tkinter
janela = tk.Tk()
janela.geometry("900x300")
janela.title("Classificador de Frutas")

# Criar fontes 
fonte_titulo = ("Arial", 24)
fonte_texto = ("Arial", 16)

# Criar cores 
cor_fundo = "#f2f2f2" #Silver
cor_botao = "#4CAF50" #Green
cor_texto_botao = "#ffffff" #White 

janela.configure(bg=cor_fundo)

# Criar um rotulo para instruções
lbl_instrucao = tk.Label(janela,
                         text="Insira uma palavra:",
                         font=fonte_titulo, bg=cor_fundo)
lbl_instrucao.grid(row=0, column=0, padx=20, pady=20)

# Criar entrada palavra 
entrada_palavra = tk.Entry(janela, font=fonte_texto)
entrada_palavra.grid(row=0, column=1, padx=20, pady=20)

# Criar Botoes para ecolher rotulo de plavras

var_rotulo = tk.IntVar()
var_rotulo.set(0) 

# Primerio botao (RadioButton)
r1 = tk.Radiobutton(janela, 
                    text="Não e uma fruta",
                    variable=var_rotulo,
                    value=0,
                    font=fonte_texto,
                    bg=cor_fundo)
r1.grid(row=1, column=0, padx=20, pady=10)

r2 = tk.Radiobutton(janela, 
                    text="È uma fruta",
                    variable=var_rotulo,
                    value=1,
                    font=fonte_texto,
                    bg=cor_fundo)
r2.grid(row=1, column=1, padx=20, pady=10)

# Criar botao adicionar palavra
btn_adicionar = tk.Button(janela, 
                    text="Adicionar Palavra",
                    command=adicionar_palavra,
                    bg=cor_botao,
                    fg=cor_texto_botao,
                    font=fonte_texto)
btn_adicionar.grid(row=2, column=1, padx=20, pady=20)

# Criar botao verificar_palavra
btn_verificar = tk.Button(janela, 
                    text="Verificar Palavra",
                    command=verificar_palavra,
                    bg=cor_botao,
                    fg=cor_texto_botao,
                    font=fonte_texto)
btn_verificar.grid(row=2, column=1, padx=20, pady=20)

# Criar rotulo para exibir resultados
lbl_resultado = tk.Label(janela,
                         text="",
                         font=("Arial", 20),
                         bg=cor_fundo)
lbl_resultado.grid(row=3, columnspan=2, padx=20, pady=20)

janela.mainloop()