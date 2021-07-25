from Servicos.ServicoEscutar import ServicoEscutar
from Servicos.ServicoFalar import ServicoFalar
from Servicos.ServicosSO import ServicosSO


class ServicoIndex:

    def __init__(self):
        self.data = []
        self.frase: str = None
        self.servicoEscutar: ServicoEscutar = ServicoEscutar()
        self.servicoFalar: ServicoFalar = ServicoFalar()
        self.servicosSO: ServicosSO = ServicosSO()
        # self.reticao: bool = True
        # self.layout = Layout()
        self.servicosSO.clear()

    def ouvir(self):
        self.frase = self.servicoEscutar.escutar().lower()
        return self.frase

    def falar(self, frase='Frase não informada'):
        self.frase = frase
        self.servicoFalar.criar_audio(self.frase, 'audio-frase.mp3')

    def comando_so(self):
        self.data = self.frase.split(" ")
        self.servicosSO.executar_comando(self.data)

# controllerIndex = ControllerIndex()
# index.ouvir()
# index.falar()
# index.comando_so()
