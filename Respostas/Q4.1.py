from scapy.all import ARP, Ether, srp

class VarreduraARP:
    def __init__(self, rede):
        self.rede = rede

    def executar(self):
        pacote = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=self.rede)
        respostas, _ = srp(pacote, timeout=2, verbose=False)
        for envio, recepcao in respostas:
            print(f"IP: {recepcao.psrc}, MAC: {recepcao.hwsrc}")

VarreduraARP("192.168.1.0/24").executar()
