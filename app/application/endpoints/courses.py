import sqlite3
from typing import List
from fastapi import APIRouter, status, HTTPException
from app.application.models import CourseIn, CourseOut
from app.infrastructure.database.courses_repository import get_one, get_all, create, update, delete

router = APIRouter()

@router.get("/", response_model=List[CourseOut])
def get_courses():
  response = get_all()
  if "error" in response: raise HTTPException(status_code=404)
  return [dict(row) for row in response]

@router.get("/{id}", response_model=CourseOut)
def get_course(id: int):
  response = get_one(id)
  if "error" in response: raise HTTPException(status_code=404)
  return dict(response)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_courses(course: CourseIn):
  response = create(course)
  if "error" in response: raise HTTPException(status_code=404)
  return status.HTTP_201_CREATED

@router.put("/{id}")
async def update_course(id: int, course: dict):
  response = update(id, course)
  if "error" in response: raise HTTPException(status_code=404)
  return status.HTTP_200_OK

@router.delete("/{id}")
async def delete_course(id: int):
  response = delete(id)
  if "error" in response: raise HTTPException(status_code=404)
  return status.HTTP_200_OK
