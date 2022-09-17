from originality import Originality
import os

# Pra que serve
# tantos códigos?
# Se a vida
# não é programada
# e as melhores coisas
# não tem lógica

def main(path, path_log):
   try:
      bool_path = os.listdir(path)
      bool_path_log = os.listdir(path_log)
      print(bool_path_log)
   except:
      print("Erro inesperado\nOcorreu um erro não previsto no sistema.\nPor favor, não faça isso dnv... \nO tecnico não liga muito pro usuário.")
      return 0
   
   val = Originality(path, path_log)
   val.occurrences()
   val.smash_file()
   val.comparator()
   val.report()

if __name__ == "__main__":
   print(f"Informe o DIRETÓRIO (Ex. /home/rochagabriell/Documentos/RandomAlgorithmsPOO/Python/Exercicios/Detector_Plagio/Files)")
   path =  str(input("-> "))
   print(f"Informe o DIRETÓRIO que será gerado o arquivo de Log (Ex. /home/rochagabriell/Documentos/RandomAlgorithmsPOO/Python/Exercicios/Detector_Plagio/log)")
   path_log = str(input("-> "))
   main(path, path_log)