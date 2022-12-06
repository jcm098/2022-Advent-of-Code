# Day 1 - https://adventofcode.com/2022/day/6
import common as c


def part1(data):
  stacks = ['V','C','D','R','Z','G','B','W'],\
            ['G','W','F','C','B','S','T','V'],\
            ['C','B','S','N','W'],\
            ['Q','G','M','N','J','V','C','P'],\
            ['T','S','L','F','D','H','B'],\
            ['J','V','T','W','M','N'],\
            ['P','F','L','C','S','T','G'],\
            ['B','D','Z'],\
            ['M','N','Z','W']
  
  instructions = c.removeCommentLines(data,'#')

  for movement in instructions:
    preciseMovements = movement.split(' ')

    moveFrom = int(preciseMovements[3])-1
    moveTo = int(preciseMovements[5])-1

    # print(preciseMovements)
    # print(stacks[moveFrom])
    # print(stacks[moveTo])
    
    for xLoop in range(int(preciseMovements[1])):
      itemToMove = c.popFromSet(stacks[moveFrom])
      # print(itemToMove)
      stacks[moveTo].append(itemToMove)
    # print(preciseMovements)

    # print(stacks[moveFrom])
    # print(stacks[moveTo])

  topStacks = stacks[0][len(stacks[0])-1] +\
              stacks[1][len(stacks[1])-1] +\
              stacks[2][len(stacks[2])-1] +\
              stacks[3][len(stacks[3])-1] +\
              stacks[4][len(stacks[4])-1] +\
              stacks[5][len(stacks[5])-1] +\
              stacks[6][len(stacks[6])-1] +\
              stacks[7][len(stacks[7])-1] +\
              stacks[8][len(stacks[8])-1]

  print(stacks)
  print(topStacks)

  return topStacks


def part2(data):
  stacks = ['V','C','D','R','Z','G','B','W'],\
            ['G','W','F','C','B','S','T','V'],\
            ['C','B','S','N','W'],\
            ['Q','G','M','N','J','V','C','P'],\
            ['T','S','L','F','D','H','B'],\
            ['J','V','T','W','M','N'],\
            ['P','F','L','C','S','T','G'],\
            ['B','D','Z'],\
            ['M','N','Z','W']
  
  instructions = c.removeCommentLines(data,'#')

  for movement in instructions:
    preciseMovements = movement.split(' ')

    moveFrom = int(preciseMovements[3])-1
    moveTo = int(preciseMovements[5])-1
    tempItems = []

    # print(preciseMovements)
    # print(stacks[moveFrom])
    # print(stacks[moveTo])
    
    for xLoop in range(int(preciseMovements[1])):
      itemToMove = c.popFromSet(stacks[moveFrom])
      # print(itemToMove)
      tempItems.append(itemToMove)
    # print(preciseMovements)

    # print(stacks[moveFrom])
    # print(stacks[moveTo])

    for xLoop in range(len(tempItems)):
      itemToMove = c.popFromSet(tempItems)

      stacks[moveTo].append(itemToMove)
  
  topStacks = stacks[0][len(stacks[0])-1] +\
              stacks[1][len(stacks[1])-1] +\
              stacks[2][len(stacks[2])-1] +\
              stacks[3][len(stacks[3])-1] +\
              stacks[4][len(stacks[4])-1] +\
              stacks[5][len(stacks[5])-1] +\
              stacks[6][len(stacks[6])-1] +\
              stacks[7][len(stacks[7])-1] +\
              stacks[8][len(stacks[8])-1]

  print(stacks)
  print(topStacks)

  return topStacks
