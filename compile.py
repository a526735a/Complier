from tkinter import* 
iddi = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
opid  = {'+':1,'-':2,'<':3,'=':4}
bcode = {'line':10,'idd':11,'const':12,'if':13,'goto':14,'print':15,'stop':16,'op':17}
value = []
ifbool = False

def complie() :
    global ifbool
    bcodebox.delete(0.0,END)
    text = codebox.get("1.0",'end-1c')
    text = text.split('\n')
    for e in text :
        temp = e.split()
        for i in range(len(temp)) :
            if i == 0 :
                bcodebox.insert(END,str(bcode['line'])+' '+str(temp[i])+' ')
            elif temp[i] in iddi :
                bcodebox.insert(END,str(bcode['idd'])+' '+str(iddi[temp[i]])+ ' ')
            elif temp[i] in opid :
                bcodebox.insert(END,str(bcode['op'])+' '+str(opid[temp[i]])+' ')
            elif temp[i] == 'PRINT' :
                bcodebox.insert(END,str(bcode['print'])+' '+str(0)+ ' ')
            elif temp[i] == 'STOP':
                bcodebox.insert(END,str(bcode['stop'])+' '+str(0)+ ' ')
            elif temp[i] == 'GOTO':
                bcodebox.insert(END,str(bcode['goto'])+' '+str(temp[i+1])+' ')
                break
            elif temp[i] == 'IF' :
                bcodebox.insert(END,str(bcode['if'])+' '+str(0)+' ')
                ifbool = True
            else:
                if ifbool and i == len(temp)-1 :
                    bcodebox.insert(END,str(bcode['goto'])+' '+str(temp[i])+ ' ')
                    ifbool = False
                else :
                    bcodebox.insert(END,str(bcode['const'])+' '+str(temp[i])+' ')
        bcodebox.insert(END,'\n')             
    bcodebox.see(END)

def clear():
    codebox.delete(0.0,END)
    bcodebox.delete(0.0,END)

root = Tk()
root.title('Complier')
root.geometry('630x650')
root.configure(background = 'black')


combutton = Button(text = 'Complie!',bg = 'black',fg = 'light green',font = 'none 12 bold')
combutton["command"] = complie
combutton.grid(row = 2 , column = 1)
combutton = Button(text = 'Clear!',bg = 'black',fg = 'light green',font = 'none 12 bold')
combutton["command"] = clear
combutton.grid(row = 3 , column = 1)


codeins = Label(text = "Enter the Code :",bg= 'black',fg='light green',font = 'none 12 bold')
codeins.grid(row=0,column =0,sticky = W )
codebox = Text(width = 50 , height = 15,wrap =WORD,bg = 'grey')
codebox.grid(row = 1 ,column = 1,sticky = W)


bcodeins = Label(text = "Bcode :",bg = 'black' ,fg = 'light green',font = 'none 12 bold')
bcodeins.grid(row=4,column =0,sticky = W )
bcodebox = Text(width = 50 , height = 15,wrap =WORD,bg = 'grey')
bcodebox.grid(row = 5 ,column = 1,sticky = W)

root.grid_rowconfigure(2,minsize = 50)

root.mainloop()




