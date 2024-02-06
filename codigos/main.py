from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import codigos.helper as hp

app = FastAPI()

@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["index"])
def index():
    
    return "Proyecto MLOps Steam - Ingresar por favor a la ruta /docs para obtener información de la API"


@app.get(path = '/developer/{desarrollador}')
def developer(desarrollador:str):
    return hp.developer_info(desarrollador)


@app.get(path = '/userdata/{User_id}')
def userdata(User_id:str):
    return hp.userdata(User_id)


@app.get(path = '/UserForGenre/{genero}')
def UserForGenre(genero:str):
    return hp.UserForGenre(genero)


@app.get(path = '/BestDeveloperYear/{año}')
def best_developer_year(año:int):
    return hp.best_developer_year(año)


@app.get(path = '/DeveloperReviewsAnalysis/{desarrolladora}')
def developer_reviews_analysis(desarrolladora:str):
    return hp.developer_reviews_analysis(desarrolladora)


@app.get(path = '/RecomendacionJuego/{id_producto}')
def recomendacion_juego(id_producto):
    return hp.recomendacion_juego(id_producto)


@app.get(path = '/RecomendacionJuegoUsuario/{id_usuario}')
def recomendacion_usuario(id_usuario):
    return hp.recomendacion_usuario(id_usuario)