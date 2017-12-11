from tkinter import *
import sqlite3
'''Creation of table in not present during testing'''
conn = sqlite3.connect('StockTable.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS
            stockTable
            (Item_ID int,
            Item_Name varchar(255),
            Item_Price,
            Item_Weight,
            Item_Quantity,
            Minimum_Stock)''')

cur.execute('''CREATE TABLE IF NOT EXISTS
            orderTable
            (Item_Name,
            Order_Quantity)''')


class App:
    def __init__(self, master):
        self.master = master

        ''''Menu title'''

        theLabel = Label(root, text="Stock System")
        theLabel.pack()

        '''Creation of frames needed for the main menu'''

        testFrame = Frame(master)
        testFrame.pack(side=BOTTOM)
        middleFrame = Frame(master)
        middleFrame.pack()
        orderFrame = Frame(master)
        orderFrame.pack()
        completeFrame = Frame(master)
        completeFrame.pack()
        viewFrame = Frame(master)
        viewFrame.pack()
        bottomFrame = Frame(master)
        bottomFrame.pack(side=BOTTOM)

        self.testData = Button(testFrame, text='Test Data', command=self.dataEntry)

        self.update = Button(middleFrame, text='Add/Update Items', command=self.updateStockTable, width=25, height=3)
        self.order = Button(orderFrame, text='Place Order', command=self.updateOrderTable, width=25, height=3)
        self.complete = Button(completeFrame, text='Complete Order', command=self.completeOrder, width=25, height=3)
        self.view = Button(viewFrame, text='View Stock', command=self.viewStock, width=25, height=3)
        self.exit = Button(bottomFrame, text="Exit", command=exit)

        self.testData.pack(side=BOTTOM)

        self.update.pack(padx=5, pady=0)
        self.order.pack(padx=5, pady=0)
        self.complete.pack(padx=5, pady=0)
        self.view.pack(padx=5, pady=0)
        self.exit.pack(side=BOTTOM)

        """Connection to between main menu button and new window created for the task"""

    def updateStockTable(self):
        self.newWindow = Toplevel(self.master)
        self.app = updateStockTable(self.newWindow)

    def updateOrderTable(self):
        self.newWindow = Toplevel(self.master)
        self.app = Orders(self.newWindow)

    def completeOrder(self):
        self.newWindow = Toplevel(self.master)
        self.app = Complete(self.newWindow)

    def viewStock(self):
        self.newWindow = Toplevel(self.master)
        self.app = View(self.newWindow)

        """Sample data for inventory and orders"""

    def dataEntry(self):
        conn = sqlite3.connect('StockTable.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0000, 'Rice', '1.00', '1.000', '15', '60')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0001, 'Lettuce', '0.50', '0.600', '120', '80')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0002, 'Beef', '6.00', '2.200', '20', '10')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0003, 'Chicken', '5.39', '1.000', '60', '75')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0004, 'Ketchup', '1.00', '0.600', '90', '150')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0005, 'Cabbage', '0.80', '0.750', '40', '30')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0006, 'Potato', '2.00', '2.500', '80', '60')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0007, 'Beans', '1.50', '2.400', '50', '70')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0008, 'Chocolate', '2.00', '0.400', '100', '200')''')
        cur.execute('''INSERT INTO stockTable(Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (0009, 'Spaghetti', '0.20', '0.500', '300', '500')''')
        conn.commit()
        cur.execute('''INSERT INTO orderTable(Item_Name, Order_Quantity)
        VALUES ('Spaghetti', '300')''')
        conn.commit()
        cur.execute('''INSERT INTO orderTable(Item_Name, Order_Quantity)
        VALUES ('Chicken', '30')''')
        conn.commit()
        cur.execute('''INSERT INTO orderTable(Item_Name, Order_Quantity)
        VALUES ('Rice', '85')''')
        conn.commit()
        cur.execute('''INSERT INTO orderTable(Item_Name, Order_Quantity)
        VALUES ('Beans', '60')''')
        conn.commit()
        cur.execute('''INSERT INTO orderTable(Item_Name, Order_Quantity)
        VALUES ('Ketchup', '110')''')
        conn.commit()
        cur.execute('''INSERT INTO orderTable(Item_Name, Order_Quantity)
        VALUES ('Chocolate', '150')''')
        conn.commit()


'''Domain Layer for updating stock database'''

class updateStockTable:

    '''Creation of frames for the update page'''

    def __init__(self, master):
        self.master = master
        aFrame = Frame(master)
        aFrame.pack()
        bFrame = Frame(master)
        bFrame.pack()
        cFrame = Frame(master)
        cFrame.pack()
        dFrame = Frame(master)
        dFrame.pack()
        eFrame = Frame(master)
        eFrame.pack()
        fFrame = Frame(master)
        fFrame.pack()


        '''Naming each input box for the user'''

        self.idlabel = Label(aFrame, text="Item ID")
        self.namelabel = Label(bFrame, text="Item Name")
        self.pricelabel = Label(cFrame, text="Item Price")
        self.weightlabel = Label(dFrame, text="Item Weight")
        self.quantitylabel = Label(eFrame, text="Item Quantity")
        self.minimumlabel = Label(fFrame, text="Minimum Stock")

        '''Creation of buttons to update and close page'''

        self.update = Button(master, text="Update Item", command=self.Update)
        self.add = Button(master, text="Add Item", command=self.Add)
        self.close = Button(master, text="Close Window", command=self.close)

        '''Size settings for entry boxes'''

        self.idEntry = Entry(aFrame, bd=5)
        self.nameEntry = Entry(bFrame, bd=5)
        self.priceEntry = Entry(cFrame, bd=5)
        self.weightEntry = Entry(dFrame, bd=5)
        self.QuantityEntry = Entry(eFrame, bd=5)
        self.MinimumEntry = Entry(fFrame, bd=5)

        '''Creation of text box'''

        self.txt = Text(master, height=7, width=60)

        '''Placement of text within the window'''

        self.idlabel.pack(side=LEFT)
        self.namelabel.pack(side=LEFT)
        self.pricelabel.pack(side=LEFT)
        self.weightlabel.pack(side=LEFT)
        self.quantitylabel.pack(side=LEFT)
        self.minimumlabel.pack(side=LEFT)


        self.idEntry.pack(side=LEFT)
        self.nameEntry.pack(side=LEFT)
        self.priceEntry.pack(side=LEFT)
        self.weightEntry.pack(side=LEFT)
        self.QuantityEntry.pack(side=LEFT)
        self.MinimumEntry.pack(side=LEFT)


        self.update.pack(side=TOP)
        self.add.pack(side=TOP)
        self.txt.pack(side=TOP)
        self.close.pack(side=BOTTOM)

        for row in cur.execute('SELECT * FROM stockTable'):
            rows = str(row)
            self.txt.insert(END, "%s \n" % rows)

        '''Adds new items and item details to the inventory '''

    def Add(self):
        ID = self.idEntry.get()
        Name = self.nameEntry.get()
        Price = self.priceEntry.get()
        Weight = self.weightEntry.get()
        Quantity = self.QuantityEntry.get()
        Minimum = self.MinimumEntry.get()

        cur.execute('''INSERT INTO stockTable (Item_ID, Item_Name, Item_Price, Item_Weight,
        Item_Quantity, Minimum_Stock)
        VALUES (?, ?, ?, ?, ?, ?)''', (ID, Name, Price, Weight, Quantity, Minimum))

        conn.commit()
        self.txt.insert(END, "Item %s has been added \n" % Name)
        for row in cur.execute('SELECT * FROM stockTable'):
            rows = str(row)
            self.txt.insert(END, "%s \n" % rows)

    def Update(self):
        ID = self.idEntry.get()
        Name = self.nameEntry.get()
        Price = self.priceEntry.get()
        Weight = self.weightEntry.get()
        Quantity = self.QuantityEntry.get()
        Minimum = self.MinimumEntry.get()

        '''Updates each column of the inventory with the selected item id'''

        cur.execute('''UPDATE stockTable
            SET Item_Name = ?
            WHERE
              Item_ID = ?
              ''', (Name, ID))

        cur.execute('''UPDATE stockTable
            SET Item_Price = ?
            WHERE
              Item_ID = ? 
              ''', (Price, ID))

        cur.execute('''UPDATE stockTable
            SET Item_Weight = ?
            WHERE
              Item_ID = ? 
              ''', (Weight, ID))

        cur.execute('''UPDATE stockTable
            SET Item_Quantity = ?
            WHERE
              Item_ID = ?
              ''', (Quantity, ID))

        cur.execute('''UPDATE stockTable
            SET Minimum_Stock = ?
            WHERE
              Item_ID = ?
              ''', (Minimum, ID))


        conn.commit()
        self.txt.insert(END, "Item %s has been updated \n" % Name)
        for row in cur.execute('SELECT * FROM stockTable'):
            rows = str(row)
            self.txt.insert(END, "%s \n" % rows)


    def close(self):
        self.master.destroy()


class Orders:

    def __init__(self, master):
        self.master = master
        aFrame = Frame(master)
        aFrame.pack()
        bFrame = Frame(master)
        bFrame.pack()

        self.namelabel = Label(aFrame, text="Item Name")
        self.quantitylabel = Label(bFrame, text="Order Amount")

        self.order = Button(master, text="Order Item", command=self.Order)
        self.close = Button(master, text="Close Window", command=self.close)

        '''Size settings for entry boxes'''

        self.nameEntry = Entry(aFrame, bd=5)
        self.QuantityEntry = Entry(bFrame, bd=5)


        '''Creation of text box'''

        self.txt = Text(master, height=7, width=30)

        '''Placement of text within the window'''

        self.namelabel.pack(side=LEFT)
        self.quantitylabel.pack(side=LEFT)


        self.nameEntry.pack(side=LEFT)
        self.QuantityEntry.pack(side=LEFT)


        self.order.pack(side=TOP)
        self.txt.pack(side=TOP)
        self.close.pack(side=BOTTOM)

        for row in cur.execute('SELECT * FROM orderTable'):
            rows = str(row)
            self.txt.insert(END, "%s \n" % rows)

    '''Adds items to the order'''

    def Order(self):
        Name = self.nameEntry.get()
        Quantity = self.QuantityEntry.get()

        cur.execute('''INSERT INTO orderTable (Item_Name, Order_Quantity)
        VALUES (?, ?)''', (Name, Quantity))


        conn.commit()
        self.txt.insert(END, "Item %s has been ordered \n" % Name)
        for row in cur.execute('SELECT * FROM orderTable'):
            rows = str(row)
            self.txt.insert(END, "%s \n" % rows)


    def close(self):
        self.master.destroy()


class Complete:

    def __init__(self, master):
        self.master = master

        self.complete = Button(master, text="Confirm", command=self.completeOrder)
        self.txt = Text(master, height=7, width=30)
        self.close = Button(master, text="Close Window", command=self.close)


        self.close.pack(side=BOTTOM)

        self.complete.pack(side=TOP)
        self.txt.pack(side=TOP)

        for row in cur.execute('SELECT * FROM orderTable'):
            rows = str(row)
            self.txt.insert(END, "%s \n" % rows)

    '''Adds the new stock to the inventory and removes it from pending orders'''

    def completeOrder(self):

        for row in cur.execute('SELECT * FROM orderTable'):
            Name = str(row[0])
            Quantity = int(row[1])
            for item in cur.execute('SELECT * FROM stockTable WHERE Item_Name = ?', [Name]):
                Quantity_1 = int(item[4])
                newQuantity = (Quantity + Quantity_1)
                cur.execute('''UPDATE stockTable
                    SET Item_Quantity = ?
                    WHERE
                      Item_Name = ?
                      ''', (newQuantity, Name))
                conn.commit()
            cur.execute('DELETE FROM orderTable WHERE Item_Name = ?', [Name])
            conn.commit()

    def close(self):
        self.master.destroy()

    '''Displays a restricted view of the stock list'''

class View:

    def __init__(self, master):
        self.master = master

        self.txt = Text(master, height=7, width=60)
        self.close = Button(master, text="Close Window", command=self.close)

        self.txt.pack(side=TOP)
        self.close.pack(side=BOTTOM)

        for row in cur.execute('SELECT Item_Name, Item_Price, Item_Quantity, Minimum_Stock FROM stockTable'):
            item = row[0]
            price = row[1]
            quantity = int(row[2])
            min = int(row[3])
            pound = '$'
            self.txt.insert(END, "Item %s - Price %s%s - Quantity %s  \n" % (item, pound, price, quantity))

            '''Notifies staff if item levels drop below minimum '''

            if quantity < min:
                self.txt.insert(END, "Item %s low in stock, notify stock control assistant \n" % item)




    def close(self):
        self.master.destroy()



conn.commit()
root = Tk()
root.title("Stock System")
root.resizable(width=False, height=False)
app = App(root)
root.mainloop()
