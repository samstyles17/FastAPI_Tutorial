from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#Specify the schema of the  post
class Post(BaseModel):
	title:str
	content:str
	published:bool =  True
	rating:Optional[int] = None

@app.get("/")
def root():
	return {"message":"Hello, This is Server from WSL"}

@app.get("/posts")
def get_posts():
	return {"data":"This is your posts"}
"""
@app.post("/createposts")
def create_posts(payLoad:dict= Body(...)):
	#print(payLoad)
	return {"new_post":f"Title:{payLoad['title']} Content:{payLoad['content']}"}
"""

@app.post("/createposts")
def create_posts(new_posts: Post):
	print(new_posts)
	return {"new_data":f"Title->{new_posts.title} Content->{new_posts.content} Published->{new_posts.published}"}
