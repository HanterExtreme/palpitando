import requests


class consulta_api():
    def __init__(self):
        self.tokens = ['6981f38aa16147e7a43215c893be184f', '7f6e46464e7947af973449a40418e0e3', 
                       '8b907dc83bad45b5acc1ede8a1d3c33a', '359d518f5e7346daa9ecb1fe50efb006']
        self.api_base = 'http://api.football-data.org/v2/'
        self.headers = {'X-Auth-Token': '7f6e46464e7947af973449a40418e0e3'}

    def response(self, url):
        print(url)
        request = requests.get(url, headers=self.headers)
        json = request.json()
        try:
            temp = json['errorCode']
            for _ in range(len(self.tokens)):
                if int(temp) == 429:
                    index_token_atual = self.tokens.index(self.headers['X-Auth-Token'])
                    print(index_token_atual)
                    if index_token_atual == len(self.tokens) - 1:
                        self.headers['X-Auth-Token'] = self.tokens[0]
                    else:
                        self.headers['X-Auth-Token'] = self.tokens[index_token_atual + 1]
                request = requests.get(url, headers=self.headers)
                json = request.json()
                
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
        