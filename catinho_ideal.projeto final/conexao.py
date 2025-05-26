import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="cantinho_ideal",
        password="rbc123567",
        database="sistema_locacao",
        auth_plugin='mysql_native_password'
        )



print(conectar())
