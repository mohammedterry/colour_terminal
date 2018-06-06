from sys import stderr
BLACK = 0
BOLD = 1
GREY = 2
ITALIC = 3
UNDERLINE = 4
FLASHING = 5
HIGHLIGHT = 7
WHITE = 8
RED = 31
GREEN = 32 
YELLOW = 33
PURPLE = 34 
PINK = 35
BLUE = 36
BOLDWHITE = 37 

def print(txt,colour=0):
    stderr.write('\x1b[1;{}m{}\x1b[0m\n'.format(colour,txt))