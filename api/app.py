from fastapi import FastAPI

from api.route_api import router


app = FastAPI()

app.include_router(router)
