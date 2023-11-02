import PySimpleGUI as sg
import os

sg.theme("DarkGray5")

layout = [
    [sg.Text("Flash Tool", size=(20, 1), font=("Calibri", 20), justification='center')],
    [sg.InputText("", key='file_input'), sg.FileBrowse(key='file_browse', file_types=(("Text Files", "*.txt"), ("All Files", "*.*")))],
    [sg.Button("Flash")]
]

window = sg.Window("Flash Tool", layout, element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "file_input":
        selected_file = values["file_input"]
    elif event == "file_browse":
        window["file_browse"].update(visible=False)
    elif event == "Flash":
        selected_file = values["file_input"]
        if selected_file:
            confirm_popup = sg.popup_yes_no(f"Are you sure you want to flash selected file?\n\n{selected_file}", title="Confirmation")
            if confirm_popup == "Yes":
                sg.popup_scrolled(open(selected_file, "r").read(), font=("Calibri", 16), size=(50,25), title=os.path.basename(selected_file))
        else:
            sg.popup("No file selected", title="Error")

window.close()
