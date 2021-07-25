import time
from threading import Timer

import PySimpleGUI as sg


def alterar_status(window: sg.Window, key: str, status: str):
    window.Element(key).Update(value=status)
    window.Refresh()


def set(window: sg.Window, key: str, valor: str):
    window.Element(key).Update(value=valor)
    window.Refresh()


def get(window: sg.Window, key: str):
    return window.FindElement(key).Get()


def delay(segundos: int):
    start_time = time.time()
    time.sleep(segundos)


def timer_thread(metodo, paramentros):
    Timer(2.5, metodo, paramentros).run()
