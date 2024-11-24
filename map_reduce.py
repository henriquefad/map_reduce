from collections import defaultdict
import urllib.request
import re

# URL correta para acessar o conteúdo raw do arquivo no GitHub
url = "https://raw.githubusercontent.com/henriquefad/map_reduce/main/arquivo_mapreduce-1.txt"
conteudo = urllib.request.urlopen(url)
dados = conteudo.read().decode('utf-8')  # Decodificando para string UTF-8

# Função Map: separa cada palavra e associa o valor 1 para contagem
def map_func(dados):
    result = []
    # Limpando o texto, removendo qualquer coisa que não seja palavra ou espaço
    dados = re.sub(r'[^a-zA-Zá-úÁ-Ú\s]', '', dados)  # Remove caracteres não alfabéticos
    for palavra in dados.split():
        result.append((palavra.lower(), 1))  # Converte as palavras para minúsculas
    return result

# Função Reduce: soma o valor de cada palavra para contar as ocorrências
def reduce_func(mapped_data):
    resultado = defaultdict(int)
    for palavra, contagem in mapped_data:
        resultado[palavra] += contagem
    return resultado

# Passo 1: Aplicar o Map
mapped_data = map_func(dados)

# Passo 2: Aplicar o Reduce
reduced_data = reduce_func(mapped_data)

# Ordenar as palavras por contagem, de forma decrescente
sorted_data = sorted(reduced_data.items(), key=lambda item: item[1], reverse=True)

# Pegar as 10 palavras mais frequentes
top_10 = sorted_data[:10]

# Exibir as 10 palavras mais frequentes
print("As 10 palavras mais frequentes são:")
for palavra, contagem in top_10:
    print(f"{palavra}: {contagem}")
