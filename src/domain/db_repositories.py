from abc import ABC, abstractmethod
from src.shared import schemas

class CourseRepository(ABC):
  @abstractmethod
  def create_new_course(self, course: schemas.CourseIn):
    pass

  @abstractmethod
  def find_courses(self) -> list[schemas.CourseOut]:
    pass

  @abstractmethod
  def find_course_by_id(self, id: int):
    pass
  
  @abstractmethod
  def update_course_by_id(self, id: int, course: dict):
    pass

  @abstractmethod
  def delete_course_by_id(self, id: int):
    pass




















