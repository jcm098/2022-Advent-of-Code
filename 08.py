# Day 1 - https://adventofcode.com/2022/day/8

#hint from Geoff Butler --- may need nearest neighbor algorithm or variation to solve

#create an array and look around to count totals of visible trees

import common as c
from pprint import pprint

debug = False

def checkEast(val, trees):
  eastVisible = False
  
  for tree in trees:
    # print('checkEast',val,tree, trees)
    if int(tree) >= int(val):
      eastVisible = False
      break
    else:
      eastVisible = True

  # print('eastVisible',eastVisible)
  
  return eastVisible

def colToRow(col, matrix):

  newRow = [*()]

  # print(matrix)
  for row in matrix:
    newRow.append(row[col])

  # print('colToRow',col,newRow)
  
  return newRow

def checkWest(val, trees):
  visible = False
  
  for tree in trees:
    # print('checkWest',val,tree, trees)
    if int(tree) >= int(val):
      visible = False
      break
    else:
      visible = True

  # print('westVisible',visible)
  
  return visible

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
  print("\ninitial PERIMETER visible tree count",visibleTrees)

  for rowLoop in range(1,totalRows-1):
    for colLoop in range(1,totalColumns-1):
      trees = []
      # visibleTrees += eligibleForATreehouse(rowLoop, colLoop, theForestMatrix, totalColumns, totalRows)
      # print(rowLoop, colLoop, theForestMatrix[rowLoop])
      if checkEast(theForestMatrix[rowLoop][colLoop], theForestMatrix[rowLoop][0:colLoop]):
        visibleTrees += 1
      elif checkWest(theForestMatrix[rowLoop][colLoop], theForestMatrix[rowLoop][colLoop+1:totalRows]):
        visibleTrees += 1
      elif checkEast(theForestMatrix[rowLoop][colLoop],colToRow(colLoop, theForestMatrix)[0:rowLoop]):
        visibleTrees += 1
      elif checkWest(theForestMatrix[rowLoop][colLoop],colToRow(colLoop, theForestMatrix)[rowLoop+1:totalColumns]):
        visibleTrees += 1
      # print(colToRow(colLoop,theForestMatrix))

  print("visible trees", visibleTrees)
  
  return visibleTrees

# *** PART 2 ***
#
#
#
#

def viewTrees(direction, val, trees):
  viewedTrees = 0
  # lastTreeSize = 0
  if (direction == 'left') or (direction == 'up'):
    reversedTrees = trees[::-1]
  else:
    reversedTrees = trees
  
  for tree in reversedTrees:
    # print('view',direction,val,tree, reversedTrees)
    if int(tree) < int(val):
      viewedTrees += 1
      # lastTreeSize = int(tree)
    elif int(tree) >= int(val):
      viewedTrees += 1
      break
    else:
      break

  # print('view',direction,'trees',viewedTrees)
  
  return viewedTrees

def part2(data):
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
  pprint(theForestMatrix)

  currentTreeSceneScore = 0
  for rowLoop in range(1,totalRows-1):
    for colLoop in range(1,totalColumns-1):
      treeSceneScore = 0
      # print('r',rowLoop, 'c',colLoop, theForestMatrix[rowLoop])

      
      treeSceneScore = viewTrees('left',\
                                 theForestMatrix[rowLoop][colLoop],\
                                 theForestMatrix[rowLoop][0:colLoop])
      treeSceneScore *= viewTrees('right',\
                                  theForestMatrix[rowLoop][colLoop],\
                                  theForestMatrix[rowLoop]\
                                  [colLoop+1:totalRows])
      treeSceneScore *= viewTrees('up',\
                                  theForestMatrix[rowLoop]\
                                  [colLoop],colToRow(colLoop,\
                                  theForestMatrix)\
                                  [0:rowLoop])
      treeSceneScore *= viewTrees('down',\
                                  theForestMatrix[rowLoop][colLoop]\
                                  ,colToRow(colLoop,\
                                  theForestMatrix)\
                                  [rowLoop+1:totalColumns])

      # print("treeSceneScore",treeSceneScore)
      if treeSceneScore > currentTreeSceneScore:
        currentTreeSceneScore = treeSceneScore

  print("scene score", currentTreeSceneScore)
  
  return 0

