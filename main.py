from fastapi import FastAPI
from fastapi.responses import JSONResponse

from entity.category import Category
from services.create_category import create_category
from services.get_category import get_all_categories

app = FastAPI()


@app.get("/category")
def get_categories():
    list_categories = get_all_categories()
    return list_categories


@app.post("/category")
def post_category(category: Category):
    generated_id = create_category(category)

    return JSONResponse(content={"id": generated_id}, status_code=201)
