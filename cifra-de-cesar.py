
def codificarMensagem(mensagem):
    alfabeto =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # msgCripto = []
    msgCripto = ''
    mensagem = str(mensagem)
    mensagem = mensagem.lower()
    for letra in mensagem:
        # print(letra)
        if letra in alfabeto:
            # print(letra.index())
            posicao = alfabeto.index(letra)
            # print(f'posição: {letra}')
            letraNova = alfabeto[(posicao + 3)]
            # print(f'posicao + 3: {letraNova}')
            # msgCripto.append(letraNova)
            msgCripto = msgCripto + letraNova
        # print(msgCripto)
    return msgCripto

teste = print(codificarMensagem('bola'))

