import PySimpleGUI as sg
sg.set_options(font= 'Calibri 17', button_element_size=(6,3))
button_size = (6,3)
layout = [
    [sg.Push(), sg.Text('0', key='txt')],
    [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
    [sg.Button('7', size = button_size), sg.Button('8', size = button_size), sg.Button('9', size = button_size), sg.Button('*', size = button_size)],
    [sg.Button('4', size = button_size), sg.Button('5', size = button_size), sg.Button('6', size = button_size), sg.Button('/', size = button_size)],
    [sg.Button('1', size = button_size), sg.Button('2', size = button_size), sg.Button('3', size = button_size), sg.Button('-', size = button_size)],
    [sg.Button('0', expand_x=True), sg.Button('.', size = button_size), sg.Button('+', size = button_size)]
]
sg.theme('dark')
window = sg.Window('Calc', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    match event:
        case '1': 
            num = values['txt']
            window['txt'].update(str(num) + '1')

window.close()