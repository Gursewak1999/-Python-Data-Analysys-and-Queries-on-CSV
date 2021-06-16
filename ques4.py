import csv
from tkinter import *
import tkinter as tk
import os;

window=tk.Tk()
window.title("CSE1 CLASS SEM 4")

un=Label(window,text="QUERIES ON CSE1 CLASS SEM 4",font=('poppins',15),fg='red',bg='yellow')
un.grid(row=0,column=0)

rows = []
columns = []

def clear():
    print("\n"*5)

with open("data/class_data.csv",'r') as csvfile:
        csvreader=csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
def query1():
    
    for i in rows:
        print(i[3])
    print("total number of rows %d"%(csvreader.line_num))
    clear()
   
def query4():
    
    for i in rows:
        if i[3] not in (None,'') and i[7] not in (None,''):
            print(i[3]+" "*(22-len(i[3])),"SCORED",i[7],"! cgpa !")
    print("total number of rows %d"%(csvreader.line_num))
    clear()
    
def query2():
    
    print("STUDENTS BELONGING TO AMRITSAR")    
    for i in rows:
            if i[3] not in (None,'') and i[5] not in (None,''):
                if i[5]=="Amritsar":
                    print(i[3])
    print("STUDENTS BELONGING TO BIHAR")    
    for i in rows:
            if i[3] not in (None,'') and i[5] not in (None,''):
                if i[5]=="Bihar":
                    print(i[3])
    print("STUDENTS BELONGING TO TARAN TARAN")    
    for i in rows:
            if i[3] not in (None,'') and i[5] not in (None,''):
                if i[5]=="TaranTaran":
                    print(i[3])
    print("STUDENTS BELONGING TO LUDHIANA")    
    for i in rows:
        if i[3] not in (None,'') and i[5] not in (None,''):
            if i[5]=="Ludhiana":
                print(i[3])
    print("STUDENTS BELONGING TO Batala")    
    for i in rows:
        if i[3] not in (None,'') and i[5] not in (None,''):
            if i[5]=="Batala":
                print(i[3])            
    clear()
def query5():  
    for i in rows:
        if i[3] not in (None,'') and i[4] not in (None,''):
            if i[3].startswith('A') and i[4].endswith('2000'):
                print(i[3])

    clear()      
def query3():
    for i in rows:
        if i[5] not in (None,'') and i[4] not in (None,''):
            if i[5]=='Amritsar' and i[4].endswith('2000'):
                print(i[3])
    clear()
    
btn1 = tk.Button(window, text = "List All Students", fg = "black",command = query1)
btn2 = tk.Button(window, text = "List Students City-wise", fg = "black",command = query2)
btn3 = tk.Button(window, text = "List Students City-wise (year being 2000)", fg = "black",command = query3)
btn4 = tk.Button(window, text = "List Students CGPA", fg = "black",command = query4)
btn5 = tk.Button(window, text = "List Students with name starting from (say A)", fg = "black",command = query5)
btn1.grid(row=6,column=0)
btn2.grid(row=7,column=0)
btn3.grid(row=8,column=0)
btn4.grid(row=9,column=0)
btn5.grid(row=10,column=0)
window.mainloop()
csvfile.close()
