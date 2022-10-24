from tkinter import *
from tkinter import ttk


class Pre_palpite():
    def campeonatos(self):
        root = Tk()
        root.geometry('400x250+200+100')
        root.title('Escolher campeonato')

        campeonatos = [['Champions League', 2001], ['Premier League', 2021], ['Brasileirão', 2013], ['La liga', 2014]]

        Label(root, text='Escolha um campeonato', font=('Times', 20)).pack(pady=5)

        for campeonato in campeonatos:
            id = campeonato[1]
            btn_camp = Button(root, text=campeonato[0], command=lambda id=id: self.trocarJanela(root, 'pessoas()', id_camp=id)).pack(pady=2)
            Label()
        
        frameBottom = Frame(root,width=300,height=30)
        frameBottom.pack(side="bottom")
        frameBottom.pack_propagate(0)

        Button(frameBottom, text='Voltar', command=lambda : self.trocarJanela(root, 'menu_inicial()')).pack(side='left')

    def pessoas(self):
        root = Tk()
        root.geometry('200x200+200+100')
        root.title('Escolher palpiteiros')

        frame1 = Frame(root, width=100,height=30)
        frame1.pack()
        frame1.pack_propagate(1)

        Label(frame1, text='Quantos jogadores:').pack(side='left')

        t = ttk.Combobox(frame1, values=[1,2,3,4,5], width=3)
        t.pack(side='right')

        #quando for selecionado
        t.bind("<<ComboboxSelected>>", lambda x: criar_entry(t.get()))

        frame2 = Frame(root)
        frame2.pack()

        frameError = Frame(root)
        frameError.pack()

        frameBottom = Frame(root,width=250,height=30)
        frameBottom.pack(side="bottom")
        frameBottom.pack_propagate(0)

        Button(frameBottom, text='Voltar', command=lambda : self.trocarJanela(root, 'campeonatos()')).pack(side='left')

        def criar_entry(num):
            [widget.destroy() for widget in frame2.grid_slaves()]
            
            try:
                frameError.pack_slaves()[0].destroy()            
            except:
                pass

            row = 0
            for c in range(int(num)):
                Label(frame2, text="Nome:").grid(column=0, row=row)

                e1 = Entry(frame2)
                e1.grid(column=1, row=row)
                e1.bind('<Return>', lambda x: autenticar_entry())

                row +=1
            try:
                self.buttonPalpitar.destroy()
                print()
            except:
                pass
            finally:
                self.buttonPalpitar = Button(frameBottom, text='Palpitar', command=lambda : autenticar_entry())
                self.buttonPalpitar.pack(side='right')
            global labelError
            labelError = Label(frameError, text="Preencha todos os campos", fg='red')
            labelError.pack()
            labelError.pack_forget()

            
        
        def autenticar_entry():
            entrys = []
            [entrys.append(entry.get()) for entry in frame2.grid_slaves() if str(type(entry)) == "<class 'tkinter.Entry'>"]
            
            preenchido = True

            for campo in entrys:
                if campo == '':
                    preenchido = False
            
            if preenchido:
                entrys.reverse()
                
                self.nomes.clear()

                [self.nomes.append(nome) for nome in entrys]

                self.trocarJanela(root, 'palpite()')
            else:
                labelError.pack()
            
            
