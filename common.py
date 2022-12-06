# Set of common functions

# https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files


def splitString(string):
  first_half = string[0:len(string) // 2]
  second_half = string[len(string) // 2:]

  return [first_half, second_half]


def commonCharacters(s1, s2, s3):
  return " ".join(sorted(set(s1) & set(s2) & set(s3)))

def removeCommentLines(data, comment_flag):
  outputData = []
  inputData = data.split('\n')

  for index, line in enumerate(inputData):

    if line.count(comment_flag) == 0:
      outputData.append(line)
  
  return outputData

def popFromSet(set):

  lastItem = set[len(set)-1]
  set.pop()
  
  return lastItem

def findDuplicateCharacters(str):
  duplicate_char = []
  
  for character in str:
     # check whether there are duplicate characters or not
     # returning the frequency of a character in the string
        if str.count(character) > 1:
     # append to the list if it is already not present
           if character not in duplicate_char:
              duplicate_char.append(character)
  # print(*duplicate_char)
  
  return duplicate_char