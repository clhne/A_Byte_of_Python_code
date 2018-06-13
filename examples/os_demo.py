#!/usr/bin/python
import os
#print os.name                   # Windows-->nt, Linux/Unix-->posix
#print os.uname()              # only supported on Linux/Unix
#print os.listdir('/')         # Linux
#print os.listdir('f:\\')      # Windows
#os.remove('12.txt')
#print os.getcwd()
#print os.listdir(os.getcwd())
#print os.getenv('os')
#os.system('date')
print os.path.isfile('poem.txt')
