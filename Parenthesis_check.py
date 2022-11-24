
from tkinter import *
from tkinter import filedialog

def Balanced(str):
    #Stack for storing opening Brackets
    stack=[]
    #Loop for checking String
    for char in str:
        if char=='{' or char=='[' or char=='(' :
            stack.append(char)
        elif char=='<' or char=='>':
            if len(stack)==0:

                return True
        elif char=='}' or char==')' or char==']':
            if len(stack)==0:
                return False
            top_element=stack.pop()
            if not Compare(top_element,char):
                return False
    if len(stack)!=0:
        return False
    return True
def Compare(opening , closing):
    if opening=='(' and closing==')':
        return True
    if opening =='[' and closing==']':
        return True
    if opening=='{' and closing=='}':
        return True
    if opening=='(' and (closing =="<"  or closing=='>'):
        return True
    if opening =='<' and closing=='>':
        return True

    else:
        return False
def pickfile_and_Analyze():
    filename=filedialog.askopenfilename(initialdir="/",
                                        title="Select a Java File",
                                        filetypes=(("javax files","*.java*"),("all files","*.*")))
    textfield.configure(text="File Opened: "+filename)
    #return filename

    filenam=open(filename,'r')

    content=filenam.read()
    #print(content)




    if Balanced(content)==True:
        lab1.configure(text="Java file Nested Correctly")
    else:
        lab1.configure(text="Java File Not Nested Correctly")
    filenam.close()



top=Tk()

top.geometry("500x500")
frame1=Frame(top,highlightbackground="blue",highlightthickness=2)
frame1.pack(fill=BOTH)
frame1.pack(padx=20,pady=20)


lbl=Label(frame1,text="Braces Debugger")
lbl.grid(row=1,column=2)

textfield=Label(frame1,text="No File Browsed",fg="green")
textfield.grid(row=3,column=2)


lab=Label(frame1,text="Results:")
lab.grid(row=5,column=1)

lab1=Label(frame1,text="")
lab1.grid(row=5,column=2)


btn=Button(frame1,text="Upload File",command=pickfile_and_Analyze,fg="blue",activebackground="blue")
btn.grid(row=8,column=2)




#print(pickfile())
top.mainloop()


