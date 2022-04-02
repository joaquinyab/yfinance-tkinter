from tkinter import *
from scipy.misc import face
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
from tkinter import *


def plot():

    ticker1 = str(STOCK.get())
    ticker2 = str(STOCK2.get())
    start = "2011-01-01"
    end = date.today()

    tickerInfo = yf.Ticker(ticker1).info
    market_price = tickerInfo['regularMarketPrice']
    tickerPrice.set(market_price)

    if len(STOCK2.get()) == 0:
        stock1 = yf.download(ticker1, start, end)
        stock1['Open'].plot(label=ticker1, figsize=(15, 7))


        plt.style.use('dark_background')

        plt.show()


        plt.legend()
        plt.show()

        tickerInfo2 = yf.Ticker(ticker2).info
        market_price = tickerInfo2['regularMarketPrice']
        tickerPrice2.set(market_price)

    else:

        stock1 = yf.download(ticker1, start, end)
        stock2 = yf.download(ticker2, start, end)

        stock1['Open'].plot(label=ticker1, figsize=(15, 7))
        stock2['Open'].plot(label=ticker2, figsize=(15, 7))



        ax = plt.axes()
        plt.figure(facecolor="black")
        


        plt.title('')
        
        ax.set_facecolor("black")

        
        
        
        plt.legend()
        plt.show()
        




window = Tk()


window.title('Plotting in Tkinter')
window.geometry("400x400")
window.config(background="#0c0c22")

tickerPrice = StringVar()
tickerPrice2 = StringVar()

start = "2011-01-01"
end = date.today()



window.resizable(False, False)


STOCK = Entry(window,background="#aaa6ca")
STOCK.pack()



STOCK2 = Entry(window, background=  "#aaa6ca")
STOCK2.pack()


plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot",
                     background="#6c6889")


plot_button.pack()

crypto = Label(window, text="crypto 1", foreground="white", background="#0c0c22",textvariable=tickerPrice)
crypto.pack()

crypto2 = Label(window, text="crypto 2", foreground="white",
                background="#0c0c22", textvariable=tickerPrice2)
crypto2.pack()


window.mainloop()
