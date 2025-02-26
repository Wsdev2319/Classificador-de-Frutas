# Classificador de Frutas

Este projeto consiste em um classificador simples de palavras que utiliza aprendizado de máquina para determinar se uma palavra está relacionada a uma fruta ou não. A aplicação utiliza a biblioteca `Tkinter` para a interface gráfica e `scikit-learn` para o modelo de aprendizado de máquina.

## Funcionalidades

- **Classificação de Palavras**: O modelo classifica se uma palavra corresponde a uma fruta (1) ou não (0).
- **Adicionar Novas Palavras**: Permite que o usuário adicione novas palavras com seus respectivos rótulos (fruta ou não fruta).
- **Treinamento Dinâmico**: O modelo é treinado e atualizado automaticamente sempre que uma nova palavra é adicionada.
- **Interface Gráfica**: A interface gráfica foi criada com a biblioteca `Tkinter`, permitindo uma interação simples para o usuário inserir palavras e obter previsões.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter as seguintes bibliotecas Python instaladas:

- `tkinter`: para a interface gráfica
- `scikit-learn`: para o modelo de aprendizado de máquina
- `os`: para manipulação de arquivos e diretórios

Você pode instalar as bibliotecas necessárias utilizando o `pip`:

```bash
pip install scikit-learn

Passo 1: Adicionar Palavras
Insira uma palavra na caixa de texto.
Selecione o rótulo da palavra:
"Não é uma fruta" (valor 0)
"É uma fruta" (valor 1)
Clique no botão Adicionar Palavra para adicionar a palavra e atualizar o modelo.

Passo 2: Verificar Palavras
Insira a palavra a ser verificada na caixa de texto.
Clique no botão Verificar Palavra para saber se a palavra foi classificada como fruta ou não.
Passo 3: Treinamento do Modelo
O modelo é automaticamente treinado sempre que uma nova palavra é adicionada à base de dados.
Estrutura do Código
O código está dividido em funções principais:

carregar_dados(): Carrega os dados de treinamento de um arquivo de texto.
salvar_dados(): Salva os dados de treinamento no arquivo.
treinar_modelo(): Treina o modelo de aprendizado de máquina usando CountVectorizer e MultinomialNB.
adicionar_palavra(): Função para adicionar uma nova palavra ao conjunto de dados e atualizar o modelo.
verificar_palavra(): Função para verificar se a palavra inserida é classificada como uma fruta ou não.
Arquivos de Dados
Os dados de treinamento são armazenados no arquivo perguntas.txt, localizado no caminho:

C:\\Users\\weses\\OneDrive\\Documentos\\teste.python\\aprednizado_de_maquina\\perguntas.txt

Formato do arquivo:

Cada linha contém uma palavra e seu respectivo rótulo (0 ou 1), separados por vírgula.
Exemplo:
perl
Copiar
Editar
banana,1
maçã,1
carro,0
Exemplo de Uso
Adicione a palavra "banana" com o rótulo "1" (fruta).
Adicione a palavra "carro" com o rótulo "0" (não é uma fruta).
Clique no botão Verificar Palavra e insira a palavra "banana". O sistema responderá com: "Previsão para 'banana': é uma Fruta".
Contribuições
Sinta-se à vontade para contribuir para o projeto! Você pode:

Corrigir bugs
Adicionar novas funcionalidades
Melhorar a interface gráfica
Para contribuir, faça um fork deste repositório, faça as alterações necessárias e crie um pull request.


