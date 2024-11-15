from fastapi import FastAPI
from pydantic import BaseModel
from nilai import nilai_router


app = FastAPI()

app.include_router(nilai_router)


@app.post("/")
def read_root():
    return {"Hello": "World"}

@app.post("/mahasiswa")
def read_root():
    return {"Hello": "Mahasiswa"}


@app.post("/mahasiswa/1")
def data_mahasiswa():
    return {"Hello": "Mahasiswa 1"}

@app.post("/mahasiswa/{prodi}/{nim}")
def mahasiswa_prodi(prodi, nim):
    return {"Hello": "Mahasiswa prodi "+ prodi + " dengan nim "  + nim}

class Item(BaseModel):
    name: str
    description: str 
    price: float
    tax: float 

@app.post("/items/")
async def create_item(item: Item):
    return item
