# Day 1 - https://adventofcode.com/2022/day/8

#hint from Geoff Butler --- may need nearest neighbor algorithm or variation to solve

#create an array and look around to count totals of visible trees

import common as c
from pprint import pprint

debug = False

def eligibleForATreehouse(treeRow,treeCol,forestMatrix,maxCol,maxRow):

  visibleFromTheWest = False
  visibleFromTheEast = False
  visibleFromTheNorth = False
  visibleFromTheSouth = False
  
  #From the West (ie. left to right)
  # print('*** West',treeRow,treeCol)
  for col in range(treeCol):
    # print("r",treeRow,"c",treeCol,"colLoop",col,"size",forestMatrix[treeRow][treeCol],"comp",forestMatrix[treeRow][col])
    if forestMatrix[treeRow][col] < forestMatrix[treeRow][treeCol]:
      # print("true")
      visibleFromTheWest = True
    else:
      visibleFromTheWest = False

  if visibleFromTheWest:
    # print("r",treeRow,"c",treeCol,"west", visibleFromTheWest, forestMatrix[treeRow][treeCol])
    return True

  #From the East (ie. right to left)
  # print('*** East',treeRow,treeCol)
  for col in range(maxCol-1,treeCol,-1):
    # print("r",treeRow,"c",treeCol,"colLoop",col,"size",forestMatrix[treeRow][treeCol],"comp",forestMatrix[treeRow][col])
    if forestMatrix[treeRow][col] < forestMatrix[treeRow][treeCol]:
      # print("true")
      visibleFromTheEast = True
    else:
      visibleFromTheEast = False

  if visibleFromTheEast:
    # print("r",treeRow,"c",treeCol,"east", visibleFromTheEast, forestMatrix[treeRow][treeCol])
    return True

  #From the North (ie. top to bottom)
  # print('*** North',treeRow,treeCol)
  for row in range(treeRow):
    # print("r",treeRow,"c",treeCol,"rowLoop",row,"size",forestMatrix[treeRow][treeCol],"comp",forestMatrix[row][treeCol])
    if forestMatrix[row][treeCol] < forestMatrix[treeRow][treeCol]:
      # print("true")
      visibleFromTheNorth = True
    else:
      # print("false")
      visibleFromTheNorth = False
      break

  if visibleFromTheNorth:
    # print("r",treeRow,"c",treeCol,"north", visibleFromTheNorth, forestMatrix[treeRow][treeCol])
    return True

  #From the South (ie. bottom to top)
  # print('*** North',treeRow,treeCol)
  for row in range(maxRow-1,treeRow,-1):
    # print("r",treeRow,"c",treeCol,"rowLoop",row,"size",forestMatrix[treeRow][treeCol],"comp",forestMatrix[row][treeCol])
    if forestMatrix[row][treeCol] < forestMatrix[treeRow][treeCol]:
      # print("true")
      visibleFromTheSouth = True
    else:
      # print("false")
      visibleFromTheSouth = False
      break

  if visibleFromTheSouth:
    # print("r",treeRow,"c",treeCol,"south", visibleFromTheSouth, forestMatrix[treeRow][treeCol])
    return True
  
  return False

def part1(data):
  theForestData = c.removeCommentLines(data,'#')
  theForestMatrix = []
  totalRows = 0
  totalColumns = 0
  visibleTrees = 0
  visibleInternalTreeSet = {*()}
  
  if debug: print('theForestData',theForestData)
  #convert Forest data to a matrix
  for forestRow in theForestData:
    
    #get matrix dimensions
    if debug: print("forest row length",len(forestRow))
    totalRows += 1
    if totalColumns == 0:
      totalColumns = len(forestRow)
    elif totalColumns != len(forestRow):
      print("column mismatch", totalColumns, len(forestRow))

    #build the forest matrix
    rowList = []
    if debug: pprint(theForestMatrix)
    for columnLoop in range(totalColumns):
      # print(totalRows-1,columnLoop,forestRow[columnLoop])
      rowList.append(forestRow[columnLoop])
    # print(rowList,len(rowList))
    theForestMatrix.append(rowList)

  print("totalColumns",totalColumns,"totalRows",totalRows,len(theForestMatrix))
  # pprint(theForestMatrix)
    
  #determine visible trees from PERIMETER
  visibleTrees += ((totalRows-1)*2) + ((totalColumns-1)*2)
  print("ninitial PERIMETER visible tree count",visibleTrees)

  for rowLoop in range(1,totalRows-1):
    for colLoop in range(1,totalColumns-1):
      visibleTrees += eligibleForATreehouse(rowLoop, colLoop, theForestMatrix, totalColumns, totalRows)

  print("visible trees", visibleTrees)
  
  return visibleTrees


def part2(data):
  inputData = c.removeCommentLines(data,'#')

  return 0
