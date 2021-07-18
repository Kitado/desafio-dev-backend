import MySQLdb
from typing import Union


USER = "root"
DB = "Blu365"
HOST = "mysql"
PORT = 3306


class Database:

    def __init__(self) -> None:
        self.conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, db=DB)
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        self.execute = self.cursor.execute
        
    def __del__(self):
        self.conn.close()

    def read(self, profissao):
        query = f"SELECT * FROM profissoes WHERE profissao = '{profissao}'" 
        
        self.execute(query)
        return self.cursor.fetchone()
    
        
    def register(self, profissao: str, valor_diario: Union[float, int]):
        
        query = f"INSERT INTO profissoes (profissao, valor_diario) VALUES ('{profissao}', {valor_diario})"

        try:
            self.execute(query)
            return "Cadastrado com sucesso!", 201
        except Exception as err:
            return f"Houve algum erro: {err.args}", 400
    