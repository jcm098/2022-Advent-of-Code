# Day 1 - https://adventofcode.com/2022/day/10

# loop through all of the instructions and add to a nested dictionary
#  then loop through the dictionary and calculate the totals

import common as c
from pprint import pprint


def part1(data):
  cpuInstructions = {}
  currentCycle = 0
  totalCycles = 1
  xRegister = [*()]
  inputData = c.removeCommentLines(data,'#')
  
  # create the dictionary
  for index, instruction in enumerate(inputData, start=1):
    parameters = instruction.split(' ')
    if len(parameters) == 1: parameters.append(0)
    cpuInstructions[index] = {}
    cpuInstructions[index]["instruction"] = parameters[0]
    cpuInstructions[index]["instructionParm"] = int(parameters[1])

    if parameters[0] == 'noop':
      totalCycles += 1
    elif parameters[0] == 'addx':
      totalCycles += 2

  # build empty register of total cycles
  for xLoop in range(totalCycles):
    xRegister.append(0)

  # initial register value is 1
  xRegister[0] = 1
  
  # run the calculations
  for instruction in cpuInstructions:
    print(cpuInstructions[instruction]["instruction"])
    if cpuInstructions[instruction]["instruction"] == 'noop':
      currentCycle += 1
      xRegister[currentCycle] += xRegister[currentCycle-1]
    elif cpuInstructions[instruction]["instruction"] == 'addx':
      currentCycle += 1
      xRegister[currentCycle] += xRegister[currentCycle-1]
      currentCycle += 1
      xRegister[currentCycle] += xRegister[currentCycle-1]
      xRegister[currentCycle] += cpuInstructions[instruction]["instructionParm"]
      
    # pprint(cpuInstructions[instruction]["instruction"])
  
  pprint(inputData)
  pprint(cpuInstructions)
  pprint(xRegister)
  print('totalCycles', totalCycles)

  if totalCycles >= 220:
    signalSum = 0
    for xLoop in range(20,221,40):
      print('cycle', xLoop, 'register', xRegister[xLoop-1],\
              'signal', xRegister[xLoop-1] * xLoop)
      signalSum += xRegister[xLoop-1] * xLoop
    print('signal sum', signalSum)
      
    # print('\n')
    # print('20th cycle ', xRegister[20-1], xRegister[20-1]*20)
    # print('60th cycle ', xRegister[60-1], xRegister[60-1]*60)
    # print('100th cycle', xRegister[100-1], xRegister[100-1]*100)
    # print('140th cycle', xRegister[140-1], xRegister[140-1]*140)
    # print('180th cycle', xRegister[180-1], xRegister[180-1]*180)
    # print('220th cycle', xRegister[220-1], xRegister[220-1]*220)

    

  return 0


def part2(data):
  cpuInstructions = {}
  currentCycle = 0
  totalCycles = 1
  xRegister = [*()]
  inputData = c.removeCommentLines(data,'#')
  
  # create the dictionary
  for index, instruction in enumerate(inputData, start=1):
    parameters = instruction.split(' ')
    if len(parameters) == 1: parameters.append(0)
    cpuInstructions[index] = {}
    cpuInstructions[index]["instruction"] = parameters[0]
    cpuInstructions[index]["instructionParm"] = int(parameters[1])

    if parameters[0] == 'noop':
      totalCycles += 1
    elif parameters[0] == 'addx':
      totalCycles += 2

  # build empty register of total cycles
  for xLoop in range(totalCycles):
    xRegister.append(0)

  # initial register value is 1
  xRegister[0] = 1
  
  # run the calculations
  for instruction in cpuInstructions:
    print(cpuInstructions[instruction]["instruction"])
    if cpuInstructions[instruction]["instruction"] == 'noop':
      currentCycle += 1
      xRegister[currentCycle] += xRegister[currentCycle-1]
    elif cpuInstructions[instruction]["instruction"] == 'addx':
      currentCycle += 1
      xRegister[currentCycle] += xRegister[currentCycle-1]
      currentCycle += 1
      xRegister[currentCycle] += xRegister[currentCycle-1]
      xRegister[currentCycle] += cpuInstructions[instruction]["instructionParm"]
      
    # pprint(cpuInstructions[instruction]["instruction"])
  
  # pprint(inputData)
  # pprint(cpuInstructions)
  # pprint(xRegister)
  print('totalCycles', totalCycles)

  spriteStart = 0
  spriteEnd = 2
  crtDisplay = ''

  for yLoop in range(0,221,40):
    for xLoop in range(40):
      spriteStart = xRegister[xLoop+yLoop] - 1
      spriteEnd = xRegister[xLoop+yLoop] + 1
      # print('loop start',xLoop,spriteStart,spriteEnd)
      if xLoop >= (spriteStart) and xLoop <= (spriteEnd):
        crtDisplay = crtDisplay + '#'
      else:
        crtDisplay = crtDisplay + '.'
    crtDisplay = crtDisplay + '\n'

    # print('cycle', xLoop+1, 'register', xRegister[xLoop],\
          # 'crtDisplay', crtDisplay, '\n  sprite', spriteStart, spriteEnd) 

  print(crtDisplay)

  return 0
