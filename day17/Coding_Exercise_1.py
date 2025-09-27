import FreeSimpleGUI as sg

label_feet = sg.Text("Enter feet:")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches:")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
convert_result = sg.Text("", key="meters")

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button, convert_result]])

while True:
    event, values = window.read()
    print(event, values)
    meters = float(values["feet"]) * 0.3048 + float(values["inches"]) * 0.0254
    print(meters, "m")
    window["meters"].update(value=f"{meters} m")

window.close()
