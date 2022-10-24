from tkinter import *

from db import Db

from windows.tkscrolledframe import ScrolledFrame


class VerPalpite():
    
    def calcular_pontos(self, r_casa, r_fora, p_casa, p_fora):
        if p_casa == r_casa:
            if p_fora == r_fora:
                return 3
            else:
                return 0
        elif p_casa == r_fora:
            if p_fora == r_casa:
                return 1
            else:
                return 0
        else:
            return 0
            
    def ver_palpite(self):
        self.palpites()
        root = Tk()
        widthWin = 600
        widthHei = 200
        root.geometry(f'{widthWin}x{widthHei}+200+100')
        root.title('Palpites Feitos')
        
        
        sf = ScrolledFrame(root, width=widthWin, height=widthHei-80)
        sf.pack(side="top", expand=1, fill="both")

        sf.bind_arrow_keys(root)
        sf.bind_scroll_wheel(root)
        inner_frame = sf.display_widget(Frame)
        
        frame1 = Frame(inner_frame)
        frame1.pack(padx=20)
        row = 0
        self.buttons = {}
        for match in range(0, len(self.resultados)//2):
            r_casa = self.resultados[match*2]
            r_fora = self.resultados[match*2+1]
            #time de casa
            Label(frame1, text=f'{self.times[match*2]}', font=('Times',14)).grid(column=0, row=row, pady=(2,0), sticky=E)
            Label(frame1, text=f'{r_casa}', font=('Times',14)).grid(column=1, row=row, pady=(2,0))

            Label(frame1, text='x', font=('Times',14)).grid(column=2, row=row, pady=(2,0))
            #time de fora
            Label(frame1, text=f'{r_fora}', font=('Times',14)).grid(column=3, row=row, pady=(2,0))
            Label(frame1, text=f'{self.times[match*2+1]}', font=('Times',14)).grid(column=4, row=row, pady=(2,0), sticky=W)

            id = self.ids_terminados[match]
            deletar_button = Button(frame1, text='Apagar palpite', command=lambda id=id, row=row:deletar_jogo(id,row), bg='red', fg='black')
            deletar_button.grid(column=5, row=row)
            self.buttons[row] = deletar_button
            row += 1

            for palpite in range(len(self.palpites_users[match])):
                p_casa = self.palpites_users[match][palpite][2]
                p_fora = self.palpites_users[match][palpite][3]

                #nome
                Label(frame1, text=self.palpites_users[match][palpite][1]).grid(column=0, row=row)
                #palpite time de casa
                Label(frame1, text=self.palpites_users[match][palpite][2]).grid(column=1, row=row)
                Label(frame1, text='x').grid(column=2, row=row)
                #palpite time de fora
                Label(frame1, text=self.palpites_users[match][palpite][3]).grid(column=3, row=row)
                #pontos
                Label(frame1, text=self.calcular_pontos(r_casa, r_fora, int(p_casa), int(p_fora))).grid(column=4, row=row)
                row += 1
        
        frameBottom = Frame(root, width=widthWin, height= 30)
        frameBottom.pack()
        frameBottom.pack_propagate(0)

        btnBack = Button(frameBottom, text='Voltar', command=lambda:self.trocarJanela(root, 'menu_inicial()'))
        btnBack.pack(side='left')

        btnDelete = Button(frameBottom, text='Apagar tudo', bg='red', command=lambda:apagar_tudo())
        btnDelete.pack(side='right')

        def apagar_tudo():
            with Db() as db:
                db.delete()
            self.trocarJanela(root, 'menu_inicial()')

        def deletar_jogo(id,row):
            with Db() as db:
                db.delete_palpite(id)
            
            self.buttons[row].destroy()
            del self.buttons[row]

            Label(frame1, text='Palpite apagado', font=('Times',12)).grid(column=5, row=row, pady=(2,0))
