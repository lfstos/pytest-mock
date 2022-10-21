class CanalEmail:
    def enviar(self, destinatario, msg):
        nome = destinatario.split('@')[0].capitalize()
        return destinatario, f'{nome} {msg}'

class EnviadorDeSpam:
    def __init__(self, destinatarios=None):
        self.destinatarios = destinatarios if destinatarios else []
        self.canal_de_envio = CanalEmail()

    def adicionar_destinatario(self, destinatario):
        self.destinatarios.append(destinatario)

    def enviar_spam(self, msg):
        canal_de_envio = CanalEmail()
        for destinatario in self.destinatarios:
                # for canal in self.canal_de_envio:
                    yield canal_de_envio.enviar(destinatario, msg)
