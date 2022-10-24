import json
import urllib.parse as up
import psycopg2 as db

def connectDb():
    with open('config.json', 'r', encoding= 'utf-8') as file:
        dicionary = json.load(file)
        try:
            #usando elephantsql
            up.uses_netloc.append("postgres")
            url = up.urlparse(dicionary['url'])
            
            conn = db.connect(database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
            )

            return conn
            
            #usando banco de dados local
            # connect = db.connect(user= dicionary['user'], 
            #                     password= dicionary['password'],
            #                     host= dicionary['host'],
            #                     database= dicionary['database'])
            # return connect
        except Exception as e:
            print('erro', e)
    