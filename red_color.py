'''
from termcolor import colored

print(colored('Hello', 'red'), colored('World', 'green'))
'''
'''
def red(name):
    print ("\033[91m {}\033[00m" .format(name))

red('This should be displayed in red colour')
'''

from termcolor import colored
import colorama
colorama.init()
print(colored('hello','red'), colored('world', 'green'))