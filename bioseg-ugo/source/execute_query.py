import pandas

from source.connect_mysql import connect_mysql


def execute_query(query):
    connection = connect_mysql()
    if connection:
        try:
            df = pandas.read_sql(query, connection)
            return df
        except Exception as e:
            print(f'Erro ao executar consulta: {e}')
        finally:
            connection.close()