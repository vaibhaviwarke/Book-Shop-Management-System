import sqlite3
from tkinter import messagebox
import datetime
import random
import fpdf


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.conn.commit()

    def insert(self, title, language, author, isbn, qty, genre, pur_pr, sell_pr):
        sold_qty = 0
        profit_mny = 0
        new_isbn = self.isbn(title,language)
        profit_per_book = sell_pr - pur_pr

        print(new_isbn)
        author_id = self.search_author(author)
        if author_id is None:
            self.cur.execute("insert into author (fname) values (?)",[author,])
            author_id_new = self.cur.lastrowid
            if new_isbn == isbn:
                self.update_qty(title, qty, isbn, language)
                self.conn.commit()
            else:
                print("inside elseif blk")
                self.cur.execute("INSERT INTO book VALUES(?,?,?,?,?)", (title, author_id_new, genre, isbn, language, ))
                self.cur.execute("INSERT INTO profit VALUES(?,?,?,?)", (isbn, qty, sold_qty, profit_mny, ))
                self.cur.execute("INSERT INTO store_purchase VALUES(?,?,?,?,?)", (isbn, pur_pr, sell_pr, qty, profit_per_book))
                print("inserted successfully!!!")
                self.conn.commit()
        else:
            if new_isbn == isbn:
                self.update_qty(title, qty, isbn, language)
                self.conn.commit()
            else:
                print("inside elseif blk")
                self.cur.execute("INSERT INTO book VALUES(?,?,?,?,?)", (title, author_id, genre, isbn, language, ))
                self.cur.execute("INSERT INTO profit VALUES(?,?,?,?)", (isbn, qty, sold_qty, profit_mny, ))
                self.cur.execute("INSERT INTO store_purchase VALUES(?,?,?,?,?)", (isbn, pur_pr, sell_pr, qty, profit_per_book))
                print("inserted successfully!!!")
                self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title, language):
        self.cur.execute("SELECT book.isbn,profit.rem_qty FROM book INNER JOIN profit "
                         "ON book.isbn = profit.isbn WHERE book.title = ? AND book.lang = ? ", (title, language,))
        rows = self.cur.fetchall()
        for row in rows:
            if row[1] > 0:
                return rows
            else:
                return None

    def delete(self, tname):
        self.cur.execute("DELETE FROM book WHERE title = ?", [tname, ])
        self.conn.commit()

    def select_qty(self, tname,lang):
        isbn = self.isbn(tname,lang)
        db_qty = self.cur.execute("select rem_qty from profit where isbn = ?", [isbn, ])
        for row in db_qty:
            print(row[0])
            p = row[0]
        return p

    def search_author(self,author):
        self.cur.execute("SELECT author_id FROM author WHERE fname = ?",[author,])
        rows = self.cur.fetchall()
        flag = 0
        for row in rows:
            print(row[0])
            author_id = row[0]
            int(author_id)
            flag = 1
        if flag == 1:
            return author_id
        else:
            return None

    def update_to_zero(self, tname,lang):
        isbn = self.isbn(tname,lang)
        db_qtyn = self.select_qty(tname,lang)
        self.cur.execute("UPDATE profit SET rem_qty = ? WHERE isbn = ?", [0, isbn, ])
        self.cur.execute("UPDATE store_purchase SET qty = ? WHERE isbn = ?", [0, isbn, ])
        self.conn.commit()

    def update_qty(self, tname, tqty, isbn, lang):
        actual_qty = 0
        db_qtyn = self.select_qty(tname, lang)
        int(tqty)
        print(tqty)
        actual_qty = db_qtyn + tqty
        print(actual_qty)
        self.cur.execute("UPDATE store_purchase SET qty = ? WHERE isbn = ?", [actual_qty, isbn, ])
        self.cur.execute("UPDATE profit SET rem_qty = ? WHERE isbn = ?", [actual_qty, isbn, ])
        self.conn.commit()

    def price(self, bname, lang):
        isbn_f = self.isbn(bname, lang)
        self.cur.execute("SELECT sale_pr FROM store_purchase where isbn = ?", [isbn_f, ])
        rows_price = self.cur.fetchall()
        for row in rows_price:
            print(row[0])
            sale_price = row[0]
            int(sale_price)
            return sale_price

    def isbn(self, bname, lang):
        self.cur.execute("SELECT isbn FROM book where title = ? AND lang = ?", [bname, lang, ])
        rows_isbn = self.cur.fetchall()
        if rows_isbn:
            for row in rows_isbn:
                print(row[0])
                isbn_fetched = row[0]
                int(isbn_fetched)
            return isbn_fetched
        else:
            return None

    def profit_per_book(self,isbn_f):
        self.cur.execute("SELECT profit_per_book FROM store_purchase where isbn = ?", [isbn_f, ])
        rows_price = self.cur.fetchall()
        for row in rows_price:
            print(row[0])
            profit_price = row[0]
            int(profit_price)
            return profit_price

    def update_profit(self):
        self.cur.execute("SELECT max(rowid) from cart")
        n = self.cur.fetchone()[0]
        self.cur.execute("select isbn,qty,price from cart")
        cart_val = self.cur.fetchall()

        for row in cart_val:
            profit_for_this_book = self.profit_per_book(row[0])
            total_prof = profit_for_this_book * row[1]
            self.cur.execute("UPDATE profit SET rem_qty = rem_qty - ?, sold_qty = sold_qty + ? ,"
                             "profit_mny= profit_mny + ? WHERE isbn = ?", [row[1],row[1],total_prof, row[0], ])
            #self.cur.execute("UPDATE store_purchase SET qty = qty - ? where isbn=?",(row[1], row[0], ))
            self.conn.commit()

    def add_customer(self, fname1, lname1, mob_no1):
        self.cur.execute("select isbn from cart")
        cart_val = self.cur.fetchall()

        for row in cart_val:
            self.cur.execute("select cust_id from customer where mob_no = ?",(mob_no1,))
            cust = self.cur.fetchall()
            if cust:
                for id in cust:
                    self.cur.execute("INSERT INTO sale (cust_id,isbn,pur_date) "
                                     "VALUES(?,?,date('now'))", (id[0], row[0],))
                    self.conn.commit()
            else:
                self.cur.execute("INSERT INTO customer (fname,lname,mob_no) VALUES(?,?,?)", (fname1,lname1,mob_no1,))
                cust_if_now = self.cur.lastrowid
                self.cur.execute("INSERT INTO sale (cust_id,isbn,pur_date) "
                                 "VALUES(?,?,date('now'))", (cust_if_now,row[0],))
                self.conn.commit()

    def authorid_to_authorName(self, author_id_fetched):
        author_id = int(author_id_fetched)
        self.cur.execute("select fname from author where author_id=?", [author_id])
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0])
            temp = row[0]
        return temp

    def search_by_authorId(self, title, lang):
        self.cur.execute("select author_id from book where title=? and lang=?", (title, lang))
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0])
            author_id = row[0]
            int(author_id)
            return author_id

    def select_qty_profit(self, tname, lang):
        isbn = self.isbn(tname, lang)
        db_qty = self.cur.execute("select rem_qty from profit where isbn = ?", [isbn, ])
        for row in db_qty:
            print(row[0])
            p = row[0]
        return p

    def select_qty_storepurchase(self, tname, lang):
        isbn = self.isbn(tname, lang)
        db_qty = self.cur.execute("select qty from store_purchase where isbn = ?", [isbn, ])
        for row in db_qty:
            print(row[0])
            p = row[0]
        return p

    def update_qty_for_receipt(self, tname, tqty, isbn, lang):
        actual_qty = 0
        db_qtyn_profit = self.select_qty_profit(tname, lang)
        db_qtyn_storepurchase = self.select_qty_storepurchase(tname, lang)
        int(tqty)
        print(tqty)
        actual_qty_profit = db_qtyn_profit - tqty
        print(actual_qty_profit)
        actual_qty_storepurchase = db_qtyn_storepurchase - tqty
        print(actual_qty_storepurchase)

        if actual_qty_profit >= 0 or actual_qty_storepurchase >= 0:
            self.cur.execute("UPDATE store_purchase SET qty = ? WHERE isbn = ?", [actual_qty_storepurchase, isbn, ])
            self.cur.execute("UPDATE profit SET rem_qty = ? WHERE isbn = ?", [actual_qty_profit, isbn, ])
            self.conn.commit()
        else:
            print("sorry " + tname + " is/are not available")
            messagebox.showinfo('ERROR', 'Sorry' + tname + 'is/are not available!!!')

    def cart_table(self, title, lang, qty, fname, lname):
        author_id_f = self.search_by_authorId(title, lang)
        author_id = int(author_id_f)

        author_name = self.authorid_to_authorName(author_id)

        price = self.price(title, lang)
        isbn = self.isbn(title, lang)
        actual_price = qty * price

        self.cur.execute("CREATE TABLE IF NOT EXISTS cart(isbn integer,fname text, lname text, title text,author text,"
                         "lang text,qty integer,price integer)")
        self.cur.execute("insert into cart values(?,?,?,?,?,?,?,?)",
                         (isbn, fname, lname, title, author_name, lang, qty, actual_price))


        self.conn.commit()
        print("inserted values successfully")

    def total_price(self):
        self.cur.execute("select sum(price) from cart")
        rows = self.cur.fetchall()
        for row in rows:
            total_price = row[0]
            return total_price

    def total_qty(self):
        self.cur.execute("select sum(qty) from cart")
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0])
            total_qty = row[0]
            return total_qty

    def display_bnames(self):
        bname = []
        self.cur.execute("select book.title from cart inner join book on book.isbn = cart.isbn")
        rows = self.cur.fetchall()

        for row in rows:
            bname.append(row[0])
        return bname

    def delete_table(self):
        self.cur.execute("DROP TABLE IF EXISTS cart")


    #ANALYSIS PART FUNCTIONS USE WISELY

    def graph_attr(self):
        self.cur.execute("SELECT sold_qty,title FROM profit inner join book on profit.isbn = book.isbn "
                         "where sold_qty != 0")
        rows = self.cur.fetchall()
        return rows

    def graph_attr_date(self):
        self.cur.execute("SELECT pur_date FROM sale")
        rows = self.cur.fetchall()
        return rows

    def max_sale_book(self):
        self.cur.execute("SELECT sold_qty,title FROM profit inner join book on profit.isbn = book.isbn "
                         "where sold_qty = (SELECT max(sold_qty) from profit)")
        rows = self.cur.fetchall()
        return rows

    def demanded_auth_names(self):
        auth_id_list = []
        self.cur.execute("SELECT author_id,sum(sold_qty) FROM profit inner join book on profit.isbn = book.isbn group by author_id ")
        rows = self.cur.fetchall()

        for row in rows:
            auth_id_list.append(row[0])
            print(row[0],row[1])

        sql = "SELECT distinct fname ,author.author_id FROM author inner join book on author.author_id = book.author_id where author.author_id in ({seq})".format(seq=','.join(['?'] * len(auth_id_list)))

        self.cur.execute(sql,auth_id_list)
        rows2 = self.cur.fetchall()

        for row in rows2:
            print(row[0],row[1])

        return rows, rows2

    def zero_book_list(self):
        self.cur.execute("SELECT title from book inner join profit on profit.isbn = book.isbn where rem_qty = 0")
        rows = self.cur.fetchall()
        return rows

    def most_cust_data(self):
        self.cur.execute("select cust_id,count(cust_id) as freq from sale group by cust_id order by freq desc limit 1")
        rows2 = self.cur.fetchall()
        cust_id = []
        for row in rows2:
            cust_id.append(row[0])
        sql = "select distinct fname,lname from customer inner join sale on customer.cust_id = sale.cust_id where sale.cust_id in ({seq})".format(seq=','.join(['?'] * len(cust_id)))
        self.cur.execute(sql,cust_id)
        rows2 = self.cur.fetchall()

        return rows2

    def cust_fname_lname(self):
        v = self.cur.execute("select * from cart")
        for row in v:
            fname = row[1]
            lname = row[2]
            temp = fname + " " + lname
            return temp

    def Export_To_PDF(self):
        l1 = []
        l2 = []
        now = datetime.datetime.now()
        d = str(random.randint(1, 100001))
        data11 = "\n-----------------------------------------------------------\n"
        data12 = "\n                 VISIT AGAIN\n"
        data13 = "                    RAHUL BOOK STORE\n\n"
        data14 = "RECEIPT NO : " + d + "\n\n"
        data15 = "DATE : " + str(now) + "\n\n"
        cust_name = self.cust_fname_lname()
        data17 = "CUSTOMER NAME: " + cust_name + "\n\n"
        data16 = "BOOK                      PRICE                        QTY\n\n"
        data = data11 + data13 + data11 + data14 + data15 + data11 + data17 + data11 + data16
        l2 = [data]
        data3 = data11 + data12 + data11
        p = self.cur.execute("select * from cart")
        for row in p:
            a = str(row[3])
            print(row[3])
            b = str(row[7])
            print(row[7])
            c = str(row[6])
            print(row[6])
            a += str(" " * (30 - len(a)))
            b += str(" " * (30 - len(b)))
            c += str(" " * (30 - len(c)))
            l1 = [a, b, c]
            l2.append(l1)
            l2.append("\n\n\n")

        t = self.total_price()
        data2 = "\n\nTOTAL PRICE : " + str(t) + " \n\n                                                      Signature:" + data3
        l2.append(data2)
        print("LIST2 : ", l2)
        pdf = fpdf.FPDF(format='letter')
        pdf.add_page()
        pdf.set_font("ARIAL", size=14)

        for i in l2:
            for x in i:
                pdf.write(5, str(x))
        rec = d + ".pdf"
        pdf.output(rec)
        pdf.close()

        receipt = messagebox.showinfo("Your receipt has been generated with " + rec)