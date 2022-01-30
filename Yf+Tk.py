from tkinter import *
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt
import yfinance as yf
from tkinter import *




def plot():



 
    ticker1 = str(STOCK.get())
    ticker2 = str(STOCK2.get())
    start = "2012-01-01"
    end = date.today()

    if len(STOCK2.get()) == 0:
        stock1 = yf.download(ticker1, start, end)
        stock1['Open'].plot(label=ticker1, figsize=(15, 7))

        plt.show()

    else:

        stock1 = yf.download(ticker1, start, end)
        stock2 = yf.download(ticker2,start,end)
    

        stock1['Open'].plot(label=ticker1, figsize=(15, 7))
        stock2['Open'].plot(label=ticker2, figsize=(15, 7))
    

        plt.title('Stock Prices of TCS, Infosys and Wipro')
        plt.legend()
        plt.show()



    
window = Tk()



window.title('Plotting in Tkinter')
window.geometry("400x400")

window.resizable(False, False)




STOCK = Entry(window)
STOCK.pack()

STOCK2 = Entry(window)
STOCK2.pack()




plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")


plot_button.pack()

window.mainloop()
