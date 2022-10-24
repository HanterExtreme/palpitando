import requests

class consulta_api():
    def __init__(self):
        self.api_base = 'http://api.football-data.org/v2/'
        self.headers = {'X-Auth-Token': '7f6e46464e7947af973449a40418e0e3'}

    def response(self, url):
        print(url)
        request = requests.get(url, headers=self.headers)
        json = request.json()
        try:
            temp = json['errorCode']
            print(json['message'], json['errorCode'])
        except:
            return json

    def competicao(self, id_competicao):
        url_api = f'{self.api_base}competitions/{id_competicao}'
        return self.response(url_api)

    def jogos_competicao(self, id_competicao, parametros = ''):
        url_api = f'{self.api_base}competitions/{id_competicao}/matches?{parametros}'
        return self.response(url_api)

    def jogos_completos(self, id_match):
        url_api = f'{self.api_base}matches/{id_match}'
        return self.response(url_api)
        