import FreeSimpleGUI as sg

sg.theme("Black")

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input("", key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input("", key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text("", key="output")

col1 = sg.Column([[feet_label], [inches_label]])
col2 = sg.Column([[feet_input], [inches_input]])

window = sg.Window("Convertor", layout=[[col1, col2],
                                        [convert_button, exit_button, output_label]])
while True:
    event, values = window.read()
    match event:
        case "Convert":
            print(event, values)
            meters = float(values["feet"]) * 0.3048 + float(values["inches"]) * 0.0254
            print(meters, "m")
            window["output"].update(value=f"{meters} m")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
