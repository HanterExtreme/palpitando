from tkinter import *

from db import Db

from windows.tkscrolledframe import ScrolledFrame


class Palpite:

    def palpite(self):
        root = Tk()
        widthWin = 600
        widthHei = 200
        root.geometry(f'{widthWin}x{widthHei}+200+100')
        
        frameName = Frame(root, width=widthWin, height= 30)
        frameName.pack()
        frameName.pack_propagate(0)

        self.nome = self.nomes[0]

        varNome = StringVar()
        varNome.set(f'Vez de {self.nome}')

        Label(frameName, textvariable= varNome, font=('Times',16)).pack()

        #criação do frame rolavel
        sf = ScrolledFrame(root, width=widthWin, height=widthHei-80)
        sf.pack(side="top", expand=1, fill="both")

        sf.bind_arrow_keys(root)
        sf.bind_scroll_wheel(root)

        inner_frame = sf.display_widget(Frame)

        #metodo que vai chamar a api e retornar a lista
        lista_jogos = self.listar_jogos(self.id_campeonato)

        altura = (len(lista_jogos) * 35) + 35
        frame1 = Frame(inner_frame, width=widthWin, height=altura)
        frame1.pack(padx=20)
        frame1.pack_propagate(0)

        self.stringVars = []
        [self.stringVars.append(StringVar()) for c in range(len(lista_jogos) * 2)]
        
        if len(lista_jogos) == 0:
            Label(frame1, text='Não há nenhum jogo nas proximas 2 semanas', fg='red', font=('Times',16)).pack()
        else:
            row = 0
            for jogo in lista_jogos:
                data = jogo[0]
                #data e hora
                Label(frame1, text=data).grid(column=0, row=row)
                #rodada
                Label(frame1, text=jogo[1]).grid(column=1, row=row)

                #time de casa
                Label(frame1, text=jogo[2]).grid(column=2, row=row, sticky=E)
                Entry(frame1, width=3, textvariable=self.stringVars[row*2]).grid(column=3, row=row)

                Label(frame1, text='X').grid(column=4, row=row, pady=5)
                #time de fora
                Entry(frame1, width=3, textvariable=self.stringVars[row*2+1]).grid(column=5, row=row)
                Label(frame1, text=jogo[3]).grid(column=6, row=row, sticky=W)

                id = jogo[4]
                Button(frame1, text='Palpitar', command=lambda id=id, row=row, data=data:autenticar_palpite(id,row, data)).grid(column=7, row=row)

                row+=1

        frameBack = Frame(root, width=widthWin, height= 30)
        frameBack.pack()
        frameBack.pack_propagate(0)
        
        btnBack = Button(frameBack, text='Voltar', command=lambda:self.trocarJanela(root, 'menu_inicial()'))
        btnBack.pack(side='left')

        btnNext = Button(frameBack, text='Proximo', command=lambda:proxima_pessoa())
        btnNext.pack(side='right')

        if len(self.nomes) == 1:
            btnNext['text'] = 'Finalizar'

        def proxima_pessoa():
            ProxIndice = self.nomes.index(self.nome) + 1

            #verifica se é a última pessoa
            if ProxIndice == len(self.nomes):
                self.trocarJanela(root, 'menu_inicial()')
            else:
                self.nome = self.nomes[ProxIndice]
                varNome.set(f'Vez de {self.nome}')

                [stringvar.set('') for stringvar in self.stringVars]
                try:
                    self.l_result.destroy()
                except:
                    pass

                #verifica se a próxima pessoa é a última
                if ProxIndice == len(self.nomes) - 1:
                    btnNext['text'] = 'Finalizar'
        
        def label_result(text, fg):
            try:
                self.l_result.destroy()
            except:
                pass
            finally:
                self.l_result = Label(frame1, text=text, fg=fg)
                self.l_result.grid(column= 8, row=self.row)

        def autenticar_palpite(id, c, data):
            self.row = c
            homeTeam = self.stringVars[c*2].get()
            awayTeam = self.stringVars[c*2+ 1].get()

            if awayTeam == '' or homeTeam == '':
                label_result('preencha os campos', 'red')
            else:
                #verifica se é somente números
                numeros = False
                try:
                    int(homeTeam)
                    int(awayTeam)
                    numeros = True
                except:
                    label_result('Somente numeros', 'red')

                if numeros:
                    with Db() as db:
                        #verifica se ja existe uma pessoa que palpitou nesse jogo
                        if db.select(f"WHERE match_id = '{id}' AND name = '{self.nome}'"):
                            print('update')
                            db.update(id, self.nome, homeTeam, awayTeam)
                        else:
                            print('add')
                            db.insert(id, self.nome, homeTeam, awayTeam, data)

                    label_result('Palpite feito!','green')

        root.mainloop()

    