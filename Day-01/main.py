## --- Part One ---

# handle = open("./Day-01./list.txt", "r")

# total = int()
# for line in handle:
#   twoDigits = ""
#   for char in line[:]:
#     if char.isdigit():
#       twoDigits += char
#       break
#   for char in line[::-1]:
#     if char.isdigit():
#       twoDigits += char
#       break

#   total += int(twoDigits)
# print(total)

## --- Part Two ---

def splicer(word, list, matches=None, index=0):
  """
  Recursive function looking for matches in word with list

  Parameters:
  - word (str): a random str with numbers in word and integer format
  - list (list): list of strings we want to match to

  Returns:
  list (list): a list of tuple pairs
  """
  # Base cases or when function is done
  if matches is None:
    matches = []
  if len(word) < 3:
    return matches

  for num in list:
    if word.startswith(num):
      matches.append((num, index))

  return splicer(word[1:], list, matches, index=index+1)

f = open("./Day-01./list.txt", "r")
dictOfNumStrings = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5",
                    "six":"6", "seven":"7", "eight":"8", "nine":"9"}
total = 0
data = []

for line in f:
  first, second = 0, 0

  results = splicer(line, dictOfNumStrings)

  for i, char in enumerate(line):
    if char.isdigit():
      results.append((char, i))

  data.append(results)

for list in data:
  min, max = [list[0][0], list[0][1]], [list[0][0], list[0][1]]

  for pair in list:
    if min[1] > pair[1]:
      min = [pair[0], pair[1]]
    if max[1] < pair[1]:
      max = [pair[0], pair[1]]

  convertString = [dictOfNumStrings.get(min[0], str(min[0])),
                   dictOfNumStrings.get(max[0], str(max[0]))]
  total += int(convertString[0] + convertString[1])

print(total)
