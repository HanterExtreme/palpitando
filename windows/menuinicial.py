from tkinter import *

class menuinicial:
    def menu_inicial(self):
        root = Tk()
        root.geometry('400x150+200+100')
        root.title('Menu inicial')

        l1 = Label(root, text='Menu Inicial', font=('Times',30))
        l1.pack()

        frameButtons = Frame(root)
        frameButtons.pack()

        b1 = Button(frameButtons, text='Palpitar', font=('roboto', 12), command=lambda:self.trocarJanela(root, 'campeonatos()'))
        b1.pack(side='left')
        b2 = Button(frameButtons, text='Ver palpites', font=('roboto', 12), command=lambda:self.trocarJanela(root, 'ver_palpite()'))
        b2.pack(side='left', padx=20, pady=20)

        root.mainloop()