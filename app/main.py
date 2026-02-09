from app.database import engine, session
from app.models import Base, Post
from app.crud import crud
from sqlalchemy.orm import joinedload

Base.metadata.create_all(bind=engine)
db = session()

user = crud.create_user(db, "Nouman", "nouman@emumba.com")

post1 = crud.create_post(db, user.id, "My First Post", "This is content")
post2 = crud.create_post(db, user.id, "My Second Post", "More content")

comment1 = crud.create_comment(db, post1.id, "Great post brother")
comment2 = crud.create_comment(db, post1.id, "Thanks for sharing")

posts = crud.get_posts_by_user(db, user.id)
for post in posts:
    print(post, post.comments)
    
posts_with_comments = db.query(Post).options(joinedload(Post.comments)).all()
for post in posts:
    print(post.title)
    for comment in post.comments:
        print(comment.message)
        
db.close()