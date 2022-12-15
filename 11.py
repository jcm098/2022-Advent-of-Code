# Day 1 - https://adventofcode.com/2022/day/1

# https://www.geeksforgeeks.org/python-program-to-compute-arithmetic-operation-from-string/
# https://www.pythonpool.com/python-round-down/
# https://reactgo.com/python-check-if-number-divisible-by-another/#:~:text=To%20check%20if%20a%20number%20is%20divisible%20by,of%20another%20number%20otherwise%20it%20not%20a%20divisible.
# https://stackoverflow.com/questions/10121861/dividing-large-numbers-in-python#:~:text=If%20you%20need%20precision%2C%20avoid%20floating%20point%20arithmetic,divisor%20-%201%20to%20the%20dividend%20before%20dividing.

import common as c
from decimal import Decimal
import gmpy2
from gmpy2 import mpz
import math
import time
from pprint import pprint

def loadMonkeyData(instructions):
  monkeys = {}
  currentMonkey = 0

  # loop through and build the "monkey data"
  for line in instructions:
    line = line.strip()

    if line == '':
      continue
    
    monkeyData = line.split(':')
    monkeyData[0] = monkeyData[0].replace(':', '').strip()
    monkeyData[1] = monkeyData[1].strip()

    # pprint(monkeyData)

    if monkeyData[0].startswith('Monkey'):
      currentMonkey = int(line.split(' ')[1].replace(':', ''))
      monkeys[currentMonkey] = {}
      monkeys[currentMonkey]["inspection count"] = 0
    elif monkeyData[0].startswith('Starting items'):
      monkeys[currentMonkey]['items'] = \
        monkeyData[1].split(',')
      monkeys[currentMonkey]['items'] = \
        list(map(int, monkeys[currentMonkey]['items']))
    elif monkeyData[0].startswith('Operation'):
      monkeys[currentMonkey]['operation'] = \
        monkeyData[1].split('new = ')[1]
      monkeys[currentMonkey]['operation'] = \
        monkeys[currentMonkey]['operation'].split(' ')
    elif monkeyData[0].startswith('Test'):
      monkeys[currentMonkey]['test'] = \
        int(monkeyData[1].split('divisible by ')[1])
    elif monkeyData[0].startswith('If true'):
      monkeys[currentMonkey]['if true'] = \
        int(monkeyData[1].split('throw to monkey ')[1])
    elif monkeyData[0].startswith('If false'):
      monkeys[currentMonkey]['if false'] = \
        int(monkeyData[1].split('throw to monkey ')[1])

  return monkeys

def monkeyThrowMonkeyDo(monkeys, worryReducer):
  currentItem = 0
  currentOperation = ''

  for throw in monkeys:
    for item in monkeys[throw]['items']:
      currentItem = int(item)
      monkeys[throw]['inspection count'] += 1

      # run the operation
      currentOp = monkeys[throw]['operation'][1]
      currentOpVal1 = monkeys[throw]['operation'][0]
      currentOpVal2 = monkeys[throw]['operation'][2]

      if currentOpVal1 == 'old': 
        currentOpVal1 = int(currentItem)
      else:
        currentOpVal1 = int(currentOpVal1)
      
      if currentOpVal2 == 'old': 
        currentOpVal2 = int(currentItem)
      else:
        currentOpVal2 = int(currentOpVal2)
        
      if currentOp == '*':
        currentItem = int(currentOpVal1 * currentOpVal2)
      elif currentOp == '+':
        currentItem = int(currentOpVal1 + currentOpVal2)

      # decrease worry level since thrown
      currentItem = math.floor(currentItem / worryReducer)
      # currentItem = currentItem / worryReducer
      # currentItem = int(currentItem)

        # currentItem = currentItem / worryReducer
        # currentItem = currentItem // 1

      # if throw == 2:
        # pprint(monkeys[throw])
      # determine which monkey to throw to
        # print(currentItem % monkeys[throw]['test'])
      if currentItem % monkeys[throw]['test'] == 0:
        targetMonkey = monkeys[throw]['if true']
        monkeys[targetMonkey]['items'].append(currentItem)
      else:
        targetMonkey = monkeys[throw]['if false']
        monkeys[targetMonkey]['items'].append(currentItem)
        
      # print(item, currentItem)
    
    monkeys[throw]['items'] = []
  
  return monkeys

def loadMonkeyDataBig(instructions):
  monkeys = {}
  currentMonkey = 0

  # loop through and build the "monkey data"
  for line in instructions:
    line = line.strip()

    if line == '':
      continue
    
    monkeyData = line.split(':')
    monkeyData[0] = monkeyData[0].replace(':', '').strip()
    monkeyData[1] = monkeyData[1].strip()

    # pprint(monkeyData)

    if monkeyData[0].startswith('Monkey'):
      currentMonkey = int(line.split(' ')[1].replace(':', ''))
      monkeys[currentMonkey] = {}
      monkeys[currentMonkey]["inspection count"] = 0
    elif monkeyData[0].startswith('Starting items'):
      monkeys[currentMonkey]['items'] = \
        monkeyData[1].split(',')
      monkeys[currentMonkey]['items'] = \
        list(map(int, monkeys[currentMonkey]['items']))
    elif monkeyData[0].startswith('Operation'):
      monkeys[currentMonkey]['operation'] = \
        monkeyData[1].split('new = ')[1]
      monkeys[currentMonkey]['operation'] = \
        monkeys[currentMonkey]['operation'].split(' ')
    elif monkeyData[0].startswith('Test'):
      monkeys[currentMonkey]['test'] = \
        int(monkeyData[1].split('divisible by ')[1])
    elif monkeyData[0].startswith('If true'):
      monkeys[currentMonkey]['if true'] = \
        int(monkeyData[1].split('throw to monkey ')[1])
    elif monkeyData[0].startswith('If false'):
      monkeys[currentMonkey]['if false'] = \
        int(monkeyData[1].split('throw to monkey ')[1])

  return monkeys


def bigMultiply(n, m):
    ans = 0
    count = 0
    while (m):
        # check for set bit and left
        # shift n, count times
        if (m % 2 == 1):
            ans += n << count
 
        # increment of place value (count)
        count += 1
        m = (m - 1) // (2 + 1)
      # (currentItem - 1) // worryReducer + 1
 
    return ans

def monkeyThrowMonkeyDoBig(monkeys, worryReducer):
  currentItem = 0
  currentOperation = ''

  for throw in monkeys:
    for item in monkeys[throw]['items']:
      currentItem = int(item)
      monkeys[throw]['inspection count'] += 1

      # run the operation
      # print('get')
      currentOp = monkeys[throw]['operation'][1]
      currentOpVal1 = monkeys[throw]['operation'][0]
      currentOpVal2 = monkeys[throw]['operation'][2]

      # print('assign')
      if currentOpVal1 == 'old': 
        currentOpVal1 = int(currentItem)
      else:
        currentOpVal1 = int(currentOpVal1)
      
      if currentOpVal2 == 'old': 
        currentOpVal2 = int(currentItem)
      else:
        currentOpVal2 = int(currentOpVal2)

      # print('eval')
      if currentOp == '*':
        # print('eval mult')
        valCalc = 0
        # g1 = mpz(currentOpVal1)
        # g2 = mpz(currentOpVal2)
        # if g1 == g2:
        #   if gmpy2.is_even(g1):
        #     valCalc = g1 / 2
        #     valCalc = gmpy2.square(valCalc)
        #     valCalc = valCalc * 2
        #   else:
        #     valCalc = gmpy2.square(g2)
        # else:
        #   valCalc = g1 * g2
        valCalc = gmpy2.mul(currentOpVal1, currentOpVal2)
        # if g1 == g2:
        #   valCalc = g1**2
        # else:
        #   for x in range(1,g2+1):
        #     # print('x',x)
        #     valCalc += g1
        # valCalc = currentOpVal1 * currentOpVal2
        # valCalc = karatsuba(currentOpVal1, currentOpVal2)
        # valCalc = bigMultiply(currentOpVal1,currentOpVal2)
        # f1 = Decimal(currentOpVal1)
        # f2 = Decimal(currentOpVal2)
        # valCalc = f1 * f2
        # valCalc = math.prod([currentOpVal1, currentOpVal2])
        # print('eval mult assign')
        currentItem = valCalc
        # currentItem = int(currentOpVal1) * int(currentOpVal2)
        # currentItem = math.prod(my_list1)
      elif currentOp == '+':
        # print('eval add')
        currentItem = currentOpVal1 + currentOpVal2

      # decrease worry level since thrown
      # currentItem = math.floor(currentItem / worryReducer)
      # startTime = time.time()
      # print('div')
      currentItem = (currentItem - 1) // worryReducer + 1
      # endTime = time.time()
      # print('div time', int((endTime-startTime) * 10**3), "ms")
      # currentItem = currentItem / worryReducer
      # currentItem = int(currentItem)

        # currentItem = currentItem / worryReducer
        # currentItem = currentItem // 1

      # if throw == 2:
        # pprint(monkeys[throw])
      # determine which monkey to throw to
        # print(currentItem % monkeys[throw]['test'])
      # startTime = time.time()
      # print('mod')
      if currentItem % monkeys[throw]['test'] == 0:
        targetMonkey = monkeys[throw]['if true']
        monkeys[targetMonkey]['items'].append(currentItem)
      else:
        targetMonkey = monkeys[throw]['if false']
        monkeys[targetMonkey]['items'].append(currentItem)
      currentItem = (currentItem - 1) // worryReducer + 1
      # endTime = time.time()
      # print('mod time', int((endTime-startTime) * 10**3), "ms")
        
      # print(item, currentItem)

    # print('clear')
    monkeys[throw]['items'] = []

  
  return monkeys

def part1(data):
  monkeys = {}
  throwCount = [*()]
  currentMonkey = 0
  throwIterations = 20
  inputData = c.removeCommentLines(data,'#')

  monkeys = loadMonkeyData(inputData)

  #throw the items
  for throws in range(1, throwIterations+1):
    monkeys = monkeyThrowMonkeyDo(monkeys, 3)
    # print(throws)

  #find the top 2 monkeys and calculate the monkey business
  for monkey in monkeys:
    throwCount.append(monkeys[monkey]["inspection count"])

  throwCount.sort(reverse = True)
  
  # pprint(monkeys)
  pprint(throwCount)
  print('monkey business = ', throwCount[0] * throwCount[1])
  
  return 0

def karatsuba(x,y):
  # """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
  if len(str(x)) == 1 or len(str(y)) == 1:
    return x*y
  else:
    n = max(len(str(x)),len(str(y)))
    nby2 = n / 2
    a = x / 10**(nby2)
    b = x % 10**(nby2)
    c = y / 10**(nby2)
    d = y % 10**(nby2)
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
  # this little trick, writing n as 2*nby2 takes care of both even and odd n
  prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
  
  return prod


def part2(data):

  monkeys = {}
  throwCount = [*()]
  currentMonkey = 0
  throwIterations = 10000
  inputData = c.removeCommentLines(data,'#')

  monkeys = loadMonkeyDataBig(inputData)

  #throw the items
  for throws in range(1, throwIterations+1):
    startTime = time.time()
    monkeys = monkeyThrowMonkeyDoBig(monkeys, 1)
    endTime = time.time()
    msTime = int((endTime-startTime) * 10**3)
    
    print('throw', throws, 'ms', msTime)
    # print(throws)

  #find the top 2 monkeys and calculate the monkey business
  for monkey in monkeys:
    throwCount.append(monkeys[monkey]["inspection count"])

  # pprint(monkeys)
  pprint(throwCount)
  throwCount.sort(reverse = True)
  pprint(throwCount)
  
  print('monkey business = ', throwCount[0] * throwCount[1])
  
  return 0
