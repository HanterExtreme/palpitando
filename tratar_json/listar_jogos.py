from datetime import date


class listarJogos():
    def converter_horario(self, utc):
        ano = utc[:4]
        mes = utc[5:7]
        dia = utc[8:10]
        
        horas = int(utc[11:13])
        horas = (horas + 24) - 3 if horas < 3 else horas - 3
        minutos = utc[14:16] 

        data = f'{dia}/{mes}/{ano} {horas}:{minutos}'
        return data

    def listar_jogos(self, id):
        id_competicao = id

        data_hoje = date.today()
        #1 semana
        data_futura = date.fromordinal(data_hoje.toordinal()+7)

        jogos_rodada = self.consultar.jogos_competicao(id_competicao, f'dateFrom={str(data_hoje)}&dateTo={str(data_futura)}&status=SCHEDULED')
        
        if jogos_rodada['count'] == 0:
            #2 semanas
            data_futura = date.fromordinal(data_hoje.toordinal()+14)
            jogos_rodada = self.consultar.jogos_competicao(id_competicao, f'dateFrom={str(data_hoje)}&dateTo={str(data_futura)}&status=SCHEDULED')
        
        todos_jogos = []
        lista_jogos = jogos_rodada['matches']

        for jogo in lista_jogos:
            jogo_lista = []
            jogo_lista.append(self.converter_horario(jogo['utcDate']))
            jogo_lista.append(jogo['matchday'])
            jogo_lista.append(jogo['homeTeam']['name'])
            jogo_lista.append(jogo['awayTeam']['name'])
            jogo_lista.append(jogo['id'])

            todos_jogos.append(jogo_lista)
        
        return todos_jogos
