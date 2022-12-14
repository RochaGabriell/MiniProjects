import csv

csv_rowlist = [["Abrindo arquivos em Python"],
    ["Modo", "Descrição"], 
    ["r", "Abre um arquivo para leitura. (default)"], 
    ["w", "Abre um arquivo para gravação. Cria um novo arquivo se não existir ou trunca o arquivo se existir."], 
    ["x", "Abre um arquivo para criação exclusiva. Se o arquivo já existir, a operação falhará."], 
    ["a", "Abre um arquivo para anexar no final do arquivo sem truncá-lo. Cria um novo arquivo se ele não existir."], 
    ["t", "Abre no modo de texto. (default)"], 
    ["b", "Abre em modo binário."], 
    ["+", "Abre um arquivo para atualização (leitura e escrita)"]]

# Escrevendo arquivos CSV usando csv.writer()
with open('File_Handling/Python/CSV/file.csv', 'w', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)

# Lendo arquivos CSV usando csv.reader()
with open('File_Handling/Python/CSV/file.csv', 'r', encoding = 'utf-8') as file:
    content = csv.reader(file)
    for i in content:
        print(*i)
