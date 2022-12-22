from fastapi import FastAPI
from fastapi.responses import JSONResponse
from db.models import User, Channel
from dao.user import UserDAO
from dao.channel import ChannelDAO
app = FastAPI()

@app.get("/")
async def root():
    return {
        "data" : {
            "message" : "Welcome to chat"
        }
    }

@app.post("/user")
async def create_user(user: User):
    user_dao = UserDAO()
    user_dao.create_user(data=user.dict())

    return JSONResponse({"data" : {
        "message" : "User created"
    }})

@app.get("/user")
async def get_user(id:int, name:str=None, email:str=None):
    user_dao = UserDAO()
    ret = user_dao.get_user(id=id)

    return JSONResponse({"data": ret})

    # Implement feature to get based on name and email

@app.post("/channel")
async def create_channel(channel:Channel):
    ch_dao = ChannelDAO()
    ch_dao.create_channel(data=channel.dict())

    return JSONResponse({"data" : {
        "message" : "Channel created :)"
    }})

@app.get("/channel")
async def get_channel(id: int, name:str=None, email:str=None):
    ch_dao = ChannelDAO()
    ret = ch_dao.get_channel(id=id)

    return JSONResponse({"data" : ret})

    

