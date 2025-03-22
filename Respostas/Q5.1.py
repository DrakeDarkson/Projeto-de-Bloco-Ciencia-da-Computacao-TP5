import dns.resolver

class ColetorDNS:
    def __init__(self, dominio):
        self.dominio = dominio

    def consultar_registro(self, tipo):
        try:
            return [resposta.to_text() for resposta in dns.resolver.resolve(self.dominio, tipo)]
        except dns.resolver.NoAnswer:
            return ["Nenhuma resposta"]
        except dns.resolver.NXDOMAIN:
            return ["Domínio não encontrado"]

    def exibir_registros(self):
        print("Registros A:")
        print("\n".join(self.consultar_registro("A")))
        print("Registros MX:")
        print("\n".join(self.consultar_registro("MX")))
        print("Registros NS:")
        print("\n".join(self.consultar_registro("NS")))

dominio = "example.com"
ColetorDNS(dominio).exibir_registros()
