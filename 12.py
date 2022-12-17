# Day 1 - https://adventofcode.com/2022/day/12

# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
# https://www.delftstack.com/howto/python/python-adjacency-matrix/
# followed this >>> https://likegeeks.com/python-dijkstras-algorithm/

import common as c
from pprint import pprint
from numpy import inf

def buildCosts(startPoint, rows, cols):
  costs = {startPoint: 0}

  for row in range(rows):
    for col in range(cols):
      currentLoc = 'R'+str(row)+'C'+str(col)
      if currentLoc == startPoint: continue

      costs[currentLoc] = inf
      
  return costs

def getGraphDistances(row, col, data):
  #map alphabet to numbers  
  elevations = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
    'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
    's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
    'y': 25, 'z': 26, 'S': 1, 'E': 26
  }

  # pprint(elevations)
  
  distances = {}
  mapRowCount = len(data)
  mapColCount = len(data[1])
  currentElev = data[row][col]
  currentLoc = 'R' + str(row) + 'C' + str(col)
  
  #above
  if row > 0:
    checkDistance = 0
    checkElev = data[row - 1][col]
    checkLoc = 'R' + str(row - 1) + 'C' + str(col)
    checkDistance = calcCheckDistance(checkElev, currentElev, elevations)
    if checkDistance != 0:
      distances[checkLoc] = checkDistance

  #below
  if row < (mapRowCount - 1):
    # print(row, col, mapRowCount, data[row+1][col])
    checkDistance = 0
    checkElev = data[row + 1][col]
    checkLoc = 'R' + str(row + 1) + 'C' + str(col)
    checkDistance = calcCheckDistance(checkElev, currentElev, elevations)
    if checkDistance != 0:
      distances[checkLoc] = checkDistance

  #left
  if col > 0:
    checkDistance = 0
    checkElev = data[row][col - 1]
    checkLoc = 'R' + str(row) + 'C' + str(col - 1)
    checkDistance = calcCheckDistance(checkElev, currentElev, elevations)
    if checkDistance != 0:
      distances[checkLoc] = checkDistance
      
  #right
  if col < (mapColCount - 1):
    checkDistance = 0
    checkElev = data[row][col + 1]
    checkLoc = 'R' + str(row) + 'C' + str(col + 1)
    checkDistance = calcCheckDistance(checkElev, currentElev, elevations)
    if checkDistance != 0:
      distances[checkLoc] = checkDistance
  
  return distances

def calcCheckDistance(checkElev, currentElev, elevations):
  checkDistance = 0

  if elevations[checkElev] == elevations[currentElev]:
    checkDistance = 2
  elif (elevations[currentElev] + 1) == elevations[checkElev]:
    checkDistance = 3
  elif elevations[currentElev] > elevations[checkElev]:
    checkDistance = 1
  
  return checkDistance

def search(source, target, graph, costs, parents):
    nextNode = source
    while nextNode != target:
        for neighbor in graph[nextNode]:
            if(neighbor in costs):
              pass
            else:
              continue
            # print(neighbor, nextNode, source)
            # print(graph[nextNode])
            # pprint(graph[nextNode][neighbor])
            # pprint(costs)
            # pprint(costs[nextNode])
            # pprint(costs[neighbor])
            # pprint(parents)
            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                parents[neighbor] = nextNode
            #     print('x1')
            # print('x2', neighbor, nextNode)
            # print('x2.1',graph[neighbor])
            if nextNode in graph[neighbor]:
              del graph[neighbor][nextNode]
            else:
              pass
            # print('x3')
        del costs[nextNode]
        nextNode = min(costs, key=costs.get)
    return parents

def backpedal(source, target, searchResult):
    node = target
    backpath = [target]
    path = []

    if(node in searchResult):
      pass
    else:
      return path
  
    while node != source:
        backpath.append(searchResult[node])
        node = searchResult[node]
    for i in range(len(backpath)):
        path.append(backpath[-i - 1])
    return path

def getGraph(inputData):
  graph = {}

  mapRowCount = len(inputData)
  mapColCount = len(inputData[1])

  for row in range(mapRowCount):
    for col in range(mapColCount):
      currentLoc = 'R'+str(row)+'C'+str(col)
      graph[currentLoc] = getGraphDistances(row, col, inputData)

  return graph

def part1(data, startPoint=''):
  graph = {}
  costs = {}
  parents = {}
  endPoint = ''
  
  inputData = c.removeCommentLines(data,'#')

  graph = getGraph(inputData)
  
  mapRowCount = len(inputData)
  mapColCount = len(inputData[1])

  # if startPoint != '':
  #   # build costs based on new startpoint
  #   costs = buildCosts(startPoint, mapRowCount, mapColCount)
  
  for row in range(mapRowCount):
    for col in range(mapColCount):
      currentLoc = 'R'+str(row)+'C'+str(col)
      if (inputData[row][col] == 'S') and startPoint == '':
        startPoint = currentLoc
        # startPoint = 'R0C8'
      elif inputData[row][col] == 'E':
        endPoint = currentLoc
    

  # pprint(inputData)
  # pprint(graph)
  # pprint(costs)
  # print(mapRowCount, mapColCount, startPoint, endPoint)
  costs = buildCosts(startPoint, mapRowCount, mapColCount)
  result = search(startPoint, endPoint, graph, costs, parents)
  # print('parent dictionary={}'.format(result))

  if(endPoint in result):
    pass
  else:
    return -1

  # print(startPoint, endPoint, len(result), result[endPoint])
  shortestPath = backpedal(startPoint, endPoint, result)
  # print(len(shortestPath), 'shortest path={}'.format(shortestPath))

  # print('xxx', shortestPath[0], shortestPath[len(shortestPath)-1])
  
  return len(shortestPath)-1


def part2(data):
  paths = [*()]
  pathLengths =[*()]
  startPoint = ''
  currentLoc = ''
  currentElev = ''
  inputData = c.removeCommentLines(data,'#')

  mapRowCount = len(inputData)
  mapColCount = len(inputData[1])

  # print(part1(data, 'R0C8'))
  # return 0

  #assume starting on the edges
  for row in range(mapRowCount):
    for col in range(mapColCount):
      if (row == 0) or (row == mapRowCount - 1):
        pass
      elif (col == 0) or (col == mapColCount - 1):
        pass
      else:
        continue
        
      currentLoc = 'R'+str(row)+'C'+str(col)
      currentElev = inputData[row][col]
      if currentElev == 'S' or currentElev == 'a':
        startPoint = currentLoc
        currentLen = part1(data, startPoint)
        if currentLen > 0: paths.append(currentLen)
        print(startPoint, currentLen)
  
  for path in paths:
    pathLengths.append(path)

  pathLengths.sort()
  pprint(pathLengths)
  
  return pathLengths[0]
