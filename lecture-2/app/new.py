from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import  randrange

app = FastAPI()

#Specify the schema of the  post
class Post(BaseModel):
	title:str
	content:str
	published:bool =  True
	rating:Optional[int] = None

my_posts = [{'title':'post 1','content':'content of post 1','id':1},{'title':'post 2','content':'content of post 2', 'id':2}]

@app.get("/")
def root():
	return {"message":"Hello, This is Server from WSL"}

@app.get("/posts")
def get_posts():
	return {"data":my_posts}
@app.get("/posts/{id}")
def get_post(id:int, response:Response): #Data Validation of path parameter to be integer
	data = None
	for each in my_posts:
		if each['id'] == id:
			data = each
			break
	if data is None:
		#response.status_code = status.HTTP_404_NOT_FOUND
		#response.status_code = 404
		#return {"message":f"post with {id} was not found"}
	
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} was not found")
	return {"post_detail":data}
"""
@app.post("/createposts")
def create_posts(payLoad:dict= Body(...)):
	#print(payLoad)
	return {"new_post":f"Title:{payLoad['title']} Content:{payLoad['content']}"}
"""

#@app.post("/posts")
#To change the status code of a specific path operation
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(new_posts: Post, response:Response):
	post_dict = new_posts.dict()
	post_dict['id'] = randrange(0,1000000)
	my_posts.append(post_dict)
	return {"new_data":post_dict}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
	data_index = None
	for each in my_posts:
		print(each)
		if each['id'] == id:
			data_index = my_posts.index(each)
			break
	if data_index is None:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"post with {id} not found")
	return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post:Post):
	data_index = None
	for each in my_posts:
		if each['id'] == id:
			data_index = my_posts.index(each)
			break
	if data_index is None:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
	post_dict = post.dict()
	my_posts[data_index] = post_dict
	
	return {"message":f"updated post with {id} successfully"}
