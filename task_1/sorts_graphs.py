import random
from matplotlib import pyplot as plot


'''
Todo:
  1) Add c и m to each function
    compare_count -> count of compare action in function
    move_count    -> count of variables move in function (swap = 3)
  
  2) N -> each function exectuion count for randomly generated list
    Create lists for compare_count and move_count to store each function execution result
      P.S. Should be 6 arrays CI, MI | CB, MB | CS, MS

  PLAN:
    for i in range(N):
      create random array
      execute insertion_sort -> Get compare_count and move_count
      execute bubble_sort    -> Get compare_count and move_count
      execute selection_sort -> Get compare_count and move_count
    
    Compute the average for each list
    Plot graphics
'''

# Class that implements all sorting methods
class SortCollection:
  _LIST = []  # The list we will work with
  _LENGTH = 0  # The length of the list

  # Length counters
  _MAX_LENGTH = 100
  _ITERATION_COUNT = 1

  # Dictionary that contains the measures of each sort
  _SORT_MEASURES = {}

  # Initialize
  def __init__(self, unsorted_array: list = None, length: int = 20):
    # Set the received list or create the new one if received is empty
    self._LIST = unsorted_array if unsorted_array else self.generate_random_list(length)

    # Set the length of the list
    self._LENGTH = length

    # Set the dictionary that will store all statistic data for each function
    self._SORT_MEASURES = {
      'insertion_sort': {
        'compare_count': [],
        'move_count': [],
        'compare_average': [],
        'move_average': [],
      },
      'bubble_sort': {
        'compare_count': [],
        'move_count': [],
        'compare_average': [],
        'move_average': [],
      },
      'selection_sort': {
        'compare_count': [],
        'move_count': [],
        'compare_average': [],
        'move_average': [],
      },
    }

    # print('Initialized with:', self._LIST, 'of length', self._LENGTH, '\n')

  @staticmethod
  # Method will generate random list with given length
  def generate_random_list(length: int) -> list:
    """ Function that will generate the random list with given `length`

    :param int length: The length of the generated list
    :return: list: Randomly generated list with given length
    :rtype: list
    """
    return [random.randint(0, 10000) for _ in range(length)]

  # Method will check the sort result
  def check_sort_result(self, sorted_list: list) -> bool:
    return sorted_list == sorted(self._LIST)

  # Method will calculate the average values for list measures
  def calculate_measures_average(self) -> None:
    self._SORT_MEASURES['insertion_sort']['compare_average'].append(
      sum(self._SORT_MEASURES['insertion_sort']['compare_count']) / self._ITERATION_COUNT
    )
    self._SORT_MEASURES['insertion_sort']['move_average'].append(
      sum(self._SORT_MEASURES['insertion_sort']['move_count']) / self._ITERATION_COUNT
    )
    
    self._SORT_MEASURES['bubble_sort']['compare_average'].append(
      sum(self._SORT_MEASURES['bubble_sort']['compare_count']) / self._ITERATION_COUNT
    )
      
    self._SORT_MEASURES['bubble_sort']['move_average'].append(
      sum(self._SORT_MEASURES['bubble_sort']['move_count']) / self._ITERATION_COUNT
    )
    
    self._SORT_MEASURES['selection_sort']['compare_average'].append(
      sum(self._SORT_MEASURES['selection_sort']['compare_count']) / self._ITERATION_COUNT
    )
      
    self._SORT_MEASURES['selection_sort']['move_average'].append(
      sum(self._SORT_MEASURES['selection_sort']['move_count']) / self._ITERATION_COUNT
    )

  # Method will return the measures average
  def get_measures_average(self) -> dict:
    return {
      'insertion_sort': {
        'compare_average': self._SORT_MEASURES['insertion_sort']['compare_average'],
        'move_average': self._SORT_MEASURES['insertion_sort']['move_average'],
      },
      'bubble_sort': {
        'compare_average': self._SORT_MEASURES['bubble_sort']['compare_average'],
        'move_average': self._SORT_MEASURES['bubble_sort']['move_average'],
      },
      'selection_sort': {
        'compare_average': self._SORT_MEASURES['selection_sort']['compare_average'],
        'move_average': self._SORT_MEASURES['selection_sort']['move_average'],
      },
    }

  # Insertion sort implementation. Return NoneReturn None
  def insertion_sort(self, array: list = None) -> None:
    # Create the copy of the core `_LIST`
    _list = array if array else list(self._LIST)  # Get the list from param or from class variable
    _length = len(_list) if array else self._LENGTH  # Set the length from the class attribute or from the receied list

    _compare_count = 0
    _move_count = 0

    for i in range(1, _length):
      key = _list[i]  # Save the element of current iteration
      j = i - 1  # Get the index of previous element
      _move_count += 3

      while j >= 0 and _list[j] > key:
        _list[j + 1] = _list[j]
        j -= 1
        _move_count += 4
        _compare_count += 2

      _compare_count += 1

      _list[j + 1] = key
      _move_count += 2

    # Add the counter measures
    self._SORT_MEASURES['insertion_sort']['move_count'].append(_move_count)
    self._SORT_MEASURES['insertion_sort']['compare_count'].append(_compare_count)

    # print('Insertion sort:  ', _list)

  # Bubble sort implementation. Return None
  def bubble_sort(self, array: list = None) -> None:
    # Create the copy of the core `_LIST`
    _list = array if array else list(self._LIST)  # Get the list from param or from class variable
    _length = len(_list) if array else self._LENGTH  # Set the length from the class attribute or from the receied list

    _compare_count = 0
    _move_count = 0

    # The flag that responsible for the sorting state
    is_sorted = False

    # Iterate while the is_sorted flag is not True
    while not is_sorted:
      is_sorted = True
      
      _compare_count += 1  # For while 
      _move_count += 1  # For `is_sorted`

      for i in range(_length - 1):
        # If current element is bigger than following then swap them
        if _list[i] > _list[i + 1]:
          _list[i], _list[i + 1] = _list[i + 1], _list[i]  # Swap elements
          is_sorted = False  # Mark list as unsorted

          _compare_count += 1  # From if compare
          _move_count += 5  # 1 from if + 3 from swap + 1 from `is_sorted`

    _compare_count += 1  # From while when condition if False

    self._SORT_MEASURES['bubble_sort']['move_count'].append(_move_count)
    self._SORT_MEASURES['bubble_sort']['compare_count'].append(_compare_count)

    # print('Bubble sort:     ', _list)

  # Selection sort implementation. Return None
  def selection_sort(self, array: list = None) -> None:
    # Create the copy of the core `_LIST`
    _list = array if array else list(self._LIST)  # Get the list from param or from class variable
    _length = len(_list) if array else self._LENGTH  # Set the length from the class attribute or from the receied list
    
    _compare_count = 0
    _move_count = 0

    # Sort implementation
    for i in range(0, _length):
      min_index = i

      for j in range(i + 1, _length):
        _compare_count += 1
        if _list[min_index] > _list[j]:
          min_index = j

      _list[i], _list[min_index] = _list[min_index], _list[i]  # Swap elements
      _move_count += 3
    
    self._SORT_MEASURES['selection_sort']['compare_count'].append(_compare_count)
    self._SORT_MEASURES['selection_sort']['move_count'].append(_move_count)

  # Method will execute all sorts
  def execute_all_sorts(self, array: list = None) -> None:
    if array:
      self.insertion_sort(array=list(array))
      self.bubble_sort(array=list(array))
      self.selection_sort(array=list(array))
    else:
      self.insertion_sort()
      self.bubble_sort()
      self.selection_sort()

  # Method will print the measures average values for all sorts
  def print_measures_average(self) -> None:
    print('Insertion sort:')
    print('\tAverage compare count: {}\n'.format(self._SORT_MEASURES['insertion_sort']['compare_average']))
    print('\tAverage move count: {}\n'.format(self._SORT_MEASURES['insertion_sort']['move_average']))
    
    print('Bubble sort:')
    print('\tAverage compare count: {}\n'.format(self._SORT_MEASURES['bubble_sort']['compare_average']))
    print('\tAverage move count: {}\n'.format(self._SORT_MEASURES['bubble_sort']['move_average']))
    
    print('Selection sort:')
    print('\tAverage compare count: {}\n'.format(self._SORT_MEASURES['selection_sort']['compare_average']))
    print('\tAverage move count: {}\n'.format(self._SORT_MEASURES['selection_sort']['move_average']))

  def clear_measures_values(self):
    self._SORT_MEASURES['insertion_sort']['compare_count'].clear()
    self._SORT_MEASURES['insertion_sort']['move_count'].clear()
    self._SORT_MEASURES['bubble_sort']['compare_count'].clear()
    self._SORT_MEASURES['bubble_sort']['move_count'].clear()
    self._SORT_MEASURES['selection_sort']['compare_count'].clear()
    self._SORT_MEASURES['selection_sort']['move_count'].clear()

  # Method that will execute all sorts _MAX_LENGTH + _ITERATION_COUNT times
  def measuring_execution(self) -> None:
    # Generationg arrays of required length start from 1 to _MAX_LENGTH
    for i in range(2, self._MAX_LENGTH + 1):
      # Generate the random list with length i _ITERATION_COUNT times
      for j in range(self._ITERATION_COUNT):
        array = self.generate_random_list(length=i)
        
        # Execute all sorts for the generated array
        self.execute_all_sorts(array=array)

      # This method will calculate the average values of the compare and move count for current iteration
      self.calculate_measures_average()
      
      self.clear_measures_values()

    # self.print_measures_average()


def draw_graph(name: str) -> None:
  plot.xlabel('List Length')
  plot.ylabel('Average values')
  plot.xticks(ticks=[i*10 for i in range(11)])
  
  compare = measures[sort_name]['compare_average']
  move = measures[sort_name]['move_average']
  difference = [compare[i] - move[i] for i in range(len(move))]
  
  plot.plot(compare, label='Compare Average')
  plot.plot(move, label='Move Average')

  print(move[48])

  plot.plot(difference, label='Difference')
  
  print(difference)

  plot.title(' '.join(i.title() for i in sort_name.split('_')))

  plot.legend()
  plot.savefig('./images/' + sort_name + '.png')
  plot.close()


if __name__ == '__main__':
  sort_collection = SortCollection()
  # sort_collection.execute_all_sorts()
  sort_collection.measuring_execution()
  measures = sort_collection.get_measures_average()

  for sort_name in measures.keys():
    # print(sort_name)
    # print('\t', measures[sort_name]['compare_average'])
    # print('\t', measures[sort_name]['move_average'])

    if sort_name == 'selection_sort':
      draw_graph(name=sort_name)

