from tkinter import *
from tkinter import messagebox
import matplotlib
from backend import Database
from analysis import graph

matplotlib.use('tkAgg')
database = Database("newDbook.db")
grf = graph()
root = Tk()
str1 = str(650) + "x" + str(1500)
root.geometry(str1)
root.title("RAHUL BOOK SHOP")


def search_command():
    row = database.search(name_text.get(), language_text.get())
    return row


Tops = Frame(root, width=1500, height=150, bd=5, relief="raise")
Tops.place(x=500,y=150)
title = Label(Tops, text="RAHUL BOOK SHOP", font=("sansita", 30), bg="lightblue")
title.grid(row=3, column=2)

f = Frame(root, width=600, height=300, bd=10, relief="raise", bg="lightblue")
f.place(x=400, y=250)

user_text = StringVar()
L8 = Label(f, text="USERNAME ", font=('sansita', 15), height=2, bg="lightblue")
E8 = Entry(f, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=user_text)
L8.place(x=50, y=50)
E8.place(x=210, y=50)

pwd_text = StringVar()
L9 = Label(f, text="PASSWORD", font=('helvetica', 15), height=2, bg="lightblue")
E9 = Entry(f, bd=5, font=('helvetica', 16, 'bold'), insertwidth=2, justify='center', textvariable=pwd_text, show='*')
L9.place(x=50, y=100)
E9.place(x=210, y=100)

B3 = Button(f, text="LOGIN", font=('sans new', 15, 'bold'), height=2, width=16, relief=RAISED,
            command=lambda: login())
B3.place(x=200, y=200)


def login():
    if user_text.get() == '' and pwd_text.get() == '':
        #messagebox.showinfo("LOGIN SUCCESSFUL!")
        f.destroy()
        menu()
        frame1()
    else:
        messagebox.showerror('Invalid Username or Password!')


def iExit():
    qExit = messagebox.askyesno("Exit window", "Do you want to quit ?")
    if qExit > 0:
        root.destroy()
        return


# FRAMES-----------------------------------------------------------------
f1 = Frame(root, width=700, height=600, bd=10, relief="raise", bg="lightblue")  # Buy book cust details
f3 = Frame(root, width=(1500 / 10) * 6, height=450, bd=10, relief="raise", bg="lightblue")  # receipt
f2 = Frame(root, width=(1500 / 10) * 6, height=650, bd=10, relief="raise", bg="lightblue")
f4 = Frame(root, width=(1500 / 10) * 6, height=650, bd=10, relief="raise", bg="lightblue")  # insert
f5 = Frame(root, width=300, height=800, bd=10, relief="raise", bg="lightblue")  # menu
f6 = Frame(root, width=(1500 / 10) * 6, height=650, bd=10, relief="raise", bg="lightblue")  # delete book
f7 = Frame(root, width=900, height=300, bd=10, relief="raise", bg="lightblue")  # add another book to cart y/n
f8 = Frame(root, width=(1500 / 10) * 6, height=650, bd=10, relief="raise", bg="lightblue")  # analysis
f9 = Frame(root, width=700, height=600, bd=10, relief="raise", bg="lightblue")  # more than one book entry by same cust


def menu():
    f5.pack(side=LEFT)
    B4 = Button(f5, text="Add New Book", font=('arial', 15, 'bold'), height=2, width=16, relief=RAISED,    
                command=lambda: frame3_insert())
    B4.place(x=25, y=100)
    B5 = Button(f5, text="Delete a book", font=('arial', 15, 'bold'), height=2, width=16, relief=RAISED,    
                command=lambda: frame4_delete())
    B5.place(x=25, y=200)
    B6 = Button(f5, text="Sale Ratio", font=('arial', 15, 'bold'), height=2, width=16, relief=RAISED,    
                command=lambda: frame_analysis())
    B6.place(x=25, y=300)
    B6 = Button(f5, text="Home Page", font=('arial', 15, 'bold'), height=2, width=16, relief=RAISED,
                command=lambda: frame1())
    B6.place(x=25, y=400)


def delete(bname, lang):
    row = database.update_to_zero(bname, lang)
    f6.pack_forget()
    frame1()
    return row


def frame1():
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    f9.pack_forget()

    f1.pack(side=TOP)
    title1 = Label(f1, text="Make a entry here!", font=("helvetica", 25))
    title1.place(x=200, y=0)

    global name_text, E1
    name_text = StringVar()
    L1 = Label(f1, text="Book Name ", font=('arial', 15), height=2, bg="lightblue")
    E1 = Entry(f1, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=name_text)
    L1.place(x=50, y=100)
    E1.place(x=210, y=100)

    global language_text, E2
    language_text = StringVar()
    L2 = Label(f1, text="Language ", font=('arial', 15), height=2, bg="lightblue")
    E2 = Entry(f1, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=language_text)
    L2.place(x=50, y=150)
    E2.place(x=210, y=150)

    global cust_fname_text, E3
    cust_fname_text = StringVar()
    L3 = Label(f1, text="Buyer name ", font=('arial', 15), height=2, bg="lightblue")
    E3 = Entry(f1, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=cust_fname_text)
    L3.place(x=49, y=200)
    E3.place(x=210, y=200)

    global cust_lname_text, E4
    cust_lname_text = StringVar()
    L1 = Label(f1, text="Surname", font=('arial', 15), height=2, bg="lightblue")
    E4 = Entry(f1, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=cust_lname_text)
    L1.place(x=50, y=250)
    E4.place(x=210, y=250)

    global mob_no_text, E5
    mob_no_text = StringVar()
    L1 = Label(f1, text="Contact", font=('arial', 15), height=2, bg="lightblue")
    E5 = Entry(f1, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=mob_no_text)
    L1.place(x=50, y=300)
    E5.place(x=210, y=300)

    global qty_text, w
    qty_text = IntVar()
    L5 = Label(f1, text="  Qty", font=('arial', 15), height=2, width=5, bg="lightblue")
    w = Spinbox(f1, from_=0, to=10, font=('arial', 16, 'bold'), width=5, textvariable=qty_text)
    L5.place(x=480, y=90)
    w.place(x=550, y=100)

    B1 = Button(f1, text="ADD TO CART", font=('arial', 10, 'bold'), height=2, width=16, relief=RAISED,
                    command=lambda: check_details(mob_no_text.get(),name_text.get(),language_text.get(),cust_fname_text.get(),cust_lname_text.get(),qty_text.get()))
    B1.place(x=200, y=500)


def check_details(mobno, name, language, cust_fname, cust_lname, qty):

    if len(mobno) != 10:
        messagebox.showinfo("ERROR", "Mob no is invalid")
        E5.delete(0, END)
    if name == " ":
        messagebox.showinfo("ERROR", "bname is invalid")
        E1.delete(0, END)
    if language == " ":
        messagebox.showinfo("ERROR", "lang is invalid")
        E2.delete(0, END)
    if cust_fname == " ":
        messagebox.showinfo("ERROR", "custf is invalid")
        E3.delete(0, END)
    if cust_lname == " ":
        messagebox.showinfo("ERROR", "custl is invalid")
        E4.delete(0, END)
    if qty == 0:
        messagebox.showinfo("ERROR", "qty cant be 0")
        w.delete(0, END)
    if len(mobno) == 10 and name != " " and language != " " and cust_fname != " " and cust_lname != " " and qty != 0:
        frame5(name_text.get(), language_text.get(),
               qty_text.get(), cust_fname_text.get(), cust_lname_text.get())


def frame2():
    f1.pack_forget()

    f3.pack(side=TOP)
    title1 = Label(f3, text="RECEIPT", font=("arial", 25))
    title1.place(x=200, y=0)

    rows = database.display_bnames()
    book_names = ','.join(rows)
    L1 = Label(f3, text="BOOKS      :" + book_names, font=('arial', 10, 'bold'), height=2, bg="lightblue")
    L1.place(x=10, y=100)

    ecustf = cust_fname_text.get()
    ecustl = cust_lname_text.get()
    L2 = Label(f3, text="Buyer      :" + ecustf + " " + ecustl, font=('arial', 10, 'bold'), height=2, bg="lightblue")
    L2.place(x=5, y=150)

    price = database.total_price()
    L3 = Label(f3, text="Price      :" + str(price), font=('arial', 10, 'bold'), height=2, bg="lightblue")
    L3.place(x=400, y=150)

    tot_qty = database.total_qty()
    L5 = Label(f3, text="  Qty :" + str(tot_qty), font=('arial', 10, 'bold'), height=2, width=5, bg="lightblue")
    L5.place(x=400, y=100)

    B3 = Button(f3, text="EXIT", font=('arial', 10, 'bold'), height=3, width=16, bg="GREY", relief=RAISED,
                 command=lambda: iExit())
    B3.place(x=250, y=250)
    B4 = Button(f3, text="CONFIRM & PRINT", font=('arial', 10, 'bold'), height=3, width=16, bg="GREY", relief=RAISED,
            command=lambda: on_confirm())
    B4.place(x=450, y=250)


def on_confirm():
    # add customer to database and update profit table
    database.Export_To_PDF()
    database.update_profit()
    database.add_customer(cust_fname_text.get(), cust_lname_text.get(), mob_no_text.get())
    database.delete_table()  # cart deleted
    messagebox.showinfo("BOOK PURCHASED", "SALE DETAILS RECORDED")


def graph_data():
    grf.graph_sold_as_per_month()


def graph_data2():
    grf.graph_data_sold_book()


def frame3_insert():
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    f9.pack_forget()

    f4.pack(side=TOP)
    title1 = Label(f4, text="ENTER DETAILS TO ADD A BOOK", font=("arial", 25))
    title1.place(x=200, y=0)

    global name1_text, E1
    name1_text = StringVar()
    L1 = Label(f4, text="Book Name ", font=('arial', 15), height=2, bg="lightblue")
    E1 = Entry(f4, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=name1_text)
    L1.place(x=50, y=100)
    E1.place(x=210, y=100)

    global language1_text, E2
    language1_text = StringVar()
    L2 = Label(f4, text="Language ", font=('arial', 15), height=2, bg="lightblue")
    E2 = Entry(f4, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=language1_text)
    L2.place(x=50, y=150)
    E2.place(x=210, y=150)

    global author1_text, E3
    author1_text = StringVar()
    L3 = Label(f4, text="Author Name", font=('arial', 15), height=2, bg="lightblue")
    E3 = Entry(f4, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=author1_text)
    L3.place(x=49, y=200)
    E3.place(x=210, y=200)

    global isbn1_text, E4
    isbn1_text = IntVar()
    L4 = Label(f4, text="ISBN", font=('arial', 15), height=2, bg="lightblue")
    E4 = Entry(f4, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=isbn1_text)
    L4.place(x=50, y=250)
    E4.place(x=210, y=250)

    global genre1_text, E5
    genre1_text = StringVar()
    L5 = Label(f4, text="Genre", font=('arial', 15), height=2, bg="lightblue")
    E5 = Entry(f4, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=genre1_text)
    L5.place(x=50, y=300)
    E5.place(x=210, y=300)

    global pur_pr1_text, E6
    pur_pr1_text = IntVar()
    L6 = Label(f4, text="Purchase Price", font=('arial', 15), height=2, bg="lightblue")
    E6 = Entry(f4, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=pur_pr1_text)
    L6.place(x=50, y=350)
    E6.place(x=210, y=350)

    global sell_pr1_text, E7
    sell_pr1_text = IntVar()
    L7 = Label(f4, text="Selling Price", font=('arial', 15), height=2, bg="lightblue")
    E7 = Entry(f4, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=sell_pr1_text)
    L7.place(x=50, y=400)
    E7.place(x=210, y=400)

    global qty1_text, w
    qty1_text = IntVar()
    L8 = Label(f4, text="Quantity", font=('arial', 15), height=2, width=5, bg="lightblue")
    w = Spinbox(f4, from_=0, to=10, font=('arial', 16, 'bold'), width=5, textvariable=qty1_text)
    L8.place(x=480, y=90)
    w.place(x=550, y=100)

    B1 = Button(f4, text="ADD", font=('arial', 10, 'bold'), height=2, width=16, relief=RAISED,
                    command=lambda: add())
    B1.place(x=200, y=500)


def add():
    database.insert(name1_text.get(), language1_text.get(), author1_text.get(), isbn1_text.get(), qty1_text.get(),
                    genre1_text.get(), pur_pr1_text.get(), sell_pr1_text.get())
    f4.pack_forget()
    frame1()


def frame5(name, lang, qty,fname, lname):
    f1.pack_forget()
    row = search_command()
    if row is None:
        messagebox.showinfo("OUT OF STOCK!", "SORRY! BOOK NOT AVAILABLE !")
        frame1()
    else:
        for r in row:
            if qty_text.get() > r[1]:
                messagebox.showinfo("NO ENOUGH STOCK!", "SORRY, ONLY " + str(r[1]) + " BOOKS ARE AVAILABLE")
                frame1()
            else:
                global isbn
                isbn = r[0]
                f2.pack_forget()
                f3.pack_forget()
                f4.pack_forget()
                f6.pack_forget()
                f9.pack_forget()
                f8.pack_forget()
                f1.pack_forget()

                f7.pack(side=TOP)
                L1 = Label(f7, text="\t\t   Wish to buy one more Book? ", font=('arial', 15), height=2, bg="lightblue")
                L1.place(x=50, y=100)

                yB1 = Button(f7, text="YES", font=('arial', 10, 'bold'), height=2, width=16, relief=RAISED, command=lambda: btnclick_yes(isbn, name, lang, qty,fname, lname))
                yB1.place(x=200, y=200)
                nB1 = Button(f7, text="NO", font=('arial', 10, 'bold'), height=2, width=16, relief=RAISED,
                                 command=lambda: btnclick_no(isbn, name, lang, qty,fname, lname))
                nB1.place(x=400, y=200)


def btnclick_yes(isbn1, name, lang, qty,fname, lname):
    database.cart_table(name, lang, qty,fname, lname)
    f7.pack_forget()
    on_addtocart_frame()


def btnclick_no(isbn1, name, lang, qty,fname, lname):
    database.cart_table(name, lang, qty,fname, lname)
    f7.pack_forget()
    frame2()  # check once


def on_addtocart_frame():
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    f1.pack_forget()

    f9.pack(side=TOP)

    title1 = Label(f9, text="Make a new Entry", font=("helvetica", 25))
    title1.place(x=200, y=0)

    global dname_text, dE1
    dname_text = StringVar()
    L1 = Label(f9, text="Book Name ", font=('arial', 15), height=2, bg="lightblue")
    dE1 = Entry(f9, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=dname_text)
    L1.place(x=50, y=100)
    dE1.place(x=210, y=100)

    global dlanguage_text, dE2
    dlanguage_text = StringVar()
    L2 = Label(f9, text="Language ", font=('arial', 15), height=2, bg="lightblue")
    dE2 = Entry(f9, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=dlanguage_text)
    L2.place(x=50, y=150)
    dE2.place(x=210, y=150)

    L3 = Label(f9, text="Buyer             :" + cust_fname_text.get(), font=('arial', 15), height=2, bg="lightblue")
    L3.place(x=49, y=200)

    L1 = Label(f9, text="Surname        :" + cust_lname_text.get(), font=('arial', 15), height=2, bg="lightblue")
    L1.place(x=50, y=250)

    L1 = Label(f9, text="Contact          :" + mob_no_text.get(), font=('arial', 15), height=2, bg="lightblue")
    L1.place(x=50, y=300)

    global dqty_text, dw
    dqty_text = IntVar()
    L5 = Label(f9, text="Quantity", font=('arial', 15), height=2, width=5, bg="lightblue")
    dw = Spinbox(f9, from_=0, to=10, font=('arial', 16, 'bold'), width=5, textvariable=dqty_text)
    L5.place(x=480, y=90)
    dw.place(x=550, y=100)

    B1 = Button(f9, text="ADD TO CART", font=('arial', 10, 'bold'), height=2, width=16, relief=RAISED,
                    command=lambda: frame5(dname_text.get(), dlanguage_text.get(),
                                                      dqty_text.get(),cust_fname_text.get(), cust_lname_text.get()))
    B1.place(x=200, y=500)


def frame4_delete():
    f4.pack_forget()
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f7.pack_forget()
    f8.pack_forget()
    f9.pack_forget()

    f6.pack(side=TOP)
    title1 = Label(f6, text="Make a new entry", font=("arial", 25))
    title1.place(x=200, y=0)

    global name2_text, E1
    name2_text = StringVar()
    L1 = Label(f6, text="Book Name ", font=('arial', 15), height=2, bg="lightblue")
    E1 = Entry(f6, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=name2_text)
    L1.place(x=50, y=100)
    E1.place(x=210, y=100)

    global language2_text, E2
    language2_text = StringVar()
    L2 = Label(f6, text="Language ", font=('arial', 15), height=2, bg="lightblue")
    E2 = Entry(f6, bd=5, font=('arial', 16, 'bold'), insertwidth=2, justify='center', textvariable=language2_text)
    L2.place(x=50, y=150)
    E2.place(x=210, y=150)

    B8 = Button(f6, text="ok", font=('arial', 10, 'bold'), height=2, width=16, relief=RAISED,
                    command=lambda: delete(name2_text.get(), language2_text.get()))
    B8.place(x=200, y=300)


def frame_analysis():
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    f6.pack_forget()
    f7.pack_forget()
    f9.pack_forget()

    f8.pack(side=TOP)
    title1 = Label(f8, text="SALE ANALYSIS", font=("helvetica", 25), bg="lightblue")
    title1.place(x=200, y=0)

    max_book_names = grf.max_sold_book()
    book_names = ' '.join(max_book_names)
    L1 = Label(f8, text="TRENDING BOOK       :" + book_names, font=('arial', 15), height=2, bg="lightblue")
    L1.place(x=50, y=100)

    author_names = grf.demanded_author()
    auth_name = ''.join(author_names)
    L2 = Label(f8, text="TRENDING AUTHOR    :" + auth_name, font=('arial', 15), height=2, bg="lightblue")
    L2.place(x=50, y=150)

    zero_books_list = grf.zero_books()
    zero_book_names = ','.join(zero_books_list)
    L3 = Label(f8, text="OUT OF STOCK          :" + zero_book_names, font=('arial', 15), height=2, bg="lightblue")
    L3.place(x=49, y=200)

    cust_list = grf.most_freq_cust()
    cust_str = ','.join(cust_list)
    L1 = Label(f8, text="REGULAR BUYERS     :" + cust_str, font=('arial', 15), height=2, bg="lightblue")
    L1.place(x=50, y=250)

    B1 = Button(f8, text="BOOKWISE SALE", font=('arial', 10, 'bold'), height=2, width=16, relief=RAISED,
                    command=lambda: graph_data2())
    B1.place(x=200, y=500)

    B2 = Button(f8, text="DAYWISE SALE", font=('arial', 10, 'bold'), height=2, width=16, relief=RAISED,
                    command=lambda: graph_data())
    B2.place(x=450, y=500)


root.mainloop()
