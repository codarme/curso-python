# Guia Rápido – Containers

## Conceitos

* Containers: instâncias de processos criadas a partir de *imagens*. Geralmente utilizados para isolar partes de uma aplicação do *host* e de outras aplicações.
  * `docker run <imagem>`: inicializa o container a partir de `<imagem>`
* Imagens: criadas a partir de um Dockerfile. São análogas à imagem ISO de um sistema operacional só que geralmente mais leves e voltadas para uma aplicação específica.
  * `docker build .`: cria uma *imagem* a partir do `Dockerfile` na pasta presente.
* Máquina virtual: emulação **completa** de um sistema operacional.
* Docker: programa para facilitar o gerenciamento de containers.
* Docker-Desktop: versão GUI (interface gráfica) para gerenciar *containers*. Disponível para Windows e Mac
* DockerHub: repositório de imagens públicas que podem ser baixadas e utilizadas como base para outras imagens.


## Cheatsheet

`docker run <imagem>`: executa container a partir de `<imagem>`. A opção `--rm` (`docker run --rm <imagem>`) indica que esse container deve ser automaticamente destruído após sua execução.

`docker run -dp 1234:5678 <imagem>`: executa o container em background (`-d`) e mapeia a porta `1234` do **host** para a porta `5678` do **container**.

`docker exec -it 243114be0df8 /bin/sh`: executa o *shell* (linha de comando) em um container rodando.

`docker rm <container id>`: remove o container a partir do id (ou nome).

`docker ps -a`: exibe todos os containers (parados ou em execução).

`docker ps -q`: exibe apenas os ids dos containers.

`docker rm $(docker ps -aq)`: remove TODOS os containers.

`docker rmi <image id>`: remove a imagem a partir do id (ou nome).

`docker images` OU `docker image ls`: exibe todas as imagens.

`docker rmi $(docker image ls -q)`: remove TODAS as imagens.

`docker build .`: faz o *build* de uma nova imagem a partir do `Dockerfile` na pasta atual.

`docker logs <container id>`: exibe os logs do container.

`docker-compose up`: executa todos os containers (*services*) definidos no `docker-compose.yml`.

`docker-compose up --build`: força a *build* da imagem antes de executar os *containers*.

`docker-compose up <service>`: executa apenas o *service* específicado.

`docker-compose down`: para todos os *services*.
