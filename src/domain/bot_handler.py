from telegram import Update
from telegram.ext import ContextTypes
from abc import ABC, abstractmethod

class BotCommandHandler(ABC):
  @abstractmethod
  async def start_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

  @abstractmethod
  async def help_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

  @abstractmethod
  async def get_courses_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass  
  
  @abstractmethod
  async def new_course_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass  
  
  @abstractmethod
  async def update_course_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass  
  
  @abstractmethod
  async def delete_course_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass  
  
  @abstractmethod
  async def handler_inputs_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

