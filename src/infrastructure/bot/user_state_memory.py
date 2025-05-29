from src.domain.user_state import UserStateManager

class InMemoryUserState(UserStateManager):
  def __init__(self):
    self._states = {}

  def get(self, user_id):
    return self._states.get(user_id)

  def set(self, user_id, state: dict):
    self._states[user_id] = state

  def delete(self, user_id):
    if user_id in self._states:
      del self._states[user_id]

  def has(self, user_id):
    return user_id in self._states