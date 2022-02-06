# Import libraries
from tkinter import *

# Create window
window = Tk()
window.title("Matrix Rank Calculator")
window.configure(width=500, height=500, bg='lightgray')

# DIMENTIONS
# Create matrix dimention label
dimentionsLabel = Label(window, text="Matrix dimentions:", font=("verdana", 12), bg="lightgray")
dimentionsLabel.place(x=30, y=25)

# Create dimentions input
rows = Entry(window, font=("verdana", 12))
rows.place(x=200, y=25, width=20, height=24)

columns = Entry(window, font=("verdana", 12))
columns.place(x=247, y=25, width=20, height=24)

# Create x label for dimentions
xLabel = Label(window, text="X", font=("Verdana", 12), bg="lightgray")
xLabel.place(x=225, y=25)



# MATRIX
# Create matrix label
matrixLabel = Label(window, text="Matrix:", font=("verdana", 12), bg="lightgray")
matrixLabel.place(x=30, y=65)

def calc_rank(a):
    print(a)

def create_matrix():
    # Create matrix
    m = int(rows.get())
    n = int(columns.get())
    i = 0
    j = 0
    a = []
    b = []

    while i < m:
        while j < n:
            # Create input
            b.append(Entry(window, font=('verdana', 12)).place(width=20, height=24, x=30+j*40, y=105+i*40))
            a.append([])
            a[i].append(b)
            b = []
            j += 1    
        j = 0    
        i += 1
    
    # Create get rank button 
    calcbtn = Button(window, text="get rank", fg="red", command=lambda: calc_rank(a))
    calcbtn.place(x=235, y=400)
           

# Create generate matrix button
gmbtn = Button(window, text="generate matrix", fg="red", command=create_matrix)
gmbtn.place(x=300, y=25)

# Run window
window.mainloop()