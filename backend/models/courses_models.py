from pydantic import BaseModel

class CourseIn(BaseModel):
  name: str
  price: float

class CourseOut(BaseModel):
  id: int
  name: str
  price: float