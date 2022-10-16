import PySimpleGUI as sg
layout = [
    [sg.Text('Enter kg to convert:')],
    [sg.Input(key='-KG-'), sg.Button('Convert', key='-CONVERTKG-')],
    [sg.Text(key='-LBS-')],
    [sg.Text('Enter km to convert:')],
    [sg.Input(key='-KM-'), sg.Button('Convert', key='-CONVERTKM-')],
    [sg.Text(key='-MILES-')]
]

windows = sg.Window('Converter', layout)

while True:
    event, values = windows.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERTKG-':
        windows['-LBS-'].update(str(round(float(values['-KG-']) * 2.20462, 3)) + ' lbs' )
    
    if event == '-CONVERTKM-':
        windows['-MILES-'].update(str(round(float(values['-KM-']) * 0.6214, 3)) + '  miles')
        

windows.close()
