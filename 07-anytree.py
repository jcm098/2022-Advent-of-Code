# Day 1 - https://adventofcode.com/2022/day/7

#https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd

import common as c
from anytree import Node, RenderTree

def part1(data):
  fileInfo = c.removeCommentLines(data,'#')

  fileStructure = Node("root")
  currentDirectory = fileStructure
  print(currentDirectory)
  
  for instructions in fileInfo:
      info = instructions.split(' ')
      
      if info[0] == '$':
        if info[1] == 'cd':
          if info[2] == '/':
            currentDirectory = fileStructure
          elif info[2] == '..':
            print(currentDirectory)
            currentDirectory = currentDirectory.parent
            pass
          else:
            print('*')
            print(currentDirectory.descendants)
            # currentDirectory = currentDirectory.descendants.count()
            # print(currentDirectory)
            pass
        elif info[1] == 'ls':
          pass
      elif info[0] == 'dir':
        Node(info[1],parent=currentDirectory)
        
        for pre, fill, node in RenderTree(fileStructure):
          print("%s%s" % (pre, node.name))
      elif info[0].isnumeric():
        # directoryInfo[currentDirectory][info[1]] = int(info[0])
        # currentDirectorySize = directoryInfo[currentDirectory]["size"] + int(info[0])
        # directoryInfo[currentDirectory]["size"] = currentDirectorySize
        pass

  for pre, fill, node in RenderTree(fileStructure):
      print("%s%s" % (pre, node.name))
  
  return 0


def part2(data):
  inputData = c.removeCommentLines(data,'#')

  return 0
