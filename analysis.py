from datetime import datetime
from collections import *

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('tkAgg')
from backend import Database
database = Database("newDbook.db")


class graph:
    def __init__(self):
        print("in init")

    def graph_data_sold_book(self):
        # Connect to database
        book_name = []
        quantity = []
        quantity_in_per = []

        rows = database.graph_attr()
        for row in rows:
            book_name.append(row[1])
            quantity.append(row[0])

        max_sold_book = max(quantity)
        for qty in quantity:
            per_qty = (qty*100)/max_sold_book
            quantity_in_per.append(per_qty)

        plt.bar(book_name, quantity_in_per, width=0.5, color=['red', 'green'])

        plt.xlabel('Book_Name')
        # naming the y-axis
        plt.ylabel('No of Sold Copies in %')
        # plot title
        plt.title('No of Sold copies per book')

        # plt.plot(book_name,quantity)
        plt.show()

    def graph_sold_as_per_month(self):
        fdate = []
        days = []
        x_axis = []
        y_axis = []

        rows = database.graph_attr_date()
        for row in rows:
            fdate.append(row[0])
        for dy in fdate:
            date_object = datetime.strptime(dy,"%Y-%m-%d").date()
            days.append(date_object.strftime("%d"))
            days = list(map(int,days))
            freq = Counter(days)

        freq = OrderedDict(freq.items())
        #print(freq)
        for x,y in freq.items():
            x_axis.append(x)
            y_axis.append(y)


        plt.bar(x_axis,y_axis,width=0.5, color=['red', 'green'],align='center')
        plt.locator_params(axis='x',nbins=len(x_axis))
        plt.xticks(x_axis,x_axis)
        plt.xlabel('DAY IN OCTOBER MONTH')
        # naming the y-axis
        plt.ylabel('NO OF BOOKS SOLD')
        # plot title
        plt.title('APPROXIMATE SALE AS PER DAY')

        # plt.plot(book_name,quantity)
        plt.show()

    def max_sold_book(self):
        max_book_name = []

        rows = database.max_sale_book()
        for row in rows:
            max_book_name.append(row[1])

        return max_book_name

    def demanded_author(self):
        auth_names = []

        rows,rows2 = database.demanded_auth_names()
        max_val = max(rows,key=lambda x:x[1])

        for a,b in rows2:
            if b == max_val[0]:
                max_name = a

        return max_name

    def zero_books(self):
        book_list = []
        rows = database.zero_book_list()

        for row in rows:
            book_list.append(row[0])

        return book_list

    def most_freq_cust(self):
        cust = []
        rows = database.most_cust_data()
        for row in rows:
            cust.append(row[0])
        return cust
