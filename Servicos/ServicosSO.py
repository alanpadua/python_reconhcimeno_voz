import os

from numpy import array


class ServicosSO:

    def __init__(self):
        self.palavras_chave: array = [
            'abrir', 'pesquisar', 'buscar', 'firefox', 'chrome', 'limpar', 'console', 'sublime']

    def executar(self, comando):
        os.system(f"{comando} &")

    def clear(self):
        os.system('clear')

    def executar_comando(self, lista_palavras: array):
        if 'abrir' in lista_palavras:
            self.abrir_programas(lista_palavras)
        elif 'pesquisar' in lista_palavras or 'buscar' in lista_palavras or 'procurar' in lista_palavras:
            self.comandos_busca(lista_palavras)
        elif 'limpar' in lista_palavras and 'console' in lista_palavras:
            self.limpar()
        else:
            print('Comando não encontrado.')

    def abrir_programas(self, lista_palavras):
        if 'sublime' in lista_palavras:
            self.executar('subl')
        elif 'chrome' in lista_palavras:
            self.executar('google-chrome')
        elif 'firefox' in lista_palavras:
            self.executar('firefox')
        else:
            lista_palavras = self.remover_palavras_chave(lista_palavras)
            comando = ' '.join([str(elem) for elem in lista_palavras])
            self.executar(comando)

    def limpar(self):
        self.clear()

    def comandos_busca(self, lista_palavras):
        lista_palavras = self.remover_palavras_chave(lista_palavras)
        pesquisa = ' '.join([str(elem) for elem in lista_palavras])

        self.executar(f'firefox --search \'{pesquisa}\'')

    def remover_palavras_chave(self, lista_palavras: array):
        nova_lista: array = []
        for i in lista_palavras:
            if i not in self.palavras_chave:
                nova_lista.append(i)

        return nova_lista
