# Blog System with SQLAlchemy

A simple blog system built with Python and SQLAlchemy ORM.  
Users can write posts, and posts can have comments.

---

## Project Structure

```sqlalchemy_blog_project/
├── app/
│ ├── init.py
│ ├── database.py # engine + session
│ ├── models.py # ORM models
│ ├── crud.py # CRUD operations
│ └── main.py # run & test
├── venv/
├── requirements.txt
└── blog.db
```

---

## Features

- Users with unique emails
- Users can create posts (1-to-many)
- Posts can have comments (1-to-many)
- Cascade deletes (user → posts → comments)
- Lazy & eager loading
- CRUD operations for users, posts, comments

---

## Quick Setup

```bash
# create virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
python -m pip install sqlalchemy

# run the project
python -m app.main
```

## Core Concepts Learned

- SQLAlchemy ORM mapping
- One-to-many relationships
- Foreign keys & referential integrity
- Lazy vs eager loading
- Cascade deletes
- Joins and queries
- CRUD on related tables
