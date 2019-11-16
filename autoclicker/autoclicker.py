from tkinter import *
from tkinter import messagebox

from pynput.keyboard import *

import pyautogui

# Variables #
enable = False

start_key = Key.f4
end_key = Key.f6

# Window #

window = Tk()
window.geometry("300x300")
window.title("Auto Clicker")
window.resizable(0, 0)

window.iconbitmap(r"icon.ico")

# Buttons #
enableButton = Button(window, text="Enable", font=("Arial Bold", 10), command=lambda: on_press_button("enable"));
disableButton = Button(window, text="Disable", font=("Arial Bold", 10), command=lambda: on_press_button("disable"))

# Labels #
infoLabel = Label(window, text="Auto clicker desenvolvido por:")
authorLabel = Label(window, text="stooneg0mes")

# Setting buttons & label position #
enableButton.place(y=150, x=200)
disableButton.place(y=150, x=50)

infoLabel.place(y=100, x=70)
authorLabel.place(y=120, x=120)


def on_press_button(button):
    global enable

    if button == "disable":
        if not enable:
            messagebox.showerror("Auto clicker já desabilitado!", "Para habilitar, clique no botão de habilitar.")
        else:
            enable = False
    elif button == "enable":
        if enable:
            messagebox.showerror("Auto clicker já habilitado!", "Para desabilitar, clique no botão de desabilitar.")
        else:
            enable = True


def on_press(key):
    global enable

    if key == start_key:
        enable = True
    elif key == end_key:
        enable = False


def main():
    listener = Listener(on_press=on_press)
    listener.start()

    window.mainloop()

    while enable:
        pyautogui.click(pyautogui.position())
        pyautogui.PAUSE = 1


main()