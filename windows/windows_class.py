from windows.menuinicial import menuinicial
from windows.palpite import Palpite
from windows.ver_palpite import VerPalpite
from windows.pre_palpite import Pre_palpite
from tratar_json.tratamento_base import tratar_json
from api import consulta_api

class Windows(menuinicial, Palpite, VerPalpite, tratar_json, Pre_palpite):
    def __init__(self):
        self.nome = ''
        self.nomes = []
        self.consultar = consulta_api()
        self.menu_inicial()
    
    def trocarJanela(self, root, proxJanela, id_camp=''):
        root.destroy()
        if id_camp:
            self.id_campeonato = id_camp
        eval(f"self.{proxJanela}")
    