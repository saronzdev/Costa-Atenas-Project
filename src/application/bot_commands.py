from src.infrastructure.bot.commands import CommandsHandler

commands = CommandsHandler()

class TelegramCommandHandler():
  def start(self, update, context):
    return commands.start_cmd(update, context)

  def help(self, update, context):
    return commands.help_cmd(update, context)

  def get(self, update, context):
    return commands.get_courses_cmd(update, context)

  def new(self, update, context):
    return commands.new_course_cmd(update, context)

  def update(self, update, context):
    return commands.update_course_cmd(update, context)

  def delete(self, update, context):
    return commands.delete_course_cmd(update, context)

  def handler_inputs(self, update, context):
    return commands.handler_inputs_cmd(update, context)