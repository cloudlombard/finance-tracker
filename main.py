import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np

labels = []
expenses = []


def draw_plot(labels, expenses):
    plt.pie(np.array(expenses), labels=labels)
    plt.show(block=False)


layout = [
    [sg.Text("Type your latest expense: "), sg.InputText(do_not_clear=False)],
    [sg.Text("Type the amount of cash you've spent on your latest expense: "), sg.InputText(do_not_clear=False)],
    [sg.Button("Insert expense"),
     sg.Button('Plot a chart of your expenses'),
     sg.Cancel()]
]

window = sg.Window('Finance Tracker', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Insert expense':
        labels.append(values[0])
        expenses.append(values[1])
    elif event == 'Plot a chart of your expenses':
        draw_plot(labels, expenses)
window.close()
