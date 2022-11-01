from db import Db


class listarPalpites:
    def palpites(self):
        with Db() as db:
            lista_ids = db.select_match()

        self.times = []
        self.resultados = []
        self.ids_terminados = []
        self.horarios_jogos = []
        for jogo in range(len(lista_ids)):
            game = (self.consultar.jogos_completos(lista_ids[jogo][0]))
            if (game['match']['status']) == 'FINISHED':
                self.resultados.append(game['match']['score']['fullTime']['homeTeam'])
                self.resultados.append(game['match']['score']['fullTime']['awayTeam'])
            else:
                print('nao acabou')
                self.resultados.append('')
                self.resultados.append('')
            
            self.times.append(game['match']['homeTeam']['name'])
            self.times.append(game['match']['awayTeam']['name'])
            if lista_ids[jogo][1] is None:
                print('busquei na api')
                self.horarios_jogos.append(self.converter_horario(game['match']['utcDate']))
            else:
                print('peguei no bd')
                self.horarios_jogos.append(lista_ids[jogo][1])

            self.ids_terminados.append(game['match']['id'])
        
        self.palpites_users = []
        for id in self.ids_terminados:
            with Db() as db:
                mostrar = db.show_palpites(id)
                self.palpites_users.append(mostrar)
