from graphics import *

# Writes points to a file. If the file already exists, you should overwrite.
# You can write your points to a file such that all lines will have one point in csv format
# ========
# Example:
# 10.3,5.4
# 21.2,5.3
# 5.1,2.7
# ...
# ========
# points: points to be saved, type: list of tuples containing two floats 
# fileName: file name of the file, type: string
def savePoints(points, fileName):
   f = open(fileName, 'w')
   for i in range(len(points)):
      file = str(points[i])
      file = file.replace("[", "")
      file = file.replace("]", "")
      f.write(file + '\n')
   f.close()
      
   
# Reads points from a file. If the file do not exist, return an empty list.
# fileName: file name of the file, type: string
# RETURNS: points, type: list of tuples containing two floats
def readPoints(fileName):
   f = open(fileName, 'r')
  
   lines = f.readlines()
   list1 = []
      
   for line in lines:
      values = line.split(",")
      x = float(values[0].strip())
      y = float(values[1].strip())
      point = (x,y)
      list1.append(point)
      
   return list1
 
# Plots given points to the given window with the given color.
# You can plot small Circle's to make your points visible.
# points: points to be plotted, type: list of tuples containing two floats 
# win: window object to plot points on, type: GraphWin
# color: color of the points, type: string
def plotPoints(points, win, color):
   for i in range(len(points)):
      pointC = points[i]
      x = pointC[0]
      y = pointC[1]
      point1 = Point(x,y)
      c = Circle(point1, 5)
      c.setFill(color)
      c.draw(win)