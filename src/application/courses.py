from src.shared import schemas
from src.shared import formatters
from src.shared.schemas import CourseIn
from src.domain.db_repositories import CourseRepository
from src.shared.exceptions import try_except

class CourseServices:
  def __init__(self, repo: CourseRepository):
    self.repo = repo

  def save(self, course: schemas.CourseIn):
    response = self.repo.create_new_course(course)
    return response

  def get_all(self, formated: bool = False):
    response = self.repo.find_courses()
    if "error" in response: return response

    courses = [dict(course) for course in response]
    if formated: return formatters.format_list_courses(courses)
    return courses

  def get_one(self, id: int, formated: bool = False):
    response = self.repo.find_course_by_id(id)
    if "error" in response: return response

    course = dict(response)
    if formated: return formatters.format_course(course)
    return course

  def update_one(self, id: int, course: CourseIn):
    data = course.model_dump(exclude_none=True)
    response = self.repo.update_course_by_id(id, data)
    return response

  def delete_one(self, id: int):
    response = self.repo.delete_course_by_id(id)
    return response
