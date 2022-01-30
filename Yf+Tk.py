from tkinter import *
from matplotlib.figure import Figure

import yfinance as yf
import pandas as pd
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf
from tkinter import *
import tkinter as tk
# plot function is created for
# plotting the graph in
# tkinter window


def plot():

    # the figure that will contain the plot
    
    stock = str(STOCK.get())
    start = "2010-01-01"
    end = date.today()

    tcs = yf.download(stock, start, end)

    tcs['Open'].plot(label=stock, figsize=(15, 7))

    plt.title('Stock Prices of TCS, Infosys and Wipro')
    plt.legend()
    plt.show()

    

    # creating the Tkinter canvas
    # containing the Matplotlib figure



# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("500x500")

STOCK = Entry(window)
STOCK.pack()

# button that displays the plot
plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

# run the gui
window.mainloop()
