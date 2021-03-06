import chatserver as cserver
import chatclient as cclient
from tkinter import *
from tkinter import ttk
 
 
main = Tk()
main.title('Multipurpose Network Manager')
main.geometry('800x500')
 

# gives weight to the cells in the grid
rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1
 
# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Port Checker')
 
# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='File Sharer')

page3 = ttk.Frame(nb)

def serverclick():
 	Label(page3, bg='white', text="The server has been started").pack(side=BOTTOM)
 	cserver.Main()

def clientclick():
 	Label(page3, bg='white', text="The client has been started").pack(side=BOTTOM)

 	

#mybutton = Button(page3, text="MyButton") 
#mybutton.grid(row=1,column=1)
#mybutton1 = Button(page3, text="MyButton") 
#mybutton1.grid(row=50,column=1)
Button(page3, text="START SERVER", width=25,bg="#ba0000",command=serverclick() ).pack(side=TOP,padx=20, pady=20)
Button(page3, text="START CLIENT", width=25,bg="#ba0000",command=clientclick).pack(side=TOP,padx=20)
nb.add(page3, text='Server Client Chat')
 
 
main.mainloop()
