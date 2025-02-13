from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Iniciamos el server: uvicorn users:app --reload

#Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

user_list = [ User(name="Fulanez",surname="Menganez",url="https://noseque",age=33), 
         User(name="Menganez",surname="Citranez",url="https://noseque",age=34), 
         User(name="Citranez",surname="Fulanez",url="https://noseque",age=35), 
         User(name="Fulanito",surname="Mengan",url="https://noseque",age=36)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Fulanez","surname":"Menganez","url":"https://mouredev.dev","age":20},
            {"name":"Menganez","surname":"Citranez","url":"https://mouredev.dev","age":30}]

@app.get("/users")
async def users():
    return user_list