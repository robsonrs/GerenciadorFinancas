from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
import boto3
import os

app = FastAPI()

ENDPOINT="gerenciador-financas-database.cmwy4fkikpwu.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="admin"
REGION="us-east-1"
DBNAME="GERENCIADORFINANCAS"
PASSWORD="Robson0811#"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

session = boto3.Session(profile_name='default')
client = session.client('rds')
conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME)

#Habilitar quando conseguir resolver questão do IAM Authentication
#token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

class Categoria(BaseModel):
    categoria: str
    descricao: str

@app.get("/categorias")
def buscar_categorias():
    try:
        cur = conn.cursor()
        cur.execute("SELECT IDCATEGORIA, CATEGORIA, DESCRICAO FROM TB_CATEGORIAS")
        query_results = cur.fetchall()
        return {"Resultado": query_results}
    except Exception as e:
        return {"Erro ao conectar": e }
    
@app.put("/categorias")
def criar_categoria(item: Categoria):
    try:
        cur = conn.cursor()
        insert = "INSERT INTO TB_CATEGORIAS (CATEGORIA, DESCRICAO) VALUES (%s, %s)"
        data = (item.categoria, item.descricao)
        cur.execute(insert, data)
        conn.commit()
        conn.close()
        return {"Inserido com sucesso"}
    except Exception as e:
        conn.rollback()
        conn.close()
        return {"Erro ao conectar": e }
