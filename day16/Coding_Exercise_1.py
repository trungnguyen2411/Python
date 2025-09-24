import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input()

label2 = sg.Text("Enter inches:")
input2 = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button]])

window.read()
window.close()

# Solution:
import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button]])

window.read()
window.close()
