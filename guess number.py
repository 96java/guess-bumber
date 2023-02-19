from tkinter import *
from random import randint
from tkinter.messagebox import askyesno

window = Tk()
LARGE_FONT = ("Verdana", 12)
window.geometry("400x400")
window.configure(bg = '#ce9e75')
var = IntVar()
c = randint(1, 100)
chance = 6

def check_num( event):
    global chance
    n = var.get()
    #c = clicked(n)
    try:
        print(c)
        a = int(entrer.get())
        print(a)

        if chance == 1:
            lab1['text'] = f'dommage vous avez perdu cliker sur <<valider>> pour reprendre'
            lose()
            entrer.configure(state=DISABLED)

        else:

            if a > c and chance > 0:
                chance -= 1
                lab['text'] = f'il vous reste : {chance} chances'
                lab1['text'] = f'le nombre mystère est inferieur à {a}'
                print(f'le nombre mystère est inferieur à {a}')
                print(f'vous juste : {chance} chances')


            elif a < c and chance > 0:
                chance -= 1
                lab['text'] = f'il vous reste : {chance} chances'
                lab1['text'] = f'le nombre mystère est supperieur à {a}'
                print(f'le nombre mystère est supperieur à {a}')
                print(f'vous juste : {chance} chances')


            elif a == c:
                lab1['text'] = f'le nombre mystère est bien {a} Bravo! nouvelle valeur active'
                print(f'le nombre mystère est bien {a} Bravo!')
                win()
    except:

        lab1['text'] = f"s'il vous plait entrer les valeurs en chiffe"

    entrer.delete(0, END)
def win():
    a = var.get()
    ans = askyesno(title = 'continu game', message = 'Bravo vouler vous continuer ?')
    if ans:
        clicked(a)
        chance = 6
        lab['text'] =f'vous avez juste : {chance} chances'
        entrer.configure(state = NORMAL)

    else:
        entrer.configure(state = DISABLED)
def lose():
    ans = askyesno(title = 'restart game', message = 'dommage vous avez perdu\n Vouler vous reprendre?')
    if ans:
        clicked()
        chance = 6
        lab['text'] =f'vous avez juste : {chance} chances'
        entrer.configure(state = NORMAL)
    else:
        entrer.configure(state = DISABLED)
def clicked(value):
    print(var.get())
    global c
    if value == 1:
        entrer.configure(state=NORMAL)
        print('vous optez pour le niveau facile ')
        label ['text']= 'entrer un nombre entre 1 et 50'
        c = randint(1, 50)


    elif value == 2:
        entrer.configure(state=NORMAL)
        print('vous optez pour le niveau moyen ')
        label['text'] = 'entrer un nombre entre 1 et 100'
        c = randint(1, 100)


    elif value == 3:
        entrer.configure(state=NORMAL)
        print('vous optez pour le niveau difficile ')
        label['text'] = 'entrer un nombre entre 1 et 200'
        c = randint(1, 200)
    print(c)
    return c
def valider(self):
    n = randint(1, 100)
    return n

label = Label(window, text="Page App!!!", font=LARGE_FONT,bg = '#ce9e75')
label.pack(pady=10,padx=10)

label = Label(window, text="choisicez votre niveau ", font=LARGE_FONT,bg = '#ce9e75')
label.pack(pady=10,padx=10)

Radio1 = Radiobutton(window, text = 'facile', variable = var, value = 1,bg = '#ce9e75', font=('Forte', 12),
                         command = lambda : clicked(var.get()))
Radio2 = Radiobutton(window, text='moyen', variable=var, value=2,bg = '#ce9e75', font=('Forte', 12),
                     command=lambda: clicked(var.get()))
Radio3 = Radiobutton(window, text='difficile', variable=var, value=3,bg = '#ce9e75', font=('Forte', 12),
                     command=lambda: clicked(var.get()))

Radio1.place(relx=0.1, y= 100)
Radio2.place(relx = 0.4, y= 100)
Radio3.place(relx=0.7, y= 100)

entrer = Entry(window, relief = RAISED)
entrer.place( x = 20, y = 150)
entrer.bind('<Return>', check_num)
entrer.configure(state = DISABLED)

lab = Label(window, text=f'vous avez juste : {chance} chances', bg='#ce9e75', font=LARGE_FONT)
lab.place(x=150, y=145)

lab1 = Label(window, text=f'', bg='#ce9e75', font=LARGE_FONT)
lab1.place(relx=0.1, y=300)

button0 = Button(window, text="RECOMMENCER", padx=5, pady=5,
                      command=lambda: valider)
button0.place(x=20, y=200)


window.mainloop()


lab.place(x=150, y=145)

lab1 = Label(window, text=f'', bg='#ce9e75', font=LARGE_FONT)
lab1.place(relx=0.1, y=300)

button0 = Button(window, text="RECOMMENCER", padx=5, pady=5,
                      command=lambda: valider)
button0.place(x=20, y=200)


window.mainloop()

