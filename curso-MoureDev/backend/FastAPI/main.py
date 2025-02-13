from fastapi import FastAPI

app = FastAPI()

# URL Local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "Hola FastAPI!"

# Desplegar servidor que hemos creado: uvicorn main:app --reaload

@app.get("/url")
async def url():
    return {"url":"https://mouredev.com/python" }

    # URL Local: http://127.0.0.1:8000/url


# Swagger UI para generar documentación

# O tambien 127.0.0.1/docs o /redoc

#Postman - Cliente para realizar peticiones a servidor local

#ThunderClient Cliente para la API en VS Code