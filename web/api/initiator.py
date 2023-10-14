import core.ants as ants
import fastapi


api = fastapi.FastAPI()


@api.post('/create')
def create():
    pass