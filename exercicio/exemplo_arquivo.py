def abrir_arquivo():
    # abre um arquivo para escrita
    arquivo = open('exemplo.txt', 'w+')
    # escreve no arquivo
    arquivo.write('Olá mundo')
    # fecha o arquivo
    arquivo.close()

def abrir_arquivo_with():
    # o bloco with vai fechar o arquivo automaticamente
    with open('exemplo1.txt', 'w+') as a:
        a.write('teste com with')

# leitura de um arquivo utilizando o mode=r.
# nesse caso ler o arquivo inteiro
def ler_arquivo():
    with open('exemplo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

# adicionar um conteúdo ao arquivo sem apagar o que estava
# anteriormente
def add_conteudo_arquivo(linha: str):
    with open('exemplo.txt', 'a') as arquivo:
        arquivo.write(linha + '\n')


def ler_arquivo_por_linha():
    with open('exemplo.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        
        for linha in linhas:
            print(linha)

ler_arquivo()
add_conteudo_arquivo('mais uma linha')
ler_arquivo()
ler_arquivo_por_linha()