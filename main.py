from api_config import *

app: FastAPI = APIConfig().app


@app.get('/examples')
def example():
    return {
        'Hello': 'World!'
    } 

