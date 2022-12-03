# Day 2 - https://adventofcode.com/2022/day/2
def part1(data):
  strategyGuide = {
    #A and X are Rock, score 1
    #B and Y are Paper, score 2
    #C and Z are Scissors, score 3
    #Lose, score 0
    #Draw, score 3
    #Win, score 6
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
  }
  totalScore = 0
  gamePlay = data.split('\n')

  for aGame in gamePlay:
    # print(strategyGuide.get(aGame))
    totalScore += strategyGuide.get(aGame, 0)
    # print(totalScore)

  print("Total points for this Rock/Paper/Scissors strategy is " +
        str(totalScore))
  return totalScore


def part2(data):
  strategyGuide = {
    #A is Rock, score 1
    #B is Paper, score 2
    #C is Scissors, score 3
    #X is Lose, score 0
    #Y is Draw, score 3
    #Z is Win, score 6
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
  }
  totalScore = 0
  gamePlay = data.split('\n')

  for aGame in gamePlay:
    # print(strategyGuide.get(aGame))
    totalScore += strategyGuide.get(aGame, 0)
    # print(totalScore)

  print("Total points for this Rock/Paper/Scissors strategy is " +
        str(totalScore))
  return totalScore
