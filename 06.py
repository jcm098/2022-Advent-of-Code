# Day 1 - https://adventofcode.com/2022/day/6

#https://note.nkmk.me/en/python-str-extract/#:~:text=Extract%20a%20substring%20from%20a%20string%20in%20Python,pattern%20with%20parentheses%20Match%20any%20single%20character%20
#https://www.tutorialspoint.com/python-program-to-find-all-duplicate-characters-in-a-string

import common as c


def part1(data):
  markerData = c.removeCommentLines(data,'#')

  numberOfChars = len(markerData[0])
  charsToProcess = 0
  print(numberOfChars)
  print(markerData[0][0:4])
  print(markerData[0])

  for xLoop in range(numberOfChars):

    # print(xLoop)
    # print(markerData[0][xLoop:xLoop+4])
    
    duplicateChars = c.findDuplicateCharacters(markerData[0][xLoop:xLoop+4])
    if len(duplicateChars) == 0:
      print(xLoop)
      print(duplicateChars)
      print(markerData[0][xLoop:xLoop+4])
      charsToProcess = xLoop + 4
      break
    # print(duplicateChars)
    # print(len(duplicateChars))
    
  # for i in range(len(markerData)):
  #     print(len(markerData))
  #     print(i)
  #     print(markerData[i-1])
  
  return charsToProcess


def part2(data):
  markerData = c.removeCommentLines(data,'#')

  numberOfChars = len(markerData[0])
  charsToProcess = 0
  print(numberOfChars)
  print(markerData[0][0:14])
  print(markerData[0])

  for xLoop in range(numberOfChars):

    # print(xLoop)
    # print(markerData[0][xLoop:xLoop+4])
    
    duplicateChars = c.findDuplicateCharacters(markerData[0][xLoop:xLoop+14])
    if len(duplicateChars) == 0:
      print(xLoop)
      print(duplicateChars)
      print(markerData[0][xLoop:xLoop+14])
      charsToProcess = xLoop + 14
      break
    # print(duplicateChars)
    # print(len(duplicateChars))
    
  # for i in range(len(markerData)):
  #     print(len(markerData))
  #     print(i)
  #     print(markerData[i-1])
  
  return charsToProcess
