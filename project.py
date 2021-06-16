import csv
from tkinter import *

window=Tk()
window.title("Dataset Project")

un=Label(window,text="QUERIES ON Dataset",font=('poppins',15),fg='red',bg='yellow')
un.grid(row=0,column=0)

rows = []

with open("students.csv") as dataset:
    csv_read = csv.reader(dataset, delimiter=',')
    i=0
    for row in csv_read:
        if i!=0:
            rows.append(row)
        i=i+1
    
#number of males and females and sex Ratio
def fun1():
    
    maleC=0
    femaleC=0
    for row in rows:
        if row[11]=="Male":
            maleC=maleC+1
        else:
            femaleC=femaleC+1
    print("---------:Students according to their Sex:---------")
    print("Number of males in class: ",maleC)
    print("Number of females in class: ",femaleC)
    print("Sex Ratio in class: ",(float)(maleC/femaleC))
 
#number of students having back problems due to Backpack weight
def fun2():
    counterC=0
    for row in rows:
        if int(row[15])==1:
            counterC=counterC+1
    print("---------:Students having Back Problems:---------")
    print ('Number of students having back problems: ',counterC)
    print ('Percentage of students having back problems: ',(float) (counterC/len(rows)*100))
    
#number of students who prepared the test:
def fun3():
    counter=0
    for row in rows:
        if row[17]=="completed":
            counter=counter+1
    print("---------:Students having Prepared Test:---------")
    print ('Number of students having Prepared Test: ',counter)
    print ('Percentage of students having Prepared Test: ',(float)(counter/len(rows)*100))

#calculating number of students with different eye colour
def fun4():
    b=0
    bl=0
    h=0
    g=0
    for row in rows:
        if row[10]=="Brown":
            b=b+1
        elif row[10]=="Blue":
            bl=bl+1
        elif row[10]=="Hazel":
            h=h+1
        elif row[10]=="Green":
            g=g+1
    print("---------:Students having Different eye colour:---------")
    print("Brown: ",b)
    print("Blue: ",bl)
    print("Hazel: ",h)
    print("Green",g)

#calculating number of students with different hair color
def fun5():
    
    b=0
    bl=0
    h=0
    g=0
    for row in rows:
        if row[9]=="Black":
            b=b+1
        elif row[9]=="Brown":
            bl=bl+1
        elif row[9]=="Red":
            h=h+1
        elif row[9]=="Blond":
            g=g+1
    print("---------:Students having Different hair colour:---------")
    print("Black: ",b)
    print("Brown: ",bl)
    print("Red: ",h)
    print("Blond",g)

#sorting students using backpack weight
def fun6():
    lim1=0
    lim2=0
    lim3=0
    #light: 0-10
    #normal: 11-16
    #high: >16
    for row in rows:
        i=int(row[12])
        if(i>16):
            lim3=lim3+1
        elif(i>10):
            lim2=lim2+1
        else:
            lim1=lim1+1
            
    print("---------:Students having Backpack weight:---------")
    print("Light: ",lim1)
    print("Normal: ",lim2)
    print("Heavy: ",lim3)

#sorting students according to their weight
def fun7():
    lim1=0
    lim2=0
    lim3=0
    #light: 0-10
    #normal: 11-16
    #high: >16
    for row in rows:
        i=int(row[13])
        if(i>170):
            lim3=lim3+1
        elif(i>140):
            lim2=lim2+1
        else:
            lim1=lim1+1
            
    print("---------:Students According to their Weight:---------")
    print("Light: ",lim1)
    print("Normal: ",lim2)
    print("Heavy: ",lim3)

#calculating number ofstudents having good math score
def fun8():
    lim1=0
    lim2=0
    lim3=0
    #light: 0-10
    #normal: 11-16
    #high: >16
    for row in rows:
        i=int(row[18])
        if(i>90):
            lim3=lim3+1
        elif(i>60):
            lim2=lim2+1
        else:
            lim1=lim1+1
            
    print("---------:Students According to their Math Score:---------")
    print("Excellent: ",lim1)
    print("Good: ",lim2)
    print("Average: ",lim3)
    
#calculating number ofstudents having good reading skills
def fun9():
    lim1=0
    lim2=0
    lim3=0
    #light: 0-10
    #normal: 11-16
    #high: >16
    for row in rows:
        i=int(row[19])
        if(i>90):
            lim3=lim3+1
        elif(i>60):
            lim2=lim2+1
        else:
            lim1=lim1+1
            
    print("---------:Students According to their reading skills:---------")
    print("Excellent: ",lim1)
    print("Good: ",lim2)
    print("Average: ",lim3)
    
#calculating number ofstudents having good writing score
def fun10():
    lim1=0
    lim2=0
    lim3=0
    #light: 0-10
    #normal: 11-16
    #high: >16
    for row in rows:
        i=int(row[20])
        if(i>90):
            lim3=lim3+1
        elif(i>60):
            lim2=lim2+1
        else:
            lim1=lim1+1
            
    print("---------:Students According to their writing score:---------")
    print("Excellent: ",lim1)
    print("Good: ",lim2)
    print("Average: ",lim3)
    

btn1 = Button(window, text = "Students according to their Sex", fg = "black",command = fun1)
btn2 = Button(window, text = "Students having Back Problems", fg = "black",command = fun2)
btn3 = Button(window, text = "Students having Prepared Test", fg = "black",command = fun3)
btn4 = Button(window, text = "Students having Different eye colour", fg = "black",command = fun4)
btn5 = Button(window, text = "Students having Different hair colour", fg = "black",command = fun5)
btn6 = Button(window, text = "Students having Backpack weight", fg = "black",command = fun6)
btn7 = Button(window, text = "Students According to their Weight", fg = "black",command = fun7)
btn8 = Button(window, text = "Students According to their Math Score", fg = "black",command = fun8)
btn9 = Button(window, text = "Students According to their reading skills", fg = "black",command = fun9)
btn10 = Button(window, text = "Students According to their writing score", fg = "black",command = fun10)
btn1.grid(row=2,column=0)
btn2.grid(row=3,column=0)
btn3.grid(row=4,column=0)
btn4.grid(row=5,column=0)
btn5.grid(row=6,column=0)
btn6.grid(row=7,column=0)
btn7.grid(row=8,column=0)
btn8.grid(row=9,column=0)
btn9.grid(row=10,column=0)
btn10.grid(row=11,column=0)
window.mainloop()
dataset.close()
