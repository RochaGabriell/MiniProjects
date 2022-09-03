from pytube import YouTube, Playlist
import moviepy.editor as mp
import re
import os

def main():
    os.system("clear")
    print("╓═══════════════════════════════════╖\n║                MENU               ║\n╚═══════════════════════════════════╝\n╟ 1 - Download Vídeo                ╢\n╟ 2 - Download PlayList(Vídeo)      ╢\n╟ 3 - Download Áudio                ╢\n╟ 4 - Download PlayList(Áudio)      ╢\n╟ 0 - Sair                          ╢\n╙═══════════════════════════════════╜")

    op = str(input("-> "))
    
    if op == "0":
        return exit()

    link = str(input("Link: "))
    # path = str(input("Diretótio: "))

    if op == "1":    
        return download_video(link)
    elif op == "2":
        return download_playlist_video(link)
    elif op == "3":
        return download_audio(link)
    elif op == "4":
        return download_playlist_audio(link)
    else:
        return main()

def download_video(link):
    os.system("clear")
    yt = YouTube(link) # Recebe a URL informada
    path = "Youtube_Download/Downloads/Vídeos" # Diretório definido para a pasta download
    print("Baixando...")
    video = yt.streams.get_highest_resolution().download(path) # get_highest_resolution() : Busca a melhor qualidade de download do vídeo. download() : Informo o diretório que ficara o arquivo
    print("Download Completo!")

    prox = str(input("Pressione ENTER tecla para continuar..."))
    return main()

def download_playlist_video(link):
    os.system("clear")
    nome_playlist = str(input("Nome da PlayList: "))
    path = "Youtube_Download/Downloads/"+nome_playlist # Diretório definido para a pasta download
    playlist = Playlist(link) # Recebe a URL informada
    for i, url in enumerate(playlist): # Vai percorrer toda a playlist e informar vídeo à vídeo
        print(f"{i+1} - {url} \nBaixando...")
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution() # Busca a melhor qualidade de download do vídeo. 
        video.download(output_path=path) # Informo o diretório que ficara o arquivo
    print("Download Completo!")

    prox = str(input("Pressione ENTER tecla para continuar..."))
    return main()

def download_audio(link):
    os.system("clear")
    yt = YouTube(link) # Recebe a URL informada
    path = "Youtube_Download/Downloads/Áudio" # Diretório definido para a pasta download
    print("Baixando...")
    audio = yt.streams.filter(only_audio=True).first().download(path) # get_highest_resolution() : Busca a melhor qualidade de download do vídeo. download() : Informo o diretório que ficara o arquivo
    print("Convertendo...")
    for file in os.listdir(path): # Inicia o processo de conversão com a biblioteca OS
        if re.search("mp4", file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0] + ".mp3")
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path) # Remove o arquivo .mp4 da presente pasta
    print("Download Completo!!!")

    prox = str(input("Pressione ENTER tecla para continuar..."))
    return main()
    
def download_playlist_audio(link):
    os.system("clear")
    nome_playlist = str(input("Nome da PlayList: "))
    path = "Youtube_Download/Downloads/"+nome_playlist # Diretório definido para a pasta download
    print("Baixando...")
    playlist = Playlist(link) # Recebe a URL informada
    for i, url in enumerate(playlist): 
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first().download(output_path=path) # get_highest_resolution() : Busca a melhor qualidade de download do vídeo. download() : Informo o diretório que ficara o arquivo
        print(f"{i+1} - {url} \nConvertendo...")
        for file in os.listdir(path): # Inicia o processo de conversão com a biblioteca OS
            if re.search("mp4", file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + ".mp3")
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path) # Remove o arquivo .mp4 da presente pasta
    print("Download Completo!")

    prox = str(input("Pressione ENTER tecla para continuar..."))
    return main()

if __name__ == "__main__":
    main()