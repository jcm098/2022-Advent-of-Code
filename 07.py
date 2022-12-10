# Day 1 - https://adventofcode.com/2022/day/7

#https://pythonguides.com/case-statement-in-python/
#https://www.tutorialspoint.com/python-convert-a-list-of-lists-into-tree-like-dict#
#https://stackoverflow.com/questions/54631623/build-a-tree-from-a-list
#https://stackoverflow.com/questions/444296/how-to-efficiently-build-a-tree-from-a-flat-structure
#https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd
#

import common as c
from pprint import pprint

#"constants"
rootDirectory = '/root/'

def getParentDirectory(currentDirectory):  
  parentDirectory = '/'
  directoryStructure = currentDirectory.split('/')

  for xLoop in range(len(directoryStructure)-2):
    if directoryStructure[xLoop] != '':
      parentDirectory = parentDirectory + directoryStructure[xLoop] + "/"
      
  # print(len(directoryStructure))
  
  return parentDirectory

def calibrateDirectorySizes(directoryInfo):

  # print('Calibration')

  for xLoop in range(directoryInfo[rootDirectory]["max dir level"],0,-1):
    # print(xLoop)
  
    for keys, values in directoryInfo.items():
      if directoryInfo[keys]["dir level"] == xLoop:
        # print(keys, values)
        parentDirectory = directoryInfo[keys]["parent dir"]
        directoryInfo[parentDirectory]["dir size"] += directoryInfo[keys]["dir size"]
      
  return 0

def computeTotalSize(directoryInfo, threshold):
  totalSize = 0
  
  for keys, values in directoryInfo.items():
    if directoryInfo[keys]["dir size"] <= threshold:
      totalSize += directoryInfo[keys]["dir size"]
  
  return totalSize

def findSmallestDirectoryToDelete(directoryInfo, spaceNeeded):
  totalSpaceUsed = directoryInfo[rootDirectory]["dir size"]
  unusedSpace = 70000000 - totalSpaceUsed
  missingSpace = spaceNeeded - unusedSpace
  dirToDelete = ""

  print(totalSpaceUsed, spaceNeeded, unusedSpace, missingSpace)
  
  for keys, values in directoryInfo.items():
    if values["dir size"] >= missingSpace:
      if dirToDelete == "":
        dirToDelete = keys
        print("first",keys,values["dir size"])
      elif values["dir size"] < directoryInfo[dirToDelete]["dir size"]:
        dirToDelete = keys
        print("override",keys,values["dir size"])
        
  print(directoryInfo[dirToDelete]["dir size"])
    # if directoryInfo[keys]["dir size"] <= threshold:
    #   totalSize += directoryInfo[keys]["dir size"]
  
  return dirToDelete

def part1(data):
  fileInfo = c.removeCommentLines(data,'#')
  currentDirectory = rootDirectory
  parentDirectory = ''
  directoryInfo = {
    "/root/": {"dir size":0, "dir level":0, "max dir level":0
      }  
  }

  for instructions in fileInfo:
    info = instructions.split(' ')

    # print(info)
    # print("cd = " + currentDirectory)
    
    if info[0] == '$':
      if info[1] == 'cd':
        if info[2] == '/':
          currentDirectory = rootDirectory
          currentDirLevel = 0
        elif info[2] == '..':
          currentDirectory = directoryInfo[currentDirectory]["parent dir"]
        else:
          currentDirectory = currentDirectory + info[2] + "/"
        # print(currentDirectory)
      elif info[1] == 'ls':
        pass
        # print('ls')
    elif info[0] == 'dir':
      # print('dir')
      directoryInfo[currentDirectory + info[1] + "/"] = {\
            "dir size":0,\
            "parent dir":currentDirectory,\
            "dir level":directoryInfo[currentDirectory]["dir level"]+1}
      if directoryInfo[currentDirectory]["dir level"]+1 > directoryInfo[rootDirectory]["max dir level"]:
        directoryInfo[rootDirectory]["max dir level"] = directoryInfo[currentDirectory]["dir level"]+1
    elif info[0].isnumeric():
      # print(info[0])
      # print(directoryInfo[currentDirectory])
      directoryInfo[currentDirectory][info[1]] = int(info[0])
      # print(directoryInfo)
      currentDirectorySize = directoryInfo[currentDirectory]["dir size"] + int(info[0])
      directoryInfo[currentDirectory]["dir size"] = currentDirectorySize
      # if parentDirectory != '':
      #   parentDirectorySize = directoryInfo[parentDirectory]["size"] + int(info[0])
      #   directoryInfo[parentDirectory]["size"] = parentDirectorySize
      # print(computeDirectorySize(directoryInfo[currentDirectory]))
      # directoryInfo[currentDirectory]["size"] = computeDirectorySize(directoryInfo[currentDirectory])
  
  # print("***")
  # pprint(directoryInfo)
  calibrateDirectorySizes(directoryInfo)
  # pprint(directoryInfo)

  print(computeTotalSize(directoryInfo,100000))
  
  return 0


def part2(data):
  fileInfo = c.removeCommentLines(data,'#')
  currentDirectory = rootDirectory
  parentDirectory = ''
  directoryInfo = {
    "/root/": {"dir size":0, "dir level":0, "max dir level":0
      }  
  }

  for instructions in fileInfo:
    info = instructions.split(' ')
    
    if info[0] == '$':
      if info[1] == 'cd':
        if info[2] == '/':
          currentDirectory = rootDirectory
          currentDirLevel = 0
        elif info[2] == '..':
          currentDirectory = directoryInfo[currentDirectory]["parent dir"]
        else:
          currentDirectory = currentDirectory + info[2] + "/"
      elif info[1] == 'ls':
        pass
    elif info[0] == 'dir':
      directoryInfo[currentDirectory + info[1] + "/"] = {\
            "dir name":info[1],\
            "dir size":0,\
            "parent dir":currentDirectory,\
            "dir level":directoryInfo[currentDirectory]["dir level"]+1}
      if directoryInfo[currentDirectory]["dir level"]+1 > directoryInfo[rootDirectory]["max dir level"]:
        directoryInfo[rootDirectory]["max dir level"] = directoryInfo[currentDirectory]["dir level"]+1
    elif info[0].isnumeric():
      directoryInfo[currentDirectory][info[1]] = int(info[0])
      currentDirectorySize = directoryInfo[currentDirectory]["dir size"] + int(info[0])
      directoryInfo[currentDirectory]["dir size"] = currentDirectorySize
  
  calibrateDirectorySizes(directoryInfo)
  pprint(directoryInfo)
  print(findSmallestDirectoryToDelete(directoryInfo,30000000))

  return 0
