import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
import struct
import sys

class GravarAudio:
    def __init__(self, tempoDeGravacao = 5, nomeArquivoSaida = "saidaMic.wav") -> None:
        chunk = 1024
        formato = pyaudio.paInt16
        canais = 1
        taxaDeAmostragem = 44100

        deltaX = 1.0/taxaDeAmostragem

        objetoPyAudio = pyaudio.PyAudio()

        print("Gravando durante ", tempoDeGravacao, "  segundos...")

        streamMic = objetoPyAudio.open(format=formato, channels=canais, rate=taxaDeAmostragem, input=True, frames_per_buffer=chunk)

        framesWav = []

        # captura dados do microfone
        for nLoop in range(0, int(taxaDeAmostragem / chunk * tempoDeGravacao)):
            dadosLidosMic = streamMic.read(chunk)
            framesWav.append(dadosLidosMic)
        # framesWav é uma lista com 215 "chunks" de 1024 amostras

        streamMic.stop_stream()
        streamMic.close()
        objetoPyAudio.terminate()

        # criamos uma única lista com todos os bytes encadeados
        framesWavJuntos = b''.join(framesWav)

        # salvamos o arquivo wave
        self.salvarWav(nomeArquivoSaida, canais, objetoPyAudio, formato, taxaDeAmostragem, framesWavJuntos)
        self.plotarFrequenciaAudio(framesWavJuntos, taxaDeAmostragem)

        print("Fim de gravação")

        return 0

    def plotarFrequenciaAudio(self, framesWavJuntos, taxaDeAmostragem):
        sinalAudio = np.frombuffer(framesWavJuntos, np.int16)
        print(len(sinalAudio))

        tempo = np.linspace(0, len(sinalAudio) / taxaDeAmostragem, num=len(sinalAudio))

        plt.figure(1)
        plt.title('Sinal Audio gravado')
        plt.plot(tempo, sinalAudio)
        plt.show()

    def salvarWav(self, nomeArquivoSaida, canais, objetoPyAudio, formato, taxaDeAmostragem, framesWavJuntos):
        arquivoWav = wave.open(nomeArquivoSaida, 'wb')
        arquivoWav.setnchannels(canais)
        arquivoWav.setsampwidth(objetoPyAudio.get_sample_size(formato))
        arquivoWav.setframerate(taxaDeAmostragem)
        arquivoWav.writeframes(framesWavJuntos)
        arquivoWav.close()



GravarAudio(tempoDeGravacao=5)
