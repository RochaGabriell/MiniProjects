from difflib import SequenceMatcher
import os

class Originality:
   os.system("clear")
   def __init__(self, path : str, path_log : str):
      self.path = path
      self.path_log = path_log
      self.path_matriz = []
      self.registro_plagio = []
      self.comparator_list = []

   def occurrences(self):
      os.system("clear")
      print(f"\nINICIANDO O PROCESSO DE COMPARAÇÃO\n")
      for root, dirs, files in os.walk(self.path, topdown=True): # gera um árvore de diretórios percorrendo a árvore de cima para baixo ou de baixo para cima.
         aux = []
         for name in files:
            aux.append(os.path.join(root, name)) # Adicionar o diretorio e o mome do arquivo
         self.path_matriz.append(aux[:])
         aux.clear()
      
      del(self.path_matriz[0])
      
      for i, path in enumerate(self.path_matriz):
         print(f"| BLOCO {i+1} A SER ANALISADA.")
         for j, pathh in enumerate(self.path_matriz[i]):
            print(f"| --- {j+1} {self.path_matriz[i][j]}")
         print("+", "-"*80,end="\n")

   def smash_file(self):
      for folder in self.path_matriz: 
         aux = []
         for file in folder: 
            with open(file) as fileD: 
               read_py = fileD.read() # Lê todos os arquivos presente no diretório
               aux.append(read_py)
         self.comparator_list.append(aux[:])
         aux.clear()

   def comparator(self):
      print("\nINICIANDO PROCESSO DE COMPARAÇÃO DE ARQUIVO POR ARQUIVO...")
      with open(f'{self.path_log}/log.txt', 'w', encoding = 'utf-8') as file:
         temporary_matriz = self.comparator_list[:]
         for cl_index, file_text in enumerate(self.comparator_list):
            text_01 = f"BLOCO {cl_index+1} A SER ANALISADO..."
            file.write(f"{text_01}\n")
            for cll_index, file_text2 in enumerate(self.comparator_list[cl_index]): 
               text_02 = f"  ARQUIVO: {self.path_matriz[cl_index][cll_index]} COMPARANDO..."
               file.write(f"{text_02}\n")
               for tm_index, file_text3 in enumerate(temporary_matriz):
                  for ft_index, file_text4 in enumerate(file_text3):
                     similaridade = SequenceMatcher(None, file_text2, file_text4).ratio() # Compara o aquivo do index
                     percentage = similaridade * 100
                     if percentage >= 50 and self.path_matriz[cl_index][cll_index][:self.path_matriz[cl_index][cll_index].rfind("/")] != self.path_matriz[tm_index][ft_index][:self.path_matriz[tm_index][ft_index].rfind("/")]:
                        self.registro_plagio.append(f"Block Comparation - {cl_index+1}\n    Copy File : {self.path_matriz[cl_index][cll_index]}\n    Original File : {self.path_matriz[tm_index][ft_index]}\n        Percentage : {percentage:.0f}%\n")
                     text_03 = f"    {self.path_matriz[tm_index][ft_index]} : Similaridade: {percentage:.2f}%"   
                     file.write(f"{text_03}\n")                  
               file.write(f"\n")
      print("PROCESSO COMPLETO!!!")
      
   def report(self):
      with open(f'{self.path_log}/report.txt', 'w+', encoding = 'utf-8') as file:
         for report in self.registro_plagio:
            #print(json.dumps(report, sort_keys=False, indent = 1)) # Converte o dicionário em um objeto JSON
            file.write(f"{report}\n")