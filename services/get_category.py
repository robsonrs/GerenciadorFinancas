import logging
import mysql.connector
from mysql.connector import errorcode
from entity.category import Category
from helpers.connection import open_connection

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_all_categories():
    results = []
    try:
        con = open_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM TB_CATEGORIA")
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        con.close()

    list_category = []
    try:
        for item in results:
            list_category.append(Category(categoria=item[1], descricao=item[2], idtipocategoria=item[3]))
    except ValueError as e:
        print(e)

    return list_category
