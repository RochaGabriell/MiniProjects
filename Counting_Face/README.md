<h1 align="center">Visão Computacional</h1>

<p align="justify">Este programa usa a biblioteca OpenCV para detectar rostos em uma transmissão ao vivo da webcam ou em um arquivo de vídeo armazenado na máquina local. Este programa detecta rostos em tempo real e os rastreia. Ele usa classificadores XML pré-treinados para o mesmo. Os classificadores usados neste programa têm características faciais treinadas neles.

### 📋 Pré-requisitos

```
Python
Numpy
OpenCV
dlib
```

### 🔧 Instalação

Instale os pré-requisitos do dlib:

Ubuntu 

A instalação do CMake, Boost, Boost.Python e X11 pode ser realizada facilmente com o apt-get :

```
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libboost-all-dev
```

Navegar até o diretório raiz da sua aplicação, abra o terminal e execulte o seguinte comando:

```
$ git clone https://github.com/RochaGabriell/MiniProjects.git
```

Vá até o diretório:

```
$ MiniProjects/Counting_Face/
```

E digitar:

```
$ python -m venv env
```

Ativar venv no windows digite no terminal:

```
$ \env\Scripts\activate.bat
```

No linux: 

```
$ source env/bin/activate
```

Instalar os pacotes necessários:

```
$ pip install -r requirements.txt
```

## ⚙️ Executando os testes

Para execultar, basta digitar no terminal:

```
$ python3 Counting_Face/main.py
```

## 🛠️ Construído com

* [dlib](http://dlib.net/) - Kit de ferramentas para criar aplicativos de aprendizado de máquina e análise de dados do mundo real
* [Numpy](https://numpy.org/) - Oferece funções para se trabalhar com computação numérica
* [OpenCV](https://opencv.org/) - biblioteca de ligações Python projetadas para resolver problemas de visão computacional

## 📄 Licença

Este projeto está sob a licença (MIT License) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

---