"""import pyodbc

conect_db = (
    "Driver={SQL Server};"
    "Server=DESKTOP-0N7ETQB\SQLSERVER2022;"
    "Database=dbphyton;"
)
"""



import mysql.connector


conexo = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '190614',
    database = 'dbloja'
)

cursor = conexo.cursor()

nome_produto = "PC"
valor = 3500


#CREATE -----

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

cursor.execute(comando)
conexo.commit()
print (comando)


#READ -----

comando = f'SELECT * FROM vendas'

cursor.execute(comando)
resultatdo = cursor.fetchall()
print (resultatdo)

cursor.close()
conexo.close()


#UPDATE -------

comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexo.commit()

cursor.close()
conexo.close()


#DELETE ------
comando = f'DELETE FROM vendas WHERE valor = {valor}'
cursor.execute(comando)
conexo.commit()

cursor.close()
conexo.close()

