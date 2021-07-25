from gtts import gTTS
from playsound import playsound


class ServicoFalar:

    def criar_audio(self, frase: str, nome_arquivo: str):
        tts = gTTS(frase, lang='pt-br')
        tts.save(nome_arquivo)

        print('Foi isso que você disse?')
        playsound(nome_arquivo)
