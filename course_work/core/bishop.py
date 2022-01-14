# Chess bishop figure implementation
class Bishop:
  x, y = None, None  # Current coordinates
  _own_by = None  # Owner side

  # Constructor
  def __init__(self, x: int, y: int, own_by: str) -> None:
    self.x, self.y = x, y
    self._own_by = own_by

  @property  # Get the owner side
  def own_by(self) -> str:
    return self._own_by.lower()

  @property  # Get current coordinates as tuple
  def coord(self):
    return self.x, self.y

  # Move bishop to given position
  def move_to(self, x, y):
    self.x, self.y = x, y
