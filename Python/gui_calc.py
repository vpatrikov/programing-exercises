import PySimpleGUI as sg

sg.theme('Topanga')
layout = [
    [sg.Text("Calculator!", size=25, font=("Calibri", 25), justification="center" )],
    [sg.Text("Number 1:"), sg.InputText(key='-INPUT_1', size=25)],
    [sg.Text("Number 2:"), sg.InputText(key='-INPUT_2', size=25)],
    [sg.Text("", key="-TEXT-")],
    [sg.Button("Addition"), sg.Button("Subtraction"), sg.Button("Multiplication")],
    [sg.Button("Exit")]
]

window = sg.Window('Calculator', layout, element_justification='c')

def action(sign):
    try:
        num1 = float(values['-INPUT_1'])
        num2 = float(values['-INPUT_2'])
        if sign == '+':
            result = num1 + num2
        elif sign == '-':
            result = num1 - num2
        elif sign == '*':
             result = num1 * num2
        elif sign == '/':
             result = num1 / num2
        window["-TEXT-"].update(f"{num1} {sign} {num2} = {result}")
        
    except ValueError:
            window["-TEXT-"].update("Invalid input. Please enter numbers.")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == "Addition":
        action('+')
    elif event == "Subtraction":
         action('-')
    elif event == "Multiplication":
         action('*')
    elif event == "Division":
         action('/')

window.close()
