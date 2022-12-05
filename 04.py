# Day 1 - https://adventofcode.com/2022/day/4

# https://pynative.com/python-range-function/#h-range-start-stop
# https://appdividend.com/2022/11/30/convert-list-of-ints-to-string-in-python/

import common as c


def part1(data):
  cleaningPairs = data.split('\n')
  duplicateCleaning = 0

  for pairs in cleaningPairs:
    areas = pairs.split(',')
    area1 = areas[0].split('-')
    area2 = areas[1].split('-')
    areaSet1 = set(range(int(area1[0]), int(area1[1]) + 1))
    areaSet2 = set(range(int(area2[0]), int(area2[1]) + 1))
    # listOfStrings = map(str, listOfInts)
    print(areas)
    # print(area1[0])
    # print(areaSet1)
    # print(area2)
    # print(range(int(areas[0].split('-'))))
    isDuplicate = areaSet1.issubset(areaSet2) or areaSet2.issubset(areaSet1)

    if isDuplicate:
      duplicateCleaning += 1

  print(duplicateCleaning)
  return duplicateCleaning


def part2(data):
  cleaningPairs = data.split('\n')
  overlapCleaning = 0

  for pairs in cleaningPairs:
    areas = pairs.split(',')
    area1 = areas[0].split('-')
    area2 = areas[1].split('-')
    areaSet1 = set(range(int(area1[0]), int(area1[1]) + 1))
    areaSet2 = set(range(int(area2[0]), int(area2[1]) + 1))
    print(areas)
    # isDuplicate = areaSet1.issubset(areaSet2) or areaSet2.issubset(areaSet1)

    if not (areaSet1.isdisjoint(areaSet2)):
      print('overlap')
      overlapCleaning += 1

  print(overlapCleaning)

  # print(c.splitString2("sdsdewwe"))
  return overlapCleaning
