let musica = document.querySelector("audio");
let cont_musica = 0;

let musicas = [
    {
        titulo: "O Sol e a Lua",
        artista: "Enygma",
        src: "music/O Sol e a Lua.mp3",
        img: "img/capas/Sol_Lua.jpeg"
    },
    {
        titulo: "???%",
        artista: "Enygma",
        src: "music/Mob.mp3",
        img: "img/capas/mod.jpeg"
    },
    {
        titulo: "Comédia Divina ",
        artista: "TakaB",
        src: "music/Comédia Divina.mp3",
        img: "img/capas/comedia_divina.jpeg"
    },
];

renderizarMusica(cont_musica)

let imagem = document.querySelector("img");
let nome_musica = document.querySelector(".descricao h2");
let autor_musica = document.querySelector(".descricao i");
let fim = document.querySelector(".fim");

musica.addEventListener("timeupdate", progressoMusicaTempo);
musica.addEventListener("timeupdate", progressoMusica);

document.querySelector(".botao_play").addEventListener("click", tocarMusica);
document.querySelector(".botao_pause").addEventListener("click", pausarMusica);

document.querySelector(".anterior").addEventListener("click", () => {
    cont_musica --;
    
    if (cont_musica < 0) {
        cont_musica = musicas.length - 1;
    }
    renderizarMusica(cont_musica);
}); // Função anônima
document.querySelector(".proximo").addEventListener("click", () => {
    cont_musica ++;

    if (cont_musica > musicas.length - 1){
        cont_musica = 0;
    }
    renderizarMusica(cont_musica);
});



function tocarMusica() {
    musica.play();
    document.querySelector(".botao_play").style.display = "none";
    document.querySelector(".botao_pause").style.display = "block";
}

function pausarMusica() {
    musica.pause();
    document.querySelector(".botao_play").style.display = "block";
    document.querySelector(".botao_pause").style.display = "none";
}

function progressoMusica() {
    let progresso = document.querySelector("progress");
    let duracao = Math.floor((musica.currentTime / musica.duration) * 100)
    progresso.style.width = duracao + "%";
}

function progressoMusicaTempo() {
    let inicio = document.querySelector(".inicio");
    inicio.textContent = segundoMinutos(musica.currentTime);
}

function segundoMinutos(segundos) {
    let camp_minutos = Math.floor(segundos / 60);
    let camp_segundos = Math.floor(segundos % 60);

    if (camp_segundos < 10) {
        camp_segundos = "0" + camp_segundos
    }

    return camp_minutos + ":" + camp_segundos;
}

function renderizarMusica(cont_musica) {
    musica.setAttribute("src", musicas[cont_musica].src);
    musica.addEventListener("loadeddata", () => {
        imagem.src = musicas[cont_musica].img;
        nome_musica.textContent = musicas[cont_musica].titulo;
        autor_musica.textContent = musicas[cont_musica].artista;
        fim.textContent = segundoMinutos(musica.duration)
        pausarMusica();
        progressoMusica()
    });
};