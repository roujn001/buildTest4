from fastapi import FastAPI

app = FastAPI()

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



    
