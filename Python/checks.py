import PySimpleGUI as sg
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Choose a folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],[sg.Button("Submit")]]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))
    
while True:
    event, values = window.read()
    print(values["-IN2-"])
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        print(values["-IN-"])