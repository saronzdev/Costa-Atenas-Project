import sqlite3
from typing import List
from fastapi import APIRouter, status, HTTPException, Depends
from backend.models import courses_models
from backend.controllers import courses_contollers
from backend.db import db

router = APIRouter()

@router.get("/", response_model=List[courses_models.CourseOut])
def get_courses(db: sqlite3.Connection = Depends(db.get_db)):
  users = courses_contollers.get_courses(db)
  return users

@router.get("/{id}")#, response_model=courses_models.CourseOut)
def get_course(id: int, db: sqlite3.Connection = Depends(db.get_db)):
  user = courses_contollers.get_course(id, db)
  return user

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_courses(course: courses_models.CourseIn, db: sqlite3.Connection = Depends(db.get_db)):
  await courses_contollers.add_course(course, db)
  return status.HTTP_201_CREATED

@router.delete("/{id}")
async def delete_course(id: int, db: sqlite3.Connection = Depends(db.get_db)):
  await courses_contollers.del_course(id, db)
  return status.HTTP_200_OK

@router.put("/{id}")
async def update_course(id: int, new: courses_models.CourseUpdate, db: sqlite3.Connection = Depends(db.get_db)):
  await courses_contollers.update_course(new, id, db)
  return status.HTTP_200_OK