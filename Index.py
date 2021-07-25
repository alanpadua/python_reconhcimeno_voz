from Servicos.ServicoIndex import ServicoIndex
from Utils import *
from messages import *
from Layout.IndexLayout import IndexLayout


class Index(IndexLayout):

    def __init__(self):
        self.serviceIndex = ServicoIndex()
        self.iniciar_layout()

layout = Index()
