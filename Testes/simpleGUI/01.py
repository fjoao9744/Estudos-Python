from PySimpleGUI import PySimpleGUI as sg

sg.theme('Green')

tela = [
    [sg.text('Usuario:'), sg.Input(key='usuario')],
    [sg.text('Senha:'), sg.Input(key='senha', password_char='*')],
    [sg.text('')]
    [sg.text('')]
]