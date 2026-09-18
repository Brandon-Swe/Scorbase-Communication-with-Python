
# This file is meant for recieving and sending back points 
#   (The actual adjustments will be done by the simulation, so this just to recieve and send back)

def pointCatch():
   
    with open("NewPoint.vbs", "r") as pointRead:
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
            tempList[1] = int(tempList[1])      #turning the string numbers to integers
            pointList.append(tempList)

    return(pointList)

def PointSender(argPoint):

    argPoint[0][1] = 0          # turns the fromScor to 0 so scorbase knows the point is usable

    with open("NewPoint.vbs", "w") as pointWrite:
       for coord in argPoint:
           pointWrite.write(coord[0] + " = " + str(coord[1]) + "\n") # rewrites to the vbs file

point = pointCatch()
# make the necessary edits to the point and then return it
point[1][1] = 10513
point[2][1] = 12939
point[3][1] = 1450
point[4][1] = 221
PointSender(point)