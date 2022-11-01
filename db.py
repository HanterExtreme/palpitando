from multiprocessing.reduction import duplicate

from db_connection import connectDb

con = connectDb()
cur = con.cursor()

class Db:
    def __init__(self):
        self.conn = connectDb()
        self.cur = self.conn.cursor()
        self.create()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        self.conn.commit()
        self.conn.close()
        self.cur.close()

    def create(self):
        try:
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS palpites (match_id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, homeTeam VARCHAR(255) NOT NULL, awayTeam VARCHAR(255) NOT NULL, PRIMARY KEY (match_id, name))")
        except Exception as e:
            print('deu erro', e)

    def insert(self, match_id, name, homeTeam, awayTeam, data):
        try:
            self.cur.execute(f"INSERT INTO palpites VALUES ('{match_id}', '{name}', '{homeTeam}', '{awayTeam}', '{data}')")
        except Exception as e:
            print(e)
    
    def update(self, match_id, name, homeTeam, awayTeam):
        try:
            self.cur.execute(f"UPDATE palpites SET homeTeam = {homeTeam}, awayTeam = '{awayTeam}' WHERE match_id = '{match_id}' AND name = '{name}'")
        except Exception as e:
            print(e)

    def select(self, where=''):
        try:
            self.cur.execute(f"SELECT * FROM palpites {where}")
            return (self.cur.fetchall())
        except Exception as e:
            print('deu erro', e)

    def select_match(self):
        try:
            self.cur.execute(f"SELECT match_id, TO_CHAR(time, 'MM/DD/YY HH24:MI') FROM palpites GROUP BY match_id, time order by time ASC ")
            return (self.cur.fetchall())
        except Exception as e:
            print('deu erro', e)

    def show_palpites(self, id):
        try:
            self.cur.execute(f"SELECT * FROM palpites WHERE match_id = '{id}'")
            return (self.cur.fetchall())
        except Exception as e:
            print('deu erro', e)

    
    def delete(self):
        try:
            self.cur.execute(f"DELETE FROM palpites")
        except Exception as e:
            print('deu erro', e)

    def delete_palpite(self, id):
        try:
            self.cur.execute(f"DELETE FROM palpites where match_id = '{id}'")
        except Exception as e:
            print('deu erro', e)
