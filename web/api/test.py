import fastapi as fast

api = fast.FastAPI()


@api.get('/')
def hello_world():
    return 'hello world!'
