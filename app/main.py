from app.database import engine, session
from app.models import Base

Base.metadata.create_all(bind=engine)

