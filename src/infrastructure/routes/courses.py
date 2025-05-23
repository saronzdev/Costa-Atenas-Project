from typing import List
from fastapi import APIRouter, status, HTTPException
from src.shared.schemas import CourseIn, CourseOut
from src.application.courses import CourseServices
from src.infrastructure.database.courses import CoursesRepository
import config

repo = CoursesRepository(config.DB_DIR)
courses = CourseServices(repo)

router = APIRouter()

@router.get("/", response_model=List[CourseOut])
def get_courses():
  response = courses.get_all()
  if "error" in response: raise HTTPException(status_code=response["error"])
  return response

@router.get("/{id}", response_model=CourseOut)
def get_course(id: int):
  response = courses.get_one(id)
  if "error" in response: raise HTTPException(status_code=response["error"])
  return response

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_courses(course: CourseIn):
  response = courses.save(course)
  if "error" in response: raise HTTPException(status_code=response["error"])
  return status.HTTP_201_CREATED

@router.put("/{id}")
async def update_course(id: int, course: dict):
  response = courses.update_on(id, course)
  if "error" in response: raise HTTPException(status_code=response["error"])
  return status.HTTP_200_OK

@router.delete("/{id}")
async def delete_course(id: int):
  response = courses.delete_one(id)
  if "error" in response: raise HTTPException(status_code=response["error"])
  return status.HTTP_200_OK
