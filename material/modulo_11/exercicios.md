# Exercícios Flask

## Implementando a nossa API

Em um servidor web, a mesma rota pode lidar com diferentes tipos de ações. Por exemplo, `GET /eventos` e `POST /eventos` são duas ações diferentes para a mesma rota.

Utilizando o código fornecido em [flask_server.py](flask_server.py), implemente a view `editar_evento` de modo que ela consiga realizar tanto um update parcial quando um update completo de um evento.

Você também precisará implementar o método `get_evento(id)`, que foi deixado em branco.


* Obs.: o objeto [`request`](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.method) do Flask tem um atributo `method` que retorna uma `string` indicando a operação HTTP (GET, POST, PUT, PATCH...)
* Obs. 2: observe que a nossa lista de eventos agora está sendo criada em outro arquivo: [modelos.py](modelos.py).
* Obs. 3: a palavra especial `raise` do Python retorna uma *exceção*  (também chamada de *erro*). No caso, o método `editar_evento` está retornando um `NotImplemented`. Depois de finalizar sua implementação, você deve remover essa linha de código.


## Postman

Crie uma coleção de requisições no Postman contendo as seguintes operações:
* Listar eventos: `GET /api/eventos/`
* Detalhar evento: `GET /api/eventos/<int:id>/`
* Editar evento: `PUT /api/eventos/<int:id>/`
* Editar evento parcial: `PATCH /api/eventos/<int:id>/`
* Criar evento: `POST /api/eventos/`
* Deletar evento: `DELETE /api/eventos/<int:id>/`

Lembre-se que algumas requisições precisam enviar dados no *body* (corpo da requisição). Esses dados devem estar no format `raw / json`.

Veja [esse exemplo de uma requisição para criar eventos](exemplo_post_eventos.png).