from pydantic import BaseModel


class Category(BaseModel):
    categoria: str
    descricao: str
    idtipocategoria: int

