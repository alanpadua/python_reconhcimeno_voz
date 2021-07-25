from Servicos.ServicoIndex import ServicoIndex
from Utils import *
from messages import *

class IndexLayout:
    def __init__(self):
        pass

    def iniciar_layout(self):
        sg.theme('Dark Blue 3')

        layout = [
            [sg.Text(key='status', text='Não estou te ouvindo!', size=(100, 1))],
            [sg.Text(text='Você pode fazer uma busca?'),
             sg.InputText(key='campo_frase', default_text='Me diga algo!', enable_events=True)],
            [  # [sg.Button('Ok'),
                sg.Button('Ouvir'),
                sg.Button('Repetir'),
                sg.Button('Cancel')],
            [sg.Text(key='man_abrir', text=man_abrir)],
            [sg.Text(key='man_pesquisar', text=man_pesquisar)],
            [sg.Text(key='man_limpar', text=man_limpar)],
        ]
        window = sg.Window('Reconhecimento de Voz', layout)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()

            # Fechar aplicativo
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            # Para teste de código
            self.acao_ok(window, event)

            # Abrir microfone para ouvir comando
            self.acao_ouvir(window, event)

            # Repetir sentença falada ou escrrita.
            self.acao_repetir(window, event)

        window.close()

    def acao_ok(self, window, event):
        if event == 'Ok':
            set(window, 'campo_frase', 'frase')
            print(get(window, 'campo_frase'))

    def acao_repetir(self, window, event):
        if event == 'Repetir':
            valor = get(window, 'campo_frase')
            if valor == '':
                self.serviceIndex.falar()
            else:
                self.serviceIndex.falar(valor)

    def acao_ouvir(self, window, event):
        if event == 'Ouvir':
            timer_thread(alterar_status, [
                window, 'status', 'Estou te escutando!'])
            frase = self.serviceIndex.ouvir()
            set(window, 'campo_frase', frase)
            self.serviceIndex.comando_so()
            alterar_status(window, 'status', 'Não estou te escutando!')
