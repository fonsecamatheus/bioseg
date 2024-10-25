import os

import pymysql
from dotenv import load_dotenv

load_dotenv()

def connect_mysql():
    try:
        connection = pymysql.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password')
        )
        return connection
    except pymysql.MySQLError as e:
        print(f'Erro ao conectar ao banco MySQL: {e}')
        return None
    except ValueError as ve:
        print(f'Erro de configuração: {ve}')
        return None
