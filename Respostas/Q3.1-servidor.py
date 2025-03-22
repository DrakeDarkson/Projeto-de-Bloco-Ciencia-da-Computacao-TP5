import socket
import ssl

contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain(certfile="server.crt", keyfile="server.key")

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("127.0.0.1", 12345))
servidor.listen(5)

with contexto.wrap_socket(servidor, server_side=True) as servidor_ssl:
    conexao, endereco = servidor_ssl.accept()
    print("Conexão estabelecida com", endereco)
    dados = conexao.recv(1024).decode()
    print("Recebido:", dados)
    conexao.send(dados.encode())
    conexao.close()
