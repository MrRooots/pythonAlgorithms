import time
import itertools
from functools import wraps

def timeit(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print('Execution time of [{}]: {}'.format(func.__name__, end - start))
    return result
  
  return wrapper

def stop():
  raise StopIteration

def empty_cells(cells: tuple):
  return itertools.takewhile(lambda x: True, ((x, y) for x, y in cells))

@timeit
def diagonal_cells(cell: tuple) -> itertools.chain:
  width = 10000
  height = 10000
  # board = [['-' for _ in range(width)] for _ in range(height)]
  x, y = cell

  cells = (
    zip(range(x + 1, width, 1), range(y - 1, -1, -1)),  # Right down
    zip(range(x - 1, -1, -1), range(y + 1, height)),  # Left up
    zip(range(x - 1, -1, -1), range(y - 1, -1, -1)),  # Left down
    zip(range(x + 1, width), range(y + 1, height)),  # Right up
  )

  return [i for i in itertools.chain(*(empty_cells(_zip) for _zip in cells))]


r = diagonal_cells((5000, 5000))
