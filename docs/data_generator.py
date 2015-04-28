from graphics import *
from utility import *
import random

# Generates a random 2D points.
# meanX: mean of X-axis of the underlying normal distribution, type: int
# meanY: mean of Y-axis of the underlying normal distribution, type: int
# sigmaX: standard deviation on X-axis, type: int
# sigmaY: standard deviation on Y-axis, type: int
# RETURNS: x and y value of the random point, type: tuple containing two floats
def generatePoint(meanX, meanY, sigmaX, sigmaY):

   x = random.gauss(meanX, sigmaX)
   y = random.gauss(meanY, sigmaY)
   xy = [x,y]

   return (xy)
   
# Generates multiple random points using generatePoint() function.
# meanX: mean of X-axis of the underlying normal distribution, type: int
# meanY: mean of Y-axis of the underlying normal distribution, type: int
# sigmaX: standard deviation on X-axis, type: int
# sigmaY: standard deviation on Y-axis, type: int
# numPoints: how many number of points will be generated, type: int
# RETURNS: list of random points, type: list of tuples containing two floats
def generatePoints(meanX, meanY, sigmaX, sigmaY, numPoints):

   rplist = []
   for i in range(numPoints):
      rplist.append(generatePoint(meanX, meanY, sigmaX, sigmaY))

   return rplist


def main():
   win = GraphWin("Data Collector", 500, 500)
 
   # Ask user to click on window for meanX and meanY for blue samples
   print("Click on window for meanX and meanY for blue samples")
   point = win.getMouse()
   meanX = point.getX()
   meanY = point.getY()
   # Ask user to input sigmaX and sigmaY for blue samples
   sigmaX = eval(raw_input("Input sigmaX for blue samples: "))
   sigmaY = eval(raw_input("Input sigmaY for blue samples: "))
 
   # Ask user to input how many blue samples?
   blue = eval(raw_input("Input number of blue samples: "))
    
   # Generate blue samples with given information
   bpoints = generatePoints(meanX, meanY, sigmaX, sigmaY, blue)
   
   # Plot these blue samples on window using utility functions
   plotPoints(bpoints, win, "Blue")
 
   # Write these blue samples on blues.txt using utility functions
   savePoints(bpoints, "blues.txt")
 
   # Ask user to click on window for meanX and meanY for red samples
   print("Click on window for meanX and meanY for red samples")
   point = win.getMouse()
   meanX = point.getX()
   meanY = point.getY()
 
   # Ask user to input sigmaX and sigmaY for red samples
   sigmaX = eval(raw_input("Input sigmaX for red samples: "))
   sigmaY = eval(raw_input("Input sigmaY for red samples: "))
   
   # Ask user to input how many red samples?
   red = eval(raw_input("Input number of red samples: "))
 
   # Generate red samples with given information
   rpoints = generatePoints(meanX, meanY, sigmaX, sigmaY, red)
 
   # Plot these red samples on window using utility functions
   plotPoints(rpoints, win, "Red")
   
   # Write these red samples on reds.txt using utility functions
   savePoints(rpoints, "reds.txt")
   win.getMouse()
   win.close()
   
main()
