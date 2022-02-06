from django.http.response import HttpResponse
from agenda.seed import eventos

def exibir_evento(request):
    return HttpResponse(f"""
    <html>
        <h1>Evento: {eventos[0].nome}</h1>
        <p>Categoria: {eventos[0].categoria}</p>
        <p>Local: {eventos[0].local}</p>
        <p>Link: {eventos[0].link}</p>
    <html>
    """)