# Day 1 - https://adventofcode.com/2022/day/8

#hint from Geoff Butler --- may need nearest neighbor algorithm or variation to solve

#create an array and look around to count totals of visible trees

#NOTE --- this did not work because I started out looking in, rather than starting at each tree and looking out (maybe)

import common as c
from pprint import pprint

debug = False

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

  #determine visible trees from LEFT
  if debug: print("\n*** LEFT ***")
  if debug: pprint(theForestMatrix)
  for rowLoop in range(1,totalRows-1):
    for colLoop in range(1,totalColumns):
      # print("row",rowLoop+1,"col",colLoop+1)
      # if debug: print(theForestMatrix[rowLoop][colLoop])
      if theForestMatrix[rowLoop][colLoop] == theForestMatrix[rowLoop][colLoop-1]:
        pass
      elif theForestMatrix[rowLoop][colLoop] > theForestMatrix[rowLoop][colLoop-1]:
        if debug: print("row",rowLoop+1,"column", colLoop+1,"height",theForestMatrix[rowLoop][colLoop],"prior height",theForestMatrix[rowLoop][colLoop-1])
        visibleInternalTreeSet.add('R'+str(rowLoop+1)+'C'+str(colLoop+1))
      else:
        if debug: print("break at " + 'R'+str(rowLoop+1)+'C'+str(colLoop+1))
        break

  if debug: print("plus LEFT visible internal trees",visibleInternalTreeSet)

  #determine visible trees from RIGHT
  if debug: print("\n*** RIGHT ***")
  if debug: pprint(theForestMatrix)
  for rowLoop in range(1,totalRows-1):
    for colLoop in range(totalColumns-2,0,-1):
      # print("row",rowLoop+1,"col",colLoop+1)
      # if debug: print(theForestMatrix[rightRowLoop][rightColumnLoop])
      if theForestMatrix[rowLoop][colLoop] == theForestMatrix[rowLoop][colLoop+1]:
        pass
      elif theForestMatrix[rowLoop][colLoop] > theForestMatrix[rowLoop][colLoop+1]:
        if debug: print("row",rowLoop+1,"column", colLoop+1,"height",theForestMatrix[rowLoop][colLoop],"prior height",theForestMatrix[rowLoop][colLoop+1])
        visibleInternalTreeSet.add('R'+str(rowLoop+1)+'C'+str(colLoop+1))
      else:
        if debug: print("break at " + 'R'+str(rowLoop+1)+'C'+str(colLoop+1))
        break

  if debug: print("plus RIGHT visible internal trees",visibleInternalTreeSet)

  #determine visible trees from TOP
  if debug: print("\n*** TOP ***")
  if debug: pprint(theForestMatrix)
  for colLoop in range(1,totalColumns-1):
    # print("column/TOP",colLoop)
    for rowLoop in range(1,totalRows):
      # print("col",colLoop+1,"row",rowLoop+1)
      # if debug: print(theForestMatrix[topRowLoop][topColumnLoop])
      if theForestMatrix[rowLoop][colLoop] == theForestMatrix[rowLoop-1][colLoop]:
        pass
      if theForestMatrix[rowLoop][colLoop] > theForestMatrix[rowLoop-1][colLoop]:
        if debug: print("row",rowLoop+1,"column", colLoop+1,"height",theForestMatrix[rowLoop][colLoop],"prior height",theForestMatrix[rowLoop-1][colLoop])
        # print("R",rowLoop,"C",colLoop)
        visibleInternalTreeSet.add('R'+str(rowLoop+1)+'C'+str(colLoop+1))
      else:
        if debug: print("break at col",colLoop+1,"row",rowLoop+1)
        break

  if debug: print("plus TOP visible internal trees",visibleInternalTreeSet)

  #determine visible trees from BOTTOM
  if debug: print("\n*** BOTTOM ***")
  if debug: pprint(theForestMatrix)
  for colLoop in range(1,totalColumns-1):
    # print("column/BOTTOM",colLoop)
    for rowLoop in range(totalRows-2,-1,-1):
      # if debug: print(theForestMatrix[rowLoop][colLoop])
      if theForestMatrix[rowLoop][colLoop] > theForestMatrix[rowLoop+1][colLoop]:
        if debug: print("row",rowLoop,"column", colLoop,"height",theForestMatrix[rowLoop][colLoop],"prior height",theForestMatrix[rowLoop+1][colLoop])
        visibleInternalTreeSet.add('R'+str(rowLoop+1)+'C'+str(colLoop+1))
      else:
        if debug: print("break at col",colLoop+1,"row",rowLoop+1)
        break

  # print("plus BOTTOM visible internal trees",visibleInternalTreeSet)

  print("inside trees",len(visibleInternalTreeSet))

  visibleTrees += len(visibleInternalTreeSet)

  print("visible trees", visibleTrees)
  
  return visibleTrees


def part2(data):
  inputData = c.removeCommentLines(data,'#')

  return 0
