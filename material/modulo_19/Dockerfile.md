1. Buscar a imagem que vamos utilizar como base. Exemplo: `python:3.10.4-slim-buster`
2. Definir o diretório de trabalho da imagem. Exemplo: `/app`
3. Copiar todos os arquivos do nosso projeto para a imagem.
4. Instalar todas as dependências de desenvolvimento na imagem.
5. Quando um container for executado a partir dessa imagem, um servidor Django deve ser exectuado (`runserver`).
