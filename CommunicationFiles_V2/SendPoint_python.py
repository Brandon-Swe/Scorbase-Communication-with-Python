
# This file is meant for recieving and sending back points 
#   (The actual adjustments will be done by the analytics engine, so this just to recieve and send back)

# What it reads and writes to looks like this:
# fromScor = --
# x = --
# y = --
# z = --
# roll = --

from watchfiles import watch
import threading
import queue

currPosStorageFile = "SendPoint_varTxt.vbs"
pointStorageFile = "points.txt"

def pointCatch():
   
    with open(currPosStorageFile, "r") as pointRead:
        pointString = pointRead.read()

    # parse to get position
    pointLineSplit = pointString.splitlines()

    pointList = []
    for coord in pointLineSplit:
        if coord[0] == "'":         #ignoring comments in file
            #pointList.append(coord)    #uncomment if want to keep comments in vbs file from python side
            continue
        else:
            tempList = coord.split(" = ")
            tempList[1] = int(tempList[1])      # turning the string numbers to integers
            pointList.append(tempList)

    return(pointList)

def PointSender(argPoint):

    argPoint[0][1] = 0          # turns the fromScor to 0 so scorbase knows the point is usable

    with open(currPosStorageFile, "w") as pointWrite:
       for coord in argPoint:
           # rewrites the new coordinates to the vbs file
           pointWrite.write(coord[0] + " = " + str(coord[1]) + "\n") 

#points = queue.Queue()
def pointRecord():

    #points = []
    with open(pointStorageFile, "w") as file:
        file.write("erased previous points\n")

    for changes in watch(currPosStorageFile):
        #points.append(pointCatch())
        print("Point Caught")
        tempPoint = pointCatch()
        with open(pointStorageFile, "a") as file:   
            file.write(str(tempPoint))
            file.write("\n")

#threading.Thread(target=pointRecord).start()
#print(points)

point = pointCatch()
# make the necessary edits to the point and then return it
point[1][1] = 66128
point[2][1] = 5882
point[3][1] = 48618
point[4][1] = 8915
PointSender(point)