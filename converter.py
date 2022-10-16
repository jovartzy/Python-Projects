import PySimpleGUI as sg
layout = [
    [sg.Text('Conversion Program')],
    [sg.Input(key='-INPUT-'), sg.Spin(['kg to lbs','km to miles'], key='-SPIN-'), sg.Button('Convert', key='-CONV-')],
    [sg.Text(key='-FINAL-')]
]

windows = sg.Window('Converter', layout)

while True:
    event, values = windows.read()

    if event == sg.WIN_CLOSED:
        break

    # if event == '-CONVERTKG-':
    #     windows['-LBS-'].update(str(round(float(values['-KG-']) * 2.20462, 3)) + ' lbs' )
    
    # if event == '-CONVERTKM-':
    #     windows['-MILES-'].update(str(round(float(values['-KM-']) * 0.6214, 3)) + '  miles')

    if event == '-CONV-':
        print(values['-INPUT-'])
        input_vals = values['-INPUT-']
        if input_vals.isnumeric():
            match values['-SPIN-']:
                case 'kg to lbs':
                    windows['-FINAL-'].update(str(round(float(values['-INPUT-']) * 2.20462, 3)) + ' lbs' )
                case 'km to miles':
                    windows['-FINAL-'].update(str(round(float(values['-INPUT-']) * 0.6214, 3)) + '  miles')
    

windows.close()
