---
presentation:
  theme: white.css
  center: true
  width: 1280
  height: 960
---
<!-- slide -->
# O que é uma API REST

<!-- slide -->
## O que é uma API

*Application Programming Interface*
- *Interface*: comandos
  - Controle remoto
  - Calculadora
  - Desktop
- *Application Programming*
  - Interface para outros *programas*: Google Maps API; Python API;


<!-- slide -->
## HTTP API

Expõe uma API através do protocolo HTTP

- `POST /usuarios/1/` -> Retorna usuario com id 1
- `POST /usuarios/` -> Retorna lista de usuários
- `POST /criar_usuario/` -> Cria um novo usuário
- `POST /deletar_usuario/1/` -> Exclui o usuário com id 1


<!-- slide -->
## REST API

*Representational State Transfer*
- Representação e manipulação do *estado* ou de *recursos* de uma aplicação.
- Exemplo: recurso *usuário*.


<!-- slide -->
## Padrões REST

- *Uniform interface*
- *Stateless*
- *Cacheable*
- *Client-server*


<!-- slide -->
### *Uniform Interface*

- Identificação de um recurso `usuario` **não-uniforme**
  - `POST /usuarios/1/` vs `POST /deletar_usuario/1/`

- Identificação **uniforme**:
  - `GET /usuarios/1/`
  - `DELETE /usuarios/1/`
  - `PUT /usuarios/1/`
  - `PATCH /usuarios/1/`


<!-- slide -->
### *Stateless*

- Não tem preservação de estado entre requisições.
- Cada requisição é suficiente para realizar uma operação.
- Exemplo: alterar um usuário – não é necessário "buscar" esse usuário antes.
  - Pode parecer óbvio, mas vale lembrar que esse artigo é do início dos anos 2000, então esses padrões *se tornaram* óbvios com a adoção majoritária.

<!-- slide -->
### *Cacheable*

- Vamos aprender ainda sobre como utilizar cache no curso.
- Basicamente: definimos respostas que podem ser cacheadas (*cacheable*), e não precisamos realizar a operação novamente.
- HTTP: header `Cache-Control`.


<!-- slide -->
### *Cliente-servidor*

- Também "óbvio" hoje em dia.
- Facilita a criação de diferentes clientes para a mesma aplicação.


<!-- slide -->
## HTTP != REST

- O padrão de arquitetura REST **não** precisa ser implementado em HTTP.
- Mas o protocolo HTTP atende **muito bem** os requisitos da arquitetura REST e é o principal utilizado na Web para comunicação entre cliente-servidor.
  - GET, POST, PUT, PATCH, DELETE...


<!-- slide -->
## JSON != HTTP

- JSON é apenas um dos **formatos** que podem ser utilizados para a representação e manipulação de recursos.
- Poderíamos utilizar outros como CSV, XML ou até formatos próprios.
- Porém, JSON acabou virando o padrão para aplicações Web.


<!-- slide -->
## Referências

- https://developer.mozilla.org/pt-BR/docs/Glossary/REST
- https://restfulapi.net/