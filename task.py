# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["blog_platform"]
posts_collection = db["posts"]


class Post(BaseModel):
    title: str
    content: str


class Comment(BaseModel):
    content: str


class Like(BaseModel):
    like: bool


class PostModel:
    def __init__(self, title: str, content: str, comments=[], likes=0, dislikes=0):
        self.title = title
        self.content = content
        self.comments = comments
        self.likes = likes
        self.dislikes = dislikes

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "comments": self.comments,
            "likes": self.likes,
            "dislikes": self.dislikes,
        }


@app.post("/posts/")
async def create_post(post: Post):
    post_data = PostModel(title=post.title, content=post.content)
    post_id = posts_collection.insert_one(post_data.to_dict()).inserted_id
    return {"id": str(post_id), **post.dict()}


@app.get("/posts/{post_id}")
async def read_post(post_id: str):
    post_data = posts_collection.find_one({"_id": ObjectId(post_id)})
    if post_data:
        return post_data
    else:
        raise HTTPException(status_code=404, detail="Post not found")


@app.put("/posts/{post_id}")
async def update_post(post_id: str, post: Post):
    post_data = posts_collection.find_one({"_id": ObjectId(post_id)})
    if post_data:
        posts_collection.update_one({"_id": ObjectId(post_id)}, {"$set": post.dict()})
        return {"message": "Post updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    post_data = posts_collection.find_one({"_id": ObjectId(post_id)})
    if post_data:
        posts_collection.delete_one({"_id": ObjectId(post_id)})
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts/{post_id}/comments/")
async def create_comment(post_id: str, comment: Comment):
    post_data = posts_collection.find_one({"_id": ObjectId(post_id)})
    if post_data:
        posts_collection.update_one(
            {"_id": ObjectId(post_id)}, {"$push": {"comments": comment.dict()}}
        )
        return {"message": "Comment added successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts/{post_id}/like/")
async def like_post(post_id: str, like: Like):
    post_data = posts_collection.find_one({"_id": ObjectId(post_id)})
    if post_data:
        if like.like:
            posts_collection.update_one({"_id": ObjectId(post_id)}, {"$inc": {"likes": 1}})
        else:
            posts_collection.update_one({"_id": ObjectId(post_id)}, {"$inc": {"dislikes": 1}})
        return {"message": "Reaction added successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
