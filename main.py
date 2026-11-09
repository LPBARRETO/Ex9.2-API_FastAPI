from fastapi import FastAPI

# Inicializa o aplicativo FastAPI
app = FastAPI()

# Rota RESTful usando o método GET
@app.get('/api/hello')
def api_hello():
    return {
        "status": "sucesso",
        "mensagem": "Hello World RESTful com FastAPI!",
        "codigo": 200
    }