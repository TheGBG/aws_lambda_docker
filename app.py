from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()

@app.get("/")
def home():
    return "Hello from Docker"


@app.get("/square")
def square(number: int):
    return number**2


# handler needed for the lambda
handler = Mangum(app)
