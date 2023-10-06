import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from entity.category import Category
from services.create_category import create_category
from services.get_category import get_all_categories

app = FastAPI()

@app.get("/category")
def get_categories():
    list_categories = get_all_categories()
    json_object = json.dumps([obj.__dict__ for obj in list_categories], ensure_ascii=False).encode("utf-8")

    return json_object

@app.post("/category")
def post_category(category: Category):
     create_category(category)
     
     return JSONResponse(content={"message": "OK"})