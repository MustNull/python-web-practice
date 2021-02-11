from fastapi import FastAPI
from config import CONFIG, PRODUCTION
from .controller import user_controller


debug = False if CONFIG.ENV_MODE == PRODUCTION else True


app = FastAPI(debug=debug)
app.include_router(user_controller.router, prefix='/api')

@app.get("/")
def root():
    return "Hello world"

