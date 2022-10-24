from db import Db


class listarPalpites:
    def palpites(self):
        with Db() as db:
            lista_ids = db.select_match()
        
        self.times = []
        self.resultados = []
        self.ids_terminados = []
        for jogo in range(len(lista_ids)):
            game = (self.consultar.jogos_completos(lista_ids[jogo][0]))
            if (game['match']['status']) == 'FINISHED':
                self.resultados.append(game['match']['score']['fullTime']['homeTeam'])
                self.resultados.append(game['match']['score']['fullTime']['awayTeam'])

                self.times.append(game['match']['homeTeam']['name'])
                self.times.append(game['match']['awayTeam']['name'])

                self.ids_terminados.append(game['match']['id'])
            else:
                pass
        
        self.palpites_users = []
        for id in self.ids_terminados:
            with Db() as db:
                mostrar = db.show_palpites(id)
                self.palpites_users.append(mostrar)