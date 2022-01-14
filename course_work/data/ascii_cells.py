# Implementation of desk cells in ascii symbols
class AsciiCell:
  cell_black = r'''
    ------- 
   | . . . |
   | . . . |
   | . . . |
    ------- 
  '''
  cell_white = r'''
    ------- 
   |       |
   |       |
   |       |
    ------- 
  '''
  cell_bishop_black_black = r'''
    ------- 
   |. .O. .|
   |. \*/ .|
   |. /_\ .|
    ------- 
  '''
  cell_bishop_black_white = r'''
    ------- 
   |  .O.  |
   |  \*/  |
   |  /_\  |
    ------- 
  '''
  cell_bishop_white_white = r'''
    ------- 
   |  .O.  |
   |  \ /  |
   |  /_\  |
    ------- 
  '''
  cell_bishop_white_black = r'''
    ------- 
   |. .O. .|
   |. \ / .|
   |. /_\ .|
    ------- 
  '''
