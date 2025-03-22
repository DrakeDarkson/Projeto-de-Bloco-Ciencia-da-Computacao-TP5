import socket
import ssl

class TLSClienteLogger:
    def __init__(self, host, porta):
        self.host = host
        self.porta = porta
        self.contexto = ssl.create_default_context()
        self.contexto.check_hostname = False
        self.contexto.verify_mode = ssl.CERT_NONE

    def enviar_mensagem(self, mensagem):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with self.contexto.wrap_socket(cliente, server_hostname=self.host) as cliente_tls:
            cliente_tls.connect((self.host, self.porta))
            print("Interceptado (envio):", mensagem.encode())
            cliente_tls.send(mensagem.encode())
            resposta = cliente_tls.recv(1024)
            print("Interceptado (recebido):", resposta)
            return resposta.decode()

cliente_logger = TLSClienteLogger("localhost", 12345)
cliente_logger.enviar_mensagem("Mensagem segura com logging de pacotes")
