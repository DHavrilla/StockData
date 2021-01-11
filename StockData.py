import pandas
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


def get_data():
    ##Quick search of top 10 stocks to watch chosen
    print(
        "1. Apple\n" #AAPL
        "2. Spotify\n" #SPOT
        "3. BJ's Wholesale Club\n" #BJ
        "4. Disney\n" #DIS
        "5. Facebook - don't support Zuck\n" #FB
        "6. Alibaba Group\n" #BABA
        "7. Lowe's Co.\n" #LOW
        "8. Nautilus\n" #NLS
        "9. Sonos\n" #SONO
        "10. Newmont Corp.\n" #NEM
        "11. Enter your own\n")
    x = input("Enter Stock: \n")
    if x == "1":
        stock = 'AAPL'
    elif x == "2":
        stock = "SPOT"
    elif x == "3":
        stock = "BJ"
    elif x == "4":
        stock = "DIS"
    elif x == "5":
        print("You dirty human\n")
        stock = "FB"
    elif x == "6":
        stock = "BABA"
    elif x == "7":
        stock = "LOW"
    elif x == "8":
        stock = "NLS"
    elif x == "9":
        stock == "SONO"
    elif x == "10":
        stock = "NEM"
    elif x == "11":
        stock = input("Enter Stock: \n")
    else:
        return 0
    ##Start and End for stock dates defaulted to last year.
    start = "2020-01-01" #input("Enter Start Date (yyyy-mm-dd): \n")
    end = "2021-01-01" #input("Enter End Date (yyyy-mm-dd): \n")
    data = yf.download(stock, period = "max") #, start, end)

    data.Close.plot()
    plt.ylabel('Stock Value')
    plt.show()

def main():
    get_data()

if __name__== "__main__":
    main()
