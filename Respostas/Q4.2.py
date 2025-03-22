from scapy.all import sniff, ARP

class DetectorARPSpoofing:
    def __init__(self):
        self.mapeamento = {}

    def verificar_pacote(self, pacote):
        if pacote.haslayer(ARP) and pacote.op == 2:
            ip = pacote.psrc
            mac_atual = pacote.hwsrc
            if ip in self.mapeamento and self.mapeamento[ip] != mac_atual:
                print(f"Alerta: Possível ARP Spoofing detectado para IP {ip}! MAC anterior: {self.mapeamento[ip]}, MAC atual: {mac_atual}")
            self.mapeamento[ip] = mac_atual

    def iniciar_monitoramento(self):
        sniff(store=False, prn=self.verificar_pacote, filter="arp")

DetectorARPSpoofing().iniciar_monitoramento()
