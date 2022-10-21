from brincadeira_com_mock.enviador_de_spam import EnviadorDeSpam


def test_criacao_enviador_de_spam():
    assert EnviadorDeSpam() is not None


def test_enviador_possui_destinatarios():
    enviador = EnviadorDeSpam(['luiz@email.com'])
    assert enviador.destinatarios == ['luiz@email.com']
    enviador.adicionar_destinatario('fernando@email.com')
    assert enviador.destinatarios == ['luiz@email.com', 'fernando@email.com']
