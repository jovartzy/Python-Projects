import PySimpleGUI as sg

layout = [
    [sg.Text()],
    [sg.Button(), sg.Button()],
    [sg.Button(), sg.Button(), sg.Button(), sg.Button()],
    [sg.Button(), sg.Button(), sg.Button(), sg.Button()],
    [sg.Button(), sg.Button(), sg.Button(), sg.Button()]
]

window = sg.Window('Calc', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()