#  Day 3 - https://adventofcode.com/2022/day/3


def common_characters(s1, s2, s3):
  return " ".join(sorted(set(s1) & set(s2) & set(s3)))


def splitString(string):
  first_half = string[0:len(string) // 2]
  second_half = string[len(string) // 2:]

  return [first_half, second_half]


def part1(data):
  ruckSackItemTypes = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  # print(ruckSackItemTypes.index('A')+1)
  ruckSacks = data.split('\n')
  priorities = 0

  for contents in ruckSacks:
    # print(len(contents))
    compartments = splitString(contents)
    print(contents)
    print(compartments[0] + ' - ' + compartments[1])
    commonItems = set.intersection(set(compartments[0]), set(compartments[1]))
    # print(''.join(commonStrings))
    print(commonItems)
    for item in commonItems:
      priorities += ruckSackItemTypes.index(item) + 1
      print(ruckSackItemTypes.index(item) + 1)
    # print(compartments[1])

  return priorities


def part2(data):
  ruckSackItemTypes = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  # print(ruckSackItemTypes.index('A')+1)
  ruckSacks = data.split('\n')
  priorities = 0
  teamSize = 3

  for xLoop in range(int(len(ruckSacks) / teamSize)):
    print(xLoop)
    print(ruckSacks[xLoop * 3])
    print(ruckSacks[(xLoop * 3) + 1])
    print(ruckSacks[(xLoop * 3) + 2])
    commonItemsPart1 = set.intersection(set(ruckSacks[xLoop * 3]),
                                        set(ruckSacks[(xLoop * 3) + 1]))
    commonItemsPart2 = ''.join(commonItemsPart1)
    commonItemsPart3 = set.intersection(set(commonItemsPart2),
                                        set(ruckSacks[(xLoop * 3) + 2]))
    print(
      common_characters(ruckSacks[xLoop * 3], ruckSacks[(xLoop * 3) + 1],
                        ruckSacks[(xLoop * 3) + 2]))
    print(commonItemsPart3)

    for item in commonItemsPart3:
      priorities += ruckSackItemTypes.index(item) + 1
      print(ruckSackItemTypes.index(item) + 1)

  print(len(ruckSacks))
  print(ruckSacks[0])
  return priorities
