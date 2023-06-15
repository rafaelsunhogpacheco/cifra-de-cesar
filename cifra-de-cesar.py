
def codificarMensagem(mensagem):
    alfabeto =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    msgCripto = ''
    mensagem = str(mensagem)
    mensagem = mensagem.lower()
    for letra in mensagem:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            letraNova = alfabeto[(posicao + 3)]
            msgCripto = msgCripto + letraNova
    return msgCripto

def deCodificarMensagem(msg):
    alfabeto =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    msgDeCripto = ''
    msg = str(msg)
    msg = msg.lower()
    for letra in msg:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            letraNova = alfabeto[(posicao - 3)]
            msgDeCripto = msgDeCripto + letraNova
    return msgDeCripto

criptografar = codificarMensagem('rafael')

print(criptografar)

deCriptografar = deCodificarMensagem(criptografar)

print(deCriptografar)

