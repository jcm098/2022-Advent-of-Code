# Day 1 - https://adventofcode.com/2022/day/1
def part1(data):
  mostCalories = 0
  currentCalories = 0
  inventory = data.split('\n')

  for calories in inventory:
    #print(calories)
    if calories == '':
      #print(currentCalories)
      if currentCalories > mostCalories:
        mostCalories = currentCalories
      currentCalories = 0
    else:
      #print(currentCalories)
      currentCalories += int(calories)

  print("The elf with the most calories has " + str(mostCalories) +
        " calories.")
  return mostCalories


def part2(data):
  currentCalories = 0
  elfCalorieList = []
  inventory = data.split('\n')

  for calories in inventory:
    if calories == '':
      elfCalorieList.append(currentCalories)
      currentCalories = 0
    else:
      currentCalories += int(calories)

  elfCalorieList.sort(reverse=True)

  print("The elf with the most calories has " + str(elfCalorieList[0]) +
        " calories.")
  print("The elf with the second most calories has " + str(elfCalorieList[1]) +
        " calories.")
  print("The elf with the third most calories has " + str(elfCalorieList[2]) +
        " calories.")
  topThreeCalories = elfCalorieList[0] + elfCalorieList[1] + elfCalorieList[2]
  print("The total calories for these three are " + str(topThreeCalories))

  return topThreeCalories
