from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel  


api=FastAPI()
#get, post, put, delete
@api.get("/")
def login():
    return {"message": "Welcome to my api"}


@api.get("/posts")
def get_post():
    return {"posts":"get your post"}

@api.post("/createPost")
def create_post(new_Post:Post):
    print(new_Post)
    return{"new_post":f"title {payload["title"]}content:{payload['content']}"}

class Post(BaseModel):
    title: str
    content: str