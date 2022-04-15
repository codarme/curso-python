# Exercícios Módulo 19 – Docker


## Exercício 1 – Instalando o Docker

[Baixe e instale o Docker na sua máquina](https://docs.docker.com/get-docker/). Após a instalação, execute o comando:

`docker run -d -p 80:80 docker/getting-started`

Abra o seu navegador e verifique que você consegue acessar o tutorial em `http://localhost:80`.


## Exercício 2 – Executando um container Ubuntu

1. Execute o `bash` em um container **Ubuntu** utilizando o comando `docker run`.
2. Acesse o `bash` do *container* através do Docker Desktop (dashboard).


## Exercício 3 – Criando imagens com Dockerfile

1. Crie um `Dockerfile` a partir dos passos descritos em [`Dockerfile.md`](./Dockerfile.md).
2. Faça um `build` da imagem criada e execute o container a partir dela.
3. Acesse o container e faça uma requisição utilizando o `shell` do Django e a biblioteca `requests`.
4. Observe os logs do container com `docker logs -f <container id>`.


## Exercício 4 – Mapeando portas host/container

1. Pare o container rodando nosso servidor com `docker stop <container>`.
2. Execute o container novamente, mas agora com a opção `-p 8000:800`.
3. Você agora deve conseguir fazer requisições para o container a partir do host (usando Postman).


## Exercício 5 – Persistindo dados entre containers

Crie 2 containers `ubuntu` de modo que você consiga criar um arquivo em um deles com `touch meu_texto.txt` e acessar esse arquivo no outro container com `cat meu_texto.txt`.

1. Crie um volume com `docker volume create <nome-volume>`
2. Crie o container passando a flag `-v <nome-volume>:/<caminho-app>`


## Exercício 6 – Autoreload

Pare o container do projeto Django caso ele esteja rodando. Utilize o `bind mount` do Docker para associar um diretório do **host** a um diretório do **container** de forma que alterar qualquer arquivo no host, gere uma alteração no container e vice versa.

Dica: `-v <caminho/até/projeto>:/<diretório de trabalho do projeto>`


## Exercício 7 – Docker Compose

> Se você usa Linux, provavelmente precisa instalar o [binário do docker-compose](https://docs.docker.com/compose/install/). Caso você utilize Mac/Windows, o `docker-compose` já foi instalado junto com o Docker Desktop.

Utilizando o arquivo [docker-compose.yml](./docker-compose.yml) como base, faça os ajustes necessários para rodar o projeto com um único comando: `docker-compose up`.

P.S.: Talvez você precise do seu próprio arquivo `docker.env`.