from fastapi import FastAPI
from enum import Enum

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class ModelName(str , Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"





@app.get("/")
async def root():
    return {"message":"hello there"}

@app.get("/users/{user_id}")
async def read_user(user_id: str): 
    return {"user_id": user_id}

@app.get("/name")
async def names():
    return ["rick", "berry"]

@app.get("/whook")
def message():
    return ["hello webhook"]

@app.get("/names/{user_name}")
async def read_name(user_name: str):
    return {"user_name": user_name}

@app.get("/items/")
async def read_item(skip: int =0 , limit:int =7):
    return fake_items_db[skip:skip+limit]


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}








