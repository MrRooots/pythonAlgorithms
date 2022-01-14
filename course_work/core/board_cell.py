from course_work.data.ascii_cells import AsciiCell
from course_work.core.bishop import Bishop
from course_work.data.cell_color import Colors


# Desk cell implementation
class BoardCell:
  color = None  # Color of the cell == color of the bishop
  figure = None  # Cell contains the bishop or None
  x, y = None, None  # Cell coordinates

  # Constructor
  def __init__(
      self, x: int, y: int, color: Colors, bishop: Bishop = None
  ) -> None:
    self.x, self.y = x, y
    self.color = color
    self.figure = bishop

  def copy_with(self, x=None, y=None, figure=None, color=None):
    x = x if x else self.x
    y = y if y else self.y
    figure = figure if figure else self.figure
    color = color if color else self.color

    return BoardCell(x, y, color, figure)

  @property  # Is cell empty
  def is_empty(self) -> bool:
    return self.figure is None

  # Used for {x, y = BoardCell}
  def __getitem__(self, item):
    if item == 0:
      return self.x
    elif item == 1:
      return self.y

    raise IndexError

  @property  # Get cell as ascii
  def as_ascii(self):
    if self.figure is None:
      if self.color == Colors.black:
        return AsciiCell.cell_black
      else:
        return AsciiCell.cell_white
    else:
      if self.figure.own_by == 'white':
        if self.color == Colors.white:
          return AsciiCell.cell_bishop_white_white
        else:
          return AsciiCell.cell_bishop_white_black
      else:
        if self.color == Colors.white:
          return AsciiCell.cell_bishop_black_white
        else:
          return AsciiCell.cell_bishop_black_black
