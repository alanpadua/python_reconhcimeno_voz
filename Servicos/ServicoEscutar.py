from re import A
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

class ServicoEscutar:
    frase_erro = 'Não entendi, habilite novamente o microfone.'

    def escutar(self):

        microfone = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                microfone.adjust_for_ambient_noise(source)
                print("Diga alguma coisa: ")
                audio = microfone.listen(
                    source, timeout=4, phrase_time_limit=3)

                frase = microfone.recognize_google(audio, language='pt-BR')
                # frase = microfone.recognize_ibm(audio, language='pt-BR')
                print("Você disse: " + frase)

        except sr.WaitTimeoutError:
            frase = self.frase_erro
            print('sr.WaitTimeoutError')
        except:
            frase = self.frase_erro
            print("Não entendi")

        # microfone.listen_in_background()
        # frase = 'qualquer coisa'
        return frase
        
# servicoEscutar = ServicoEscutar()
# servicoEscutar.escutar()
