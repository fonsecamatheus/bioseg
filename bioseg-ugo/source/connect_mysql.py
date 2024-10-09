import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('host'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password')
        )
        return connection
    except mysql.connector.Error as e:
        print(f'Erro ao conectar ao banco mysql: {e}')
        return None