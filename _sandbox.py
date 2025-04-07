import csv
from datetime import datetime
import os
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import sys

def main():
    path = os.path.abspath(__file__)
    path = path[:path.rfind('\\')+1]
    filename = path + 'sitka_weather_2018_simple.csv'
    displayMenuItems(filename)

def displayMenuItems(filename):
    fig_menu = plt.figure(figsize=(3, 3))

    button1_ax = plt.axes([0.1, 0.75, 0.8, 0.15])
    button1 = Button(button1_ax, 'View Highs')

    button2_ax = plt.axes([0.1, 0.5, 0.8, 0.15])
    button2 = Button(button2_ax, 'View Lows')

    button3_ax = plt.axes([0.1, 0.25, 0.8, 0.15])
    button3 = Button(button3_ax, 'Exit')

    button1.on_clicked(lambda event: on_button_click(filename, "high"))
    button2.on_clicked(lambda event: on_button_click(filename, "low"))
    button3.on_clicked(lambda event: on_button_click(filename, "exit"))

    plt.show()

def on_button_click(filename, parameter):
    if parameter == 'exit': 
        plt.close()
        exitMsg()
    else:
        plt.close()
        dates, params = buildlist(filename, parameter)
        plotGraph(parameter, dates, params)

def buildlist(filename, parameter): 
    param_row = 5 if parameter == 'high' else 6
    dates, params = [], []

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        for row in reader:
            try:
                row_date = datetime.strptime(row[2], '%Y-%m-%d')
                value = int(row[param_row])
            except ValueError:
                continue
            dates.append(row_date)
            params.append(value)

    return dates, params

def setParamVariables(parameter):
    if parameter == 'high': 
        return 'red', 'low'
    else: 
        return 'blue', 'high'

def plotGraph(parameter, dates, params):
    color, altParam = setParamVariables(parameter)
    fig, ax = plt.subplots()
    ax.plot(dates, params, c=color)
    plt.subplots_adjust(bottom=.3)

    button1_ax = plt.axes([0.1, 0.15, 0.35, 0.1])
    button1 = Button(button1_ax, f'Switch to {altParam.capitalize()}')
    button1.on_clicked(lambda event: switchGraph(filename, altParam))

    button2_ax = plt.axes([0.55, 0.15, 0.35, 0.1])
    button2 = Button(button2_ax, 'Exit')
    button2.on_clicked(lambda event: exitMsg())

    plt.title(f"Daily {parameter.capitalize()} Temperatures - 2018", fontsize=18)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.show()

def switchGraph(filename, parameter):
    plt.close()
    dates, params = buildlist(filename, parameter)
    plotGraph(parameter, dates, params)

def exitMsg():
    fig = plt.figure(figsize=(2, 1))
    plt.text(0.25, 0.5, "Goodbye!", fontsize=14)
    plt.axis('off')

    button_ax = plt.axes([0.3, 0.1, 0.4, 0.3])
    button = Button(button_ax, 'OK')
    button.on_clicked(lambda event: sys.exit())

    plt.show()

if __name__ == "__main__":
    main()
