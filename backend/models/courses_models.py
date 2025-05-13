from pydantic import BaseModel
from typing import Optional

class CourseIn(BaseModel):
  name: str
  price: float

class CourseOut(BaseModel):
  id: int
  name: str
  price: float
  
class CourseUpdate(BaseModel):
  name: Optional[str] = None
  price: Optional[float] = None