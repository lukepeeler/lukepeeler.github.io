import math
from graphics import *
from utility import *
from collections import Counter

# Calculates euclidean-distance between x and y
# x: a point, type: tuple containing two floats
# y: a point, type: tuple containing two floats
# RETURNS: Euclidean distance between x and y, type: float
def distance(x, y):
   dist = math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2))
   return dist

# Returns the majority vote in myList
# myList: a list of items, type: list of strings
# RETURNS: The element which is seen the most, type: string
def majority(myList):

   itemCounts = {}
   for i in range(len(myList)):
      
      if myList[i] not in itemCounts:
         itemCounts[myList[i]] = 1
      else:
         itemCounts[myList[i]] += 1

   maxCount = -1
   majorityItem = ""
   for k in itemCounts:
      if itemCounts[k] > maxCount:
         maxCount = itemCounts[k]
         majorityItem = k

   return majorityItem

# Classifies a new point using k-NN classifier
# bluePoints: list of blue points, type: list of tuples containing two floats
# redPoints: list of red points, type: list of tuples containing two floats
# newPoint: new point to be classified, type: tuple containing two flotas
# k: k value for k-NN classifier, type: int
# RETURNS: the predicted color using k-NN classifier, type: string (either 'blue' or 'red')
def classify(bluePoints, redPoints, newPoint, k):
   # The steps you need to follow:
   # 1. Calculate the euclidean-distance between the new point and other points (blue and red)
   # 2. Pick the closest k points to the new point
   # 3. Make a Majority Vote between these k-points
   # 4. Return the result

   dblue = []
   dred = []
   for i in range(len(bluePoints)):
      dblue.append(distance(bluePoints[i], newPoint))
   dblue = sorted(dblue)
   
   for n in range(len(redPoints)):
      dred.append(distance(redPoints[i], newPoint))
   dred = sorted(dred)



   n = 0
   blueIdx = 0
   redIdx = 0
   closest = []
   while(n < k):

      if blueIdx < len(dblue):
         blueDist = dblue[blueIdx]
      else:
         blueDist = float("inf")

      if redIdx < len(dred):
         redDist = dred[redIdx]
      else:
         redDist = float("inf")   

      if blueDist < redDist:
         closest.append("blue")
         blueIdx += 1
      else:
         closest.append("red")
         redIdx += 1

      n += 1


   winner = majority(closest)
 
   return winner

def main():
   win = GraphWin("K-NN Classifier", 500, 500)
 
   # Read blue points from blues.txt
   bluePoints = readPoints("blues.txt")
 
   # Plot blue points on win
   plotPoints(bluePoints, win, "Blue")
 
   # Read red points from reds.txt
   redPoints = readPoints("reds.txt")
 
   # Plot red points on win
   plotPoints(redPoints, win, "Red")
 
   # Ask user to input k for the k-NN classifier
   k = eval(raw_input("Input k for the k-NN classifier: "))
 
   # For every click on the win:
   while(True):
      print "Please click for the new point to be classified."
      winPoint = win.getMouse()
      point = (winPoint.getX(), winPoint.getY())
      color = classify(bluePoints, redPoints, point, k)
      print "This point is classified as:  " + color

      #    Plot the clicked point with its prediction (either blue or red)
      c = Circle(winPoint, 5)
      c.setFill(color)
      c.draw(win)
 


main()

