
import sys
import os
from os import walk
import fileclass

global filecounter
global numpythonfiles
global linecount
global filetitle

filename = sys.argv[1]
filetitle = sys.argv[0:]
numpythonfiles = 0 
filecounter = 0
linecount = 0

def main(filename):
   recursivefunction(filename)
   
   avg = float(linecount/numpythonfiles)

   fileinfo = fileclass.File(filename,filetitle, linecount, numpythonfiles, avg)
   print(fileinfo)
def countLines(filename):
   global linecount
   file = open(filename, "r")
   for i in file:
      linecount += 1
   file.close()
def recursivefunction(filename):
   global numpythonfiles
   global filecounter
   if os.path.isfile(filename) == True:
      filecounter += 1
      if filename.endswith(".py"):
         numpythonfiles += 1
         countLines(filename)
   else:
      for i in os.listdir(filename): 
        recursivefunction(filename + "/" + str(i))

main(filename)
