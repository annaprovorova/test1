import tkinter

def print_hello(event):
    #print (dir(event))
    #print(event.keycode)
    print(event.num)
    print(event.x, event.y)
    print(event.x_root, event.y_root)
    me = event.widget
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('2!')
    else:
        raise ValueError()

root = tkinter.Tk()

button1 = tkinter.Button(root, text = "OK") #кнопка
button1.bind("<Button>", print_hello)
button1.pack()

button2 = tkinter.Button(root, text = "OK") #кнопка
button2.bind("<Button>", print_hello)
button2.pack()

root.mainloop() #создание окошка
