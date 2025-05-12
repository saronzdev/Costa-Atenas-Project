from typing import List
from fastapi import APIRouter, status, HTTPException
from models import models
from backend.controllers import courses_contollers

router = APIRouter()

@router.get("/", response_model=List[models.CourseOut])
async def get_courses():
  users = courses_contollers.get_courses()
  if users == 0:
    return users
  else: raise HTTPException(status_code=404)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_courses(course: models.CourseIn):
  response = await courses_contollers.add_course(course)
  if response != 0: raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error when save on db")
  return status.HTTP_201_CREATED

@router.delete("/{id}")
async def delete_course(id: int):
  response = await courses_contollers.delete_course(id)
  if response != 0: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return status.HTTP_200_OK

@router.put("/{id}")
async def update_course(id: int, new: models.CourseIn):
  response = await courses_contollers.update_course(new, id)
  if response != 0: raise HTTPException(status_code=404)
  return status.HTTP_200_OK