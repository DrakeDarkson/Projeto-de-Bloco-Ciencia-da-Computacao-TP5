import socket
import ssl

contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

cliente = socket.create_connection(("127.0.0.1", 12345))
with contexto.wrap_socket(cliente, server_hostname="127.0.0.1") as cliente_ssl:
    print("Cliente: conexão estabelecida")
    mensagem = "Olá, servidor TLS!"
    cliente_ssl.send(mensagem.encode())
    resposta = cliente_ssl.recv(1024).decode()
    print("Cliente: recebido:", resposta)
