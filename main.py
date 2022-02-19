# Import libraries
from tkinter import *
from tkinter import messagebox

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

# Create nested list
a11 = Entry(window, font=('verdana', 12))
a12 = Entry(window, font=('verdana', 12))
a13 = Entry(window, font=('verdana', 12))
a14 = Entry(window, font=('verdana', 12))
a15 = Entry(window, font=('verdana', 12))
a16 = Entry(window, font=('verdana', 12))
a17 = Entry(window, font=('verdana', 12))
a18 = Entry(window, font=('verdana', 12))
a19 = Entry(window, font=('verdana', 12))
a21 = Entry(window, font=('verdana', 12))
a22 = Entry(window, font=('verdana', 12))
a23 = Entry(window, font=('verdana', 12))
a24 = Entry(window, font=('verdana', 12))
a25 = Entry(window, font=('verdana', 12))
a26 = Entry(window, font=('verdana', 12))
a27 = Entry(window, font=('verdana', 12))
a28 = Entry(window, font=('verdana', 12))
a29 = Entry(window, font=('verdana', 12))
a31 = Entry(window, font=('verdana', 12))
a32 = Entry(window, font=('verdana', 12))
a33 = Entry(window, font=('verdana', 12))
a34 = Entry(window, font=('verdana', 12))
a35 = Entry(window, font=('verdana', 12))
a36 = Entry(window, font=('verdana', 12))
a37 = Entry(window, font=('verdana', 12))
a38 = Entry(window, font=('verdana', 12))
a39 = Entry(window, font=('verdana', 12))
a41 = Entry(window, font=('verdana', 12))
a42 = Entry(window, font=('verdana', 12))
a43 = Entry(window, font=('verdana', 12))
a44 = Entry(window, font=('verdana', 12))
a45 = Entry(window, font=('verdana', 12))
a46 = Entry(window, font=('verdana', 12))
a47 = Entry(window, font=('verdana', 12))
a48 = Entry(window, font=('verdana', 12))
a49 = Entry(window, font=('verdana', 12))
a51 = Entry(window, font=('verdana', 12))
a52 = Entry(window, font=('verdana', 12))
a53 = Entry(window, font=('verdana', 12))
a54 = Entry(window, font=('verdana', 12))
a55 = Entry(window, font=('verdana', 12))
a56 = Entry(window, font=('verdana', 12))
a57 = Entry(window, font=('verdana', 12))
a58 = Entry(window, font=('verdana', 12))
a59 = Entry(window, font=('verdana', 12))
a61 = Entry(window, font=('verdana', 12))
a62 = Entry(window, font=('verdana', 12))
a63 = Entry(window, font=('verdana', 12))
a64 = Entry(window, font=('verdana', 12))
a65 = Entry(window, font=('verdana', 12))
a66 = Entry(window, font=('verdana', 12))
a67 = Entry(window, font=('verdana', 12))
a68 = Entry(window, font=('verdana', 12))
a69 = Entry(window, font=('verdana', 12))
a71 = Entry(window, font=('verdana', 12))
a72 = Entry(window, font=('verdana', 12))
a73 = Entry(window, font=('verdana', 12))
a74 = Entry(window, font=('verdana', 12))
a75 = Entry(window, font=('verdana', 12))
a76 = Entry(window, font=('verdana', 12))
a77 = Entry(window, font=('verdana', 12))
a78 = Entry(window, font=('verdana', 12))
a79 = Entry(window, font=('verdana', 12))
a81 = Entry(window, font=('verdana', 12))
a82 = Entry(window, font=('verdana', 12))
a83 = Entry(window, font=('verdana', 12))
a84 = Entry(window, font=('verdana', 12))
a85 = Entry(window, font=('verdana', 12))
a86 = Entry(window, font=('verdana', 12))
a87 = Entry(window, font=('verdana', 12))
a88 = Entry(window, font=('verdana', 12))
a89 = Entry(window, font=('verdana', 12))
a91 = Entry(window, font=('verdana', 12))
a92 = Entry(window, font=('verdana', 12))
a93 = Entry(window, font=('verdana', 12))
a94 = Entry(window, font=('verdana', 12))
a95 = Entry(window, font=('verdana', 12))
a96 = Entry(window, font=('verdana', 12))
a97 = Entry(window, font=('verdana', 12))
a98 = Entry(window, font=('verdana', 12))
a99 = Entry(window, font=('verdana', 12))

matrix = [[a11, a12, a13, a14, a15, a16, a17, a18, a19],
          [a21, a22, a23, a24, a25, a26, a27, a28, a29],
          [a31, a32, a33, a34, a35, a36, a37, a38, a39],
          [a41, a42, a43, a44, a45, a46, a47, a48, a49],
          [a51, a52, a53, a54, a55, a56, a57, a58, a59],
          [a61, a62, a63, a64, a65, a66, a67, a68, a69],
          [a71, a72, a73, a74, a75, a76, a77, a78, a79],
          [a81, a82, a83, a84, a85, a86, a87, a88, a89],
          [a91, a92, a93, a94, a95, a96, a97, a98, a99]]

def calc_rank(matrix, m, n):
    if(m == n):
        error = False
        i = 0
        j = 0
        while i < m:
            while j < n:
                if(isinstance(matrix[i][j].get(), float) != True):
                    error = True
                j += 1
            j = 0
            i += 1
        if(error):
            messagebox.showerror(title='Invalid matrix', message='Please make sure all entered values are numbers')
            
    else: 
        messagebox.showerror(title='Invalid matrix', message='Please enter the dimentions of a square matrix')

def create_matrix(matrix):
    # Create matrix
    m = int(rows.get())
    n = int(columns.get())
    i = 0
    j = 0

    while i < m:
        while j < n:
            # Create input
            matrix[i][j].place(width=20, height=24, x=30+j*40, y=105+i*40)
            j += 1    
        j = 0    
        i += 1
    
    # Create get rank button 
    calcbtn = Button(window, text="get rank", fg="red", command=lambda: calc_rank(matrix, m, n))
    calcbtn.place(x=235, y=400)
           

# Create generate matrix button
gmbtn = Button(window, text="generate matrix", fg="red", command=lambda: create_matrix(matrix))
gmbtn.place(x=300, y=25)

# Run window
window.mainloop()
