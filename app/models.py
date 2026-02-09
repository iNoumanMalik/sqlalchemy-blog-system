from sqlalchemy import String, Text, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[String] = mapped_column(String(50),nullable=False)
    email:Mapped[String] = mapped_column(String(100),nullable=False,unique=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    posts:Mapped[list["Post"]] = relationship("Post",back_populates="author", cascade="all,delete")
    
    def __repr__(self):
        return f"<User id={self.id} name={self.name}>"

class Post(Base):
    __tablename__ = "posts"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(100),nullable=False)
    content:Mapped[str] = mapped_column(Text,nullable=False)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    author: Mapped["User"] = relationship("User",back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post", cascade="all,delete")
    
    def __repr__(self):
        return f"<Post id={self.id} title={self.title}>"
    
class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    message: Mapped[str] = mapped_column(String, nullable=False)
    post_id: Mapped[datetime] = mapped_column(ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    post: Mapped["Post"] = relationship("Post", back_populates="comments")
    
    
    def __repr__(self):
        return f"<Comment id={self.id} message={self.message[:20]}>"