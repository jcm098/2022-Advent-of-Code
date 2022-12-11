# Day 1 - https://adventofcode.com/2022/day/9

#file is movement of a rope head, tail follows and must be underneath, next to, or diagonal to head
#base function loops through instructions
#function to move head, function for tail to follow, track movements

import common as c
from pprint import pprint

debugProd = False
debugDev = True

def moveRopeHead(movement, trace, knotCount):
  direction = ''
  distance = 0
  directionAdjustX = 0
  directionAdjustY = 0
  
  # if debugDev: pprint(movement)

  direction = movement.split(' ')[0]
  distance = int(movement.split(' ')[1])

  if direction == 'R':
    directionAdjustX = 1
  elif direction == 'L':
    directionAdjustX = -1
  elif direction == 'U':
    directionAdjustY = 1
  elif direction == 'D':
    directionAdjustY = -1
  
  currentHeadX = int(trace[0][len(trace[0])-1].split(':')[0])
  currentHeadY = int(trace[0][len(trace[0])-1].split(':')[1])

  # if debugDev: print("\ndir", direction, "distance", distance)
  # if debugDev: print("start pos", "x", currentHeadX, "y", currentHeadY)

  for moveLoop in range(distance):
    currentHeadX += directionAdjustX
    currentHeadY += directionAdjustY
    trace[0].append(str(currentHeadX) + ':' + str(currentHeadY))

    currentParentX = currentHeadX
    currentParentY = currentHeadY
    for tailLoop in range(knotCount):
      moveRopeTail(currentParentX, currentParentY, trace, tailLoop+1)
      currentParentX = int(trace[tailLoop+1][len(trace[tailLoop+1])-1].split(':')[0])
      currentParentY = int(trace[tailLoop+1][len(trace[tailLoop+1])-1].split(':')[1])

  # if debugDev: print("end pos", "x", currentHeadX, "y", currentHeadY)
      
  return 0

def moveRopeTail(headX, headY, trace, knotposition):
  currentHeadPos = [*()]
  priorityHeadPos = [*()]
  diagonalHeadPos = [*()]
  currentTailPos = [*()]
  potentialTailPos = [*()]

  #set potential tail positions around the head
  currentHeadPos.append(str(headX) + ':' + str(headY)) #spot on
  priorityHeadPos.append(str(headX+1) + ':' + str(headY)) #right
  priorityHeadPos.append(str(headX) + ':' + str(headY+1)) #above
  diagonalHeadPos.append(str(headX+1) + ':' + str(headY+1)) #right and above
  
  # if (headX-1) >= 0:
  priorityHeadPos.append(str(headX-1) + ':' + str(headY)) #left
  diagonalHeadPos.append(str(headX-1) + ':' + str(headY+1)) #left and above
  # if (headY-1) >= 0:
  priorityHeadPos.append(str(headX) + ':' + str(headY-1)) #below
  diagonalHeadPos.append(str(headX+1) + ':' + str(headY-1)) #right and below
  # if ((headX-1) >= 0) and ((headY-1) >= 0):
  diagonalHeadPos.append(str(headX-1) + ':' + str(headY-1)) #left and below
    
  #find possible areas around X then check if already in it
  #if not, move to most optimal spot
  currentX = int(trace[knotposition][len(trace[knotposition])-1].split(':')[0])
  currentY = int(trace[knotposition][len(trace[knotposition])-1].split(':')[1])

  #set potential tail positions based on current location
  currentTailPos.append(str(currentX) + ':' + str(currentY)) #spot on
  potentialTailPos.append(str(currentX+1) + ':' + str(currentY)) #right
  potentialTailPos.append(str(currentX) + ':' + str(currentY+1)) #above
  potentialTailPos.append(str(currentX+1) + ':' + str(currentY+1)) #right and above
  
  # if (currentX-1) >= 0:
  potentialTailPos.append(str(currentX-1) + ':' + str(currentY)) #left
  potentialTailPos.append(str(currentX-1) + ':' + str(currentY+1)) #left and above
  # if (currentY-1) >= 0:
  potentialTailPos.append(str(currentX) + ':' + str(currentY-1)) #below
  potentialTailPos.append(str(currentX+1) + ':' + str(currentY-1)) #right and below
  # if ((currentX-1) >= 0) and ((currentY-1) >= 0):
  potentialTailPos.append(str(currentX-1) + ':' + str(currentY-1)) #left and below

  # if debugDev: 
  #   print("\n---potential head pos around head")
  #   print("currentHeadPos", currentHeadPos)
  #   print("priorityHeadPos", priorityHeadPos)
  #   print("diagonalHeadPos", diagonalHeadPos)
  #   print("---potential tail pos next to head")
  #   print("currentTailPos", currentTailPos)
  #   print("potentialTailPos", potentialTailPos)

  #find best movement
  #https://stackoverflow.com/questions/3697432/how-to-find-list-intersection

  #if tail is alread in one of the potential positions, do not move
  if len(list(set(currentTailPos) & set(currentHeadPos))) > 0:
    # print("tail is in same position as the head")
    trace[knotposition].append(currentTailPos[0])
  elif len(list(set(currentTailPos) & set(priorityHeadPos))) > 0:
    # print("tail is in a priority position")
    trace[knotposition].append(currentTailPos[0])
  elif len(list(set(currentTailPos) & set(diagonalHeadPos))) > 0:
    # print("tail is in a diagonal position")
    trace[knotposition].append(currentTailPos[0])
  #move to a priority position if available
  elif len(list(set(potentialTailPos) & set(priorityHeadPos))) > 0:
    # print("moving tail to a priority position")
    trace[knotposition].append(list(set(potentialTailPos) & set(priorityHeadPos))[0])
  elif len(list(set(potentialTailPos) & set(diagonalHeadPos))) > 0:
    # print("moving tail to a diagonal position")
    trace[knotposition].append(list(set(potentialTailPos) & set(diagonalHeadPos))[0])
    # print("spot on",list(set(potentialTailPos) & set(currentHeadPos)))
    # print("priority movement",list(set(potentialTailPos) & set(priorityHeadPos)))

  return 0

def positionsNextToHead(headX, headY):
  positions = [*()]

  #same position
  positions.append(str(headX) + ':' + str(headY))

  #above

  return positions

def part1(data):
  movementData = c.removeCommentLines(data,'#')
  movementTrace = [['0:0'],['0:0']]

  # if debugDev: pprint(movementData)
  # if debugDev: print("start movement",movementTrace)

  for movement in movementData:
    moveRopeHead(movement, movementTrace,1)
  
  # if debugDev: 
  #   print("end movement",movementTrace)
  #   print("len head", len(movementTrace[0]))
  #   print("len tail", len(movementTrace[1]))

  #https://datagy.io/python-count-unique-values-list/
  #get unique locations

  print("unique head locations",len(set(movementTrace[0])))
  print("unique tail locations",len(set(movementTrace[1])))
  
  return 0


def part2(data):
  movementData = c.removeCommentLines(data,'#')
  movementTrace = [['0:0'],['0:0'],\
                  ['0:0'],['0:0'],\
                  ['0:0'],['0:0'],\
                  ['0:0'],['0:0'],\
                  ['0:0'],['0:0']]

  # if debugDev: pprint(movementData)
  # if debugDev: print("start movement",movementTrace)

  for movement in movementData:
    moveRopeHead(movement, movementTrace,9)
  
  # if debugDev: 
  #   print("end movement",movementTrace)
  #   print("len head", len(movementTrace[0]))
  #   print("len tail", len(movementTrace[9]))

  #https://datagy.io/python-count-unique-values-list/
  #get unique locations

  pprint(movementTrace)
  print("unique head locations",len(set(movementTrace[0])))
  print("unique tail locations",len(set(movementTrace[9])))
  
  return 0
