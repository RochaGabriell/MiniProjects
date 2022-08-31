import json

"""
Modo Descrição
r Abre um arquivo para leitura. (default)
w Abre um arquivo para gravação. Cria um novo arquivo se não existir ou trunca o arquivo se existir.
x Abre um arquivo para criação exclusiva. Se o arquivo já existir, a operação falhará.
a Abre um arquivo para anexar no final do arquivo sem truncá-lo. Cria um novo arquivo se ele não existir.
t Abre no modo de texto. (default)
b Abre em modo binário.
+ Abre um arquivo para atualização (leitura e escrita)
"""

person_dict = {
    "name": "Gabriel",
    "age": 18,
    "married": False,
    "divorced": False,
    "children": None,
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
        ]
    }
# Gravando JSON em um arquivo
# Usando json.dumps() O pacote JSON em python tem uma função chamada json.dumps() que ajuda na conversão de um dicionário em um objeto JSON.
json_object = json.dumps(person_dict, indent = 4) # ajuda na conversão de um dicionário em um objeto JSON
with open('File_Handling/JSON/file.json', 'w', encoding = 'utf-8') as file:
    file.write(json_object)

"""
Outra maneira de escrever JSON em um arquivo é usando o json.dump(). O pacote JSON possui a função “dump” que grava diretamente o dicionário em um arquivo na forma de JSON, sem a necessidade de convertê-lo em um objeto JSON real.

with open('Arquivos/JSON/file.json', 'w', encoding = 'utf-8') as file:
    json.dump(person_dict, file)

"""

# Lendo o JSON de um arquivo com Python
with open('File_Handling/JSON/file.json', 'r', encoding = 'utf-8') as file:
    reading = json.load(file) # Função que carrega o conteúdo json de um arquivo json em um dicionário.
    print(reading) # Formato de dicionário.
    print(json.dumps(reading, sort_keys=False, indent=4)) # Formato em objeto Json.