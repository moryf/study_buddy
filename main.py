from fastapi import FastAPI
from controllers import topic_controller


app = FastAPI()

app.include_router(router=topic_controller.router, prefix="/topic", tags=["topic"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
