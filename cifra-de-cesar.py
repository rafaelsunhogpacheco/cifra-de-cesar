


def codificarMensagem(mensagem):
    alfabeto =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mensagem = str(mensagem)
    mensagem = mensagem.lower()
    for letra in mensagem:
        # print(letra)
        if letra in alfabeto:
            # print(letra.index())
            posicao = alfabeto.index(letra)
            print(f'posição: {posicao}')
            LetraNova = alfabeto[(posicao + 3)]
            print(f'posicao + 3: {LetraNova}')



teste = codificarMensagem('aba')
