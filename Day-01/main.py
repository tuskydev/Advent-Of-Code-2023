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
#   print(line)

#   total += int(twoDigits)

## --- Part Two ---
handle = open("./Day-01./list.txt", "r")
stringToNums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                "six": 6, "seven": 7, "eight": 8, "nine": 9}
letterToIndex = []

for index, line in enumerate(handle):
  letterToIndex.append({})
  currDict = letterToIndex[index]

  for num in stringToNums:
    try:
      numIndex = line.index(num)
      currDict[num] = numIndex
    except: continue

  for i, char in enumerate(line):
    if char.isdigit():
      currDict[char] = i
      break
  for char in line[::-1]:
    if char.isdigit():
      ind = line.index(char)
      currDict[char] = ind
      break

total = 0

for currDict in letterToIndex:
  """
  minVal/maxVal (list) = two values, left: num - right: index
  """
  finalString = ""
  minVal = []
  maxVal = []

  for key, value in currDict.items():
    if not minVal:
      minVal.append(key)
      minVal.append(value)
    if not maxVal:
      maxVal.append(key)
      maxVal.append(value)
    if value <= minVal[1]:
      minVal[0] = key
      minVal[1] = value
    if value >= maxVal[1]:
      maxVal[0] = key
      maxVal[1] = value

  # Convert any letter numbers to numbers
  if minVal[0] in stringToNums:
    minVal[0] = stringToNums[minVal[0]]
  if maxVal[0] in stringToNums:
    maxVal[0] = stringToNums[maxVal[0]]

  finalString += str(minVal[0]) + str(maxVal[0])
  print(finalString)
  total += int(finalString)

print(total)