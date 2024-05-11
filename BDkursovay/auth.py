import os
import PySimpleGUI as sg
import config
import layout

window = sg.Window('Авторизация', layout.layout0)

layout = 1
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'auth':
        os.system('python bd8.py')
        file = open("user.txt", "w")
        file.write(f"{values['log']}\n{values['pas']}")
        file.close()
        break
    if event == 'reg':
        pass
window.close()
