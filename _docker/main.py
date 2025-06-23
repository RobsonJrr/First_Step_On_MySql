import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        #cuidado: limpa a tabela
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%s, %s) '
        )
        data = ('robson', 30)
        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "name": "maria",
            "age": 21,
        }
        result = cursor.execute(sql, data2)
        # print(sql, data)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "joão", "age": 33, },
            {"name": "maria", "age": 22, },
            {"name": "vitor", "age": 11, },
        )
        result = cursor.executemany(sql, data3)
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade)'
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("alex", 43),
            ("bob", 52),
        )
        result = cursor.executemany(sql, data4)
        print(sql)
        print(data4)
        print(result)
    connection.commit()