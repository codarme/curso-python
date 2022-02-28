from flask import Flask, jsonify, abort, make_response, request, url_for
from modelos import Evento, EventoOnline, eventos


app = Flask(__name__)


@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []
    for ev in eventos:
        eventos_dict.append(ev.__dict__)
    return jsonify(eventos_dict)


@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):  # view
    ev = get_evento(id)
    return jsonify(ev.__dict__)


@app.route("/api/eventos/", methods=["POST"])
def criar_evento():
    json_data = request.get_json() 
    nome = json_data.get("nome", None)
    local = json_data.get("local", None)
    if not nome:
        abort(400, "'nome' deve ser informado")

    if local:
        novo_evento = Evento(nome=nome, local=local)
    else:
        novo_evento = EventoOnline(nome=nome)
        
    eventos.append(novo_evento)
    return {
        "url": url_for('detalhar_evento', id=novo_evento.id),
        "id": novo_evento.id,
        "nome": novo_evento.nome,
        "local": novo_evento.local,
    }


@app.route("/api/eventos/<int:id>/", methods=["DELETE"])
def deletar_evento(id):
    evento = get_evento(id)  # Vai parar no `abort`
    eventos.remove(evento)
    return (jsonify(id=evento.id), 200)


@app.route("/api/eventos/<int:id>/", methods=["PATCH", "PUT"])  # Aceita tanto PATCH quanto PUT
def editar_evento(id):
    json_data = request.get_json() 
    nome = json_data.get("nome", None)
    local = json_data.get("local", None)

    evento = get_evento(id)
    # TODO: implementar a edição de eventos com PATCH e com PUT
    # Se for PUT, editar o evento completamente
    # Se for PATCH, editar o evento parcialmente
    raise NotImplementedError("Métod não implementado!")

    return {
        "id": evento.id,
        "nome": evento.nome,
        "local": evento.local,
    }


@app.errorhandler(400)
@app.errorhandler(404)
def handle_status(erro):
    return (jsonify(erro=erro.description), erro.code)


def get_evento(id):
    # TODO: implementar get_evento
    for ev in eventos:
        if ev.id == id:
            return ev
    abort(404, "Evento não encontrado")

