from tkinter import *
li=[]

def option(x):
    operators = list('+-*/')
    if x in range(0,10):
        str_x = str(x)
        li.append(str_x)
        temp = ''.join(li)
    
    elif x  in operators:
        li.append(x)
        temp = ''.join(li)
        if li[-1] in operators and li[-2] in operators:
            del li[-2]
            temp = ''.join(li)
    
    elif x in ['del','=','C','%','.']:
        if x == 'del':
            if len(li)==0:
                pass
            elif len(li)==1:
                ind = str(li[0]).split()
                del ind[-1]
                temp = ''.join(ind)
            else:
                del li[-1]
                temp = ''.join(li)
        
        elif x == '=':
            temp = ''.join(li)
            temp = eval(temp)
            li.clear()
            li.append(str(temp))
        
        elif x == 'C':
            li.clear()
            temp = '0'

        elif x =='%':
            temp = ''.join()
            while operators in temp:
                for i in operators:
                    ind = li.index(i)
                    del li[ind]
            
        
        else:
            li.append(x)
            temp = ''.join(li)
    output_screen.config(text=temp)
    print(li)
    return

root = Tk()
root.title('Calculator')
root.geometry('400x550')
root.config(bg='#d8f9ff')
root.resizable(False,False)
output="0"
output_screen = Label(root,text=output, font=(500),
                      cursor="xterm",anchor="se",
                      width=40+2,height=2,
                      bg="white",fg="black")
output_screen.grid(row=0,columnspan=4,pady=20)

Button(root,text='7',width=10,height=4,cursor="hand2",command= lambda:option(7)).grid(row=1,column=0)
Button(root,text='8',width=10,height=4,cursor="hand2",command= lambda:option(8)).grid(row=1,column=1)
Button(root,text='9',width=10,height=4,cursor="hand2",command= lambda:option(9)).grid(row=1,column=2)
Button(root,text='+',width=10,height=4,cursor="hand2",command= lambda:option('+')).grid(row=1,column=3,pady=10)

Button(root,text='4',width=10,height=4,cursor="hand2",command= lambda:option(4)).grid(row=2,column=0)
Button(root,text='5',width=10,height=4,cursor="hand2",command= lambda:option(5)).grid(row=2,column=1)
Button(root,text='6',width=10,height=4,cursor="hand2",command= lambda:option(6)).grid(row=2,column=2)
Button(root,text='-',width=10,height=4,cursor="hand2",command= lambda:option('-')).grid(row=2,column=3,pady=10)

Button(root,text='1',width=10,height=4,cursor="hand2",command= lambda:option(1)).grid(row=3,column=0)
Button(root,text='2',width=10,height=4,cursor="hand2",command= lambda:option(2)).grid(row=3,column=1)
Button(root,text='3',width=10,height=4,cursor="hand2",command= lambda:option(3)).grid(row=3,column=2)
Button(root,text='x',width=10,height=4,cursor="hand2",command= lambda:option('*')).grid(row=3,column=3,pady=10)

Button(root,text='.',width=10,height=4,cursor="hand2",command= lambda:option('.')).grid(row=4,column=0)
Button(root,text='0',width=10,height=4,cursor="hand2",command= lambda:option(0)).grid(row=4,column=1)
Button(root,bitmap='error',width=80-6,height=60+2, cursor="hand2",command= lambda:option('del')).grid(row=4,column=2)
Button(root,text='=',width=10,height=4,cursor="hand2",command= lambda:option('=')).grid(row=4,column=3,pady=10)

Button(root,text='/',width=10,height=4,cursor="hand2",command= lambda:option('/')).grid(row=5,column=0)
Button(root,text='%',width=10,height=4,cursor="hand2",command= lambda:option('%')).grid(row=5,column=1)
Button(root,text='C',width=10,height=4,cursor="hand2",command= lambda:option('C')).grid(row=5,column=2)
root.mainloop()