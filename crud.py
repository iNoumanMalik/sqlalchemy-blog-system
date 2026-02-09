from .models import User,Post,Comment
from sqlalchemy.orm import Session

def create_user(db:Session, name:str,email:str):
    user = User(name = name,email = email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db:Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_post(db:Session, user_id: int, title: str, content: str):
    post = Post(title = title, content = content, user_id = user_id, )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_posts_by_user(db:Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def create_comment(db:Session, message: str, post_id:int):
    comment = Comment(message = message, post_id = post_id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comments_by_post(db:Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()