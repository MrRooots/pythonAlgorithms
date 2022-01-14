import sys
import itertools

sys.setrecursionlimit(4000)


# Types of matrix diagonals
class DiagonalType:
  all = 'All'  # All diagonal cells
  main = 'Main'  # Main diagonal cells
  side = 'Side'  # Side diagonal cells


# Color types
class Color:
  white = True  # Whites turn
  black = False  # Blacks turn


# Bishop swapper implementation
# Count of diagonal for turn checks operations
class BishopSwapper:
  # Constructor
  def __init__(self, width: int, height: int, figures: tuple) -> None:
    # Width of the chess board
    self.width = width

    # Height of the chess board
    self.height = height

    # Main chess board
    self.board = [['-' for _ in range(width)] for _ in range(height)]

    # List of white figures
    self.white = []

    # List of black figures
    self.black = []

    # Previous boards
    # Contains previous positions of figures for each iteration
    # TYPE: List[Tuple]
    self.prev_boards = []

    # Fill desk and figures lists
    for x, y, figure in figures:
      # Place figure on board
      self.board[y][x] = figure

      # Append initial coordinates into previous boards list
      self.prev_boards.append((x, y))

      # Fill color-dependent figures list
      self.white.append((x, y)) if y == 0 else self.black.append((x, y))

    # Count of figures
    self.length = len(self.white)

    # Simple generator for iteration count
    self.iter = (i for i in range(150000))

  @property  # Check if all bishops are placed correctly: O(n) with n = len(self.turns)
  def is_solved(self):
    return self.board[0].count('2') == self.board[self.height - 1].count('1') == self.length

  @staticmethod  # Simplest method to break list comprehension on a condition
  def stop():
    raise StopIteration

  # Get empty diagonal cells until first non-empty cell reached
  def empty_cells(self, cells: zip) -> itertools.takewhile:
    # result = set()
    
    # for x, y in cells:
    #   if self.board[y][x] == '-':
    #     result.add((x, y))
    #   else:
    #     break
    # return result
    
    return itertools.takewhile(lambda x: self.get_by(x) == '-', ((x, y) for x, y in cells))

  # Get the diagonal cells from given cell
  def diagonal_cells(self, cell: tuple, diagonal: str = DiagonalType.all) -> itertools.chain:
    x, y = cell
    
    if diagonal == DiagonalType.main:
      cells = (
        zip(range(x + 1, self.width), range(y - 1, -1, -1)),  # Right down
        zip(range(x - 1, -1, -1), range(y + 1, self.height, 1))  # Left up
      )
    elif diagonal == DiagonalType.side:
      cells = (
        zip(range(x - 1, -1, -1), range(y - 1, -1, -1)),  # Left down
        zip(range(x + 1, self.width), range(y + 1, self.height)),  # Right up
      )
    else:
      cells = (
        zip(range(x + 1, self.width, 1), range(y - 1, -1, -1)),  # Right down
        zip(range(x - 1, -1, -1), range(y + 1, self.height)),  # Left up
        zip(range(x - 1, -1, -1), range(y - 1, -1, -1)),  # Left down
        zip(range(x + 1, self.width), range(y + 1, self.height)),  # Right up
      )

      return itertools.chain(*(self.empty_cells(_zip) for _zip in cells))

    return itertools.chain(*cells)  

  # Get board element by its coordinates
  def get_by(self, coord: tuple) -> str:
    return self.board[coord[1]][coord[0]]

  # Swap the _from value with _to value on board
  def make_turn(self, _from: tuple, _to: tuple) -> None:
    self.board[_from[1]][_from[0]], self.board[_to[1]][_to[0]] = \
      self.get_by(_to), self.get_by(_from)

  # Check if given cell is available
  # by check all diagonal cells by different from move diagonal
  # Side -> checking Main || Main -> checking Side
  def is_cell_available(self, cell: tuple, prev: tuple) -> bool:
    diagonal = DiagonalType.side

    # Get the diagonal that will be checked
    if cell[0] > prev[0] and cell[1] > prev[1] or cell[0] < prev[0] and cell[1] < prev[1]:
      diagonal = DiagonalType.main

    for _cell in self.diagonal_cells(cell, diagonal):
      _cell = self.get_by(_cell)

      if _cell != '-' and _cell != self.get_by(prev):
        return False

    return True

  # Swap backtracking logic holder
  def swap_utility(self, color: bool = Color.white) -> bool:
    self.print_board(color)

    while not self.is_solved:
      turns = self.white if color else self.black

      # Iterate through figures of `color` side
      for i in range(self.length):
        # Get all diagonal cells for current bishop
        cells = self.diagonal_cells(turns[i])

        # Get available for move cells
        available_cells = [cell for cell in cells if self.is_cell_available(cell, turns[i])]

        # If the available turns are empty for the last figure 
        # then return to previous recursion level
        if not available_cells and i == self.length - 1:
          return False

        for cell in available_cells:
          initial_pos = turns[i]
          turns[i] = cell
          all_turns = turns + self.black if color else self.white + turns

          # Check if after turn we won't get the already used board
          if all_turns in self.prev_boards:
            turns[i] = initial_pos
            continue
          
          # Save current figures position
          self.prev_boards.append(all_turns)
          self.make_turn(initial_pos, cell)
          # print('{} -> {}'.format(initial_pos, cell))

          if self.swap_utility(not color):
            return True
          else:
            # print('{} -> {} UNDO'.format(initial_pos, cell))
            self.make_turn(initial_pos, cell)
            turns[i] = initial_pos
            self.print_board(color)
        
      else:
        return False
    
    return True

  # Start swapping controller
  def swap(self) -> None:
    try:
      print('Solved!') if self.swap_utility(Color.white) else print('No solution found!')
    except RecursionError:
      print('Failed! Maximum recursion depth exceeded!')

  # Print board
  def print_board(self, color: bool) -> None:
    i = self.height - 1
    print('  {} Turn ({})'.format('White' if color else 'Black', next(self.iter)))
    for row in reversed(self.board):
      print(i, end='| ')
      i -= 1
      for el in row:
        print(el, end=' ')
      print()
    print('   ' + ' '.join(str(i) for i in range(self.width)) + '\n')


def main() -> None:
  swapper = BishopSwapper(
    width=4, height=5,
    figures=(
      (1, 0, '1'),
      (0, 0, '1'),
      (0, 4, '2'),
      (1, 4, '2'),
    )
  )

  swapper.swap()


if __name__ == '__main__':
  main()
