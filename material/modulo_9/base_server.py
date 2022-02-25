from http.server import HTTPServer, BaseHTTPRequestHandler
import hashlib


def hash_string(texto):
    """
    Recebe um texto como string e retorna a representação hash desse texto.
    Exemplo:
        hash_string("123") -> "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
    """
    return hashlib.sha256(texto.encode()).hexdigest() 


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/usuarios":
            # Enviar o status code da resposta: self.send_reponse(status_code)
            # Enviar cabeçalhos: self.send_header(nome, valor)
            # Finalizar cabeçalhos: self.end_headers()
            # Escrever dados para o "socket" (wfile): self.wfile.write(data)
            print("Implementar!")

 
server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()