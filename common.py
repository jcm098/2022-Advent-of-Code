# Set of common functions

# https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files

def splitString(string):
  first_half = string[0:len(string) // 2]
  second_half = string[len(string) // 2:]

  return [first_half, second_half]

def commonCharacters(s1, s2, s3):
  return " ".join(sorted(set(s1) & set(s2) & set(s3)))

