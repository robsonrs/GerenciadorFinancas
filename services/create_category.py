import logging
import mysql.connector
from mysql.connector import errorcode
from entity.category import Category
from helpers.connection import open_connection

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def create_category(category):
    try:
        con = open_connection()
        cursor = con.cursor()
        cursor.execute(f'''INSERT INTO TB_CATEGORIA (CATEGORIA, DESCRICAO, IDTIPOCATEGORIA) VALUES 
                        ('{category.categoria}', 
                         '{category.descricao}', 
                         {category.idtipocategoria})''')
        con.commit()
        generated_id = cursor.lastrowid
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        con.close()

    return generated_id