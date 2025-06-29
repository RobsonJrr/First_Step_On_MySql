import pymysql
import pymysql.cursors
import dotenv
import os

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.DictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR,
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
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 2
        maior_id = 4
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s  '
        )

        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data5 = cursor.fetchall()

        # for row in data5:
        #     print(row)

    # with connection.cursor() as cursor:
    #     sql = (
    #         f'DELETE FROM {TABLE_NAME} '
    #         'WHERE id = %s'
    #     )
    #     cursor.execute(sql (1, ))
    #     connection.commit()

    #     cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('joaninha', 13, 4))
        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # data6 = cursor.fetchall()

        # for row in cursor.fetchall():
        #     _id, name, age = row
        #     print(_id, name, age)
        for row in cursor.fetchall():
            print(row)  
             
    connection.commit()
