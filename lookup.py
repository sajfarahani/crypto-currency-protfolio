import matplotlib.pyplot as plt
from tkinter import *
import requests
import json

import os
os.system('cls')

def red_green(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"

root = Tk()


#root.title("Crypto Currency Protfolio")

def lookup():
    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    api = json.loads(api_request.content)

    header_name = Label(root, text="Name", bg="white", font='Helvetica 12 bold' )
    header_name.grid(row=0, column=0, sticky=N+S+E+W)

    header_rank = Label(root, text="Rank", bg="white" , font='Helvetica 12 bold')
    header_rank.grid(row=0, column=1, sticky=N+S+E+W)

    header_current_price = Label(root, text="Current Price", bg="white", font='Helvetica 12 bold' )
    header_current_price.grid(row=0, column=2, sticky=N+S+E+W)

    header_price_paid = Label(root, text="Price Paid", bg="white", font='Helvetica 12 bold' )
    header_price_paid.grid(row=0, column=3, sticky=N+S+E+W)

    header_p_l_per = Label(root, text="Profit/Loss Per Coin", bg="white", font='Helvetica 12 bold' )
    header_p_l_per.grid(row=0, column=4, sticky=N+S+E+W)

    header_one_hr_change = Label(root, text="One Hr Change", bg="white", font='Helvetica 12 bold' )
    header_one_hr_change.grid(row=0, column=5, sticky=N+S+E+W)

    header_tf_hr_change = Label(root, text="Percent Change 24h", bg="white", font='Helvetica 12 bold' )
    header_tf_hr_change.grid(row=0, column=6, sticky=N+S+E+W)

    header_seven_day_change = Label(root, text="Percent Change 7d", bg="white", font='Helvetica 12 bold' )
    header_seven_day_change.grid(row=0, column=7, sticky=N+S+E+W)

    header_current_value = Label(root, text="Current Value", bg="white", font='Helvetica 12 bold' )
    header_current_value.grid(row=0, column=8, sticky=N+S+E+W)

    header_p_l_total = Label(root, text="Profit/Loss", bg="white", font='Helvetica 12 bold' )
    header_p_l_total.grid(row=0, column=9, sticky=N+S+E+W)

    my_portfolio =[
        {
            "sym" : "BTC",
            "amount_owned": 0,
            "price_paid_per": 0
        },
        {
            "sym" : "STEEM",
            "amount_owned": 3000,
            "price_paid_per": .80
        },
        {
            "sym": "XRP",
            "amount_owned": 5000,
            "price_paid_per": .20
        },
        {
            "sym": "XLM",
            "amount_owned": 2000,
            "price_paid_per": .10
        },
        {
            "sym": "EOS",
            "amount_owned": 1000,
            "price_paid_per": 2.00
        }
    ]
    portfolio_profit_loss = 0
    total_current_value = 0
    row_count = 1
    pie = []
    pie_size= []
    for x in api:
        for coin in my_portfolio:
            if coin["sym"] == x["symbol"]:
                total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
                current_value = float(coin["amount_owned"]) * float(x["price_usd"])
                profit_loss = current_value - total_paid
                portfolio_profit_loss += profit_loss
                profit_loss_per_coin = float(x["price_usd"]) - float(coin["price_paid_per"])
                total_current_value += current_value
                pie.append(x["name"])
                pie_size.append(coin["amount_owned"])

                # print (x["name"])
                # print (" Current Price: ${0:.2f}".format(float(x["price_usd"])))
                # print (" Profit/Loss Per Coin: ${0:.2f}".format(float(profit_loss_per_coin)))
                # print (" Rank: {0:.0f}".format(float(x["rank"])))
                # print (" Total Paid: {0:.2f}".format(float(total_paid)))
                # print (" Current Value: {0:.2f}".format(float(current_value)))
                # print (" Profit/Loss: {0:.2f}".format(float(profit_loss)))
                # print ("-----------------------------------------------------------------------------")

                name = Label(root, text=x["name"], bg="white")
                name.grid(row=row_count, column=0, sticky=N+S+E+W)

                rank = Label(root, text=x["rank"], bg="silver")
                rank.grid(row=row_count, column=1, sticky=N+S+E+W)

                current_price = Label(root, text="${0:.2f}".format(float(x["price_usd"])), bg="white")
                current_price.grid(row=row_count, column=2, sticky=N+S+E+W)

                price_paid = Label(root, text="${0:.2f}".format(float(coin["price_paid_per"])), bg="silver")
                price_paid.grid(row=row_count, column=3, sticky=N+S+E+W)

                p_l_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin)), bg="white", fg=red_green(float(profit_loss_per_coin)))
                p_l_per.grid(row=row_count, column=4, sticky=N+S+E+W)

                one_hr_change = Label(root, text="${0:.2f}%".format(float(x["percent_change_1h"])), bg="silver", fg=red_green(float(x["percent_change_1h"])))
                one_hr_change.grid(row=row_count, column=5, sticky=N+S+E+W)

                tf_hr_change = Label(root, text="${0:.2f}%".format(float(x["percent_change_24h"])), bg="white", fg=red_green(float(x["percent_change_24h"])))
                tf_hr_change.grid(row=row_count, column=6, sticky=N+S+E+W)

                seven_day_change = Label(root, text="${0:.2f}%".format(float(x["percent_change_7d"])), bg="silver", fg=red_green(float(x["percent_change_7d"])))
                seven_day_change.grid(row=row_count, column=7, sticky=N+S+E+W)

                current_value = Label(root, text="{0:.2f}".format(float(current_value)), bg="white")
                current_value.grid(row=row_count, column=8, sticky=N+S+E+W)

                p_l_total = Label(root, text="{0:.2f}".format(float(profit_loss)), bg="silver", fg=red_green(float(profit_loss)))
                p_l_total.grid(row=row_count, column=9, sticky=N+S+E+W)

                row_count += 1

    portfolio_profit_loss = Label(root, text="Profit/Loss: ${0:.2f}".format(float(portfolio_profit_loss)), font="Verdana 12 bold", fg=red_green(portfolio_profit_loss))
    portfolio_profit_loss.grid(row=row_count, column=0, sticky=W, padx=10, pady=10)

    root.title("Crypto Currency Protfolio - Profit Value:  ${0:.2f}".format(float(total_current_value)))
    # total_current_value = Label(root, text="Total Current Value: ${0:.2f}".format(float(total_current_value)), font= "Verdana 12 bold", fg=red_green(total_current_value))
    # total_current_value.grid(row=row_count, column=1, sticky=W, padx=10, pady=10)
    api= ""
    update_button = Button(root, text="Update Price", command=lookup)
    update_button.grid(row=row_count, column=9, sticky=E+S, padx=10, pady=10)

    def graph(pie, pie_size):
        # Data to plot
        labels = pie
        sizes = pie_size
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
        patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    graph_button = Button(root, text="Pie Chart", command=lambda: graph(pie, pie_size))
    graph_button.grid(row=row_count, column=8, sticky=E+S, padx=10, pady=10)


lookup()
root.mainloop()
