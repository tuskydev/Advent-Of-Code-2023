# --- Day 2: Part One: Cube Conundrum ---

# f = open("./Day-02/list.txt", "r")

# def getMax(line):
#   """
#   Finds the most of cubes pulled out in a single game

#   Parameters:
#   -line (str): a sentence that needs to be parsed into respective colors

#   Returns:
#   red (int): the amount of max red cubes pulled out
#   green (int): the amount of max green cubes pulled out
#   blue (int): the amount of max blue cubes pulled out
#   """
#   red, green, blue = 0, 0, 0
#   word = line.split(" ")

#   for i, w in enumerate(word):
#     if w.startswith(("red")):
#       red += int(word[i-1])
#     if w.startswith(("green")):
#       green += int(word[i-1])
#     if w.startswith(("blue")):
#       blue += int(word[i-1])

#   return red, green, blue

# gameScoreTracker = {}

# for line in f:
#   red, green, blue = 0, 0, 0

#   for newLine in line.split(";"):
#     if newLine.startswith("Game"):
#       gameID, uniqueLine = newLine.split(":")[0][5:], newLine.split(":")[1][1:]
#       tempRed, tempGreen, tempBlue = getMax(uniqueLine)
#       if tempRed > red: red = tempRed
#       if tempGreen > green: green = tempGreen
#       if tempBlue > blue: blue = tempBlue
#     else:
#       tempRed, tempGreen, tempBlue = getMax(newLine[1:])
#       if tempRed > red: red = tempRed
#       if tempGreen > green: green = tempGreen
#       if tempBlue > blue: blue = tempBlue

#   gameScoreTracker[gameID] = red, green, blue

# total = 0
# for key, value in gameScoreTracker.items():
#   if value[0] <= 12 and value[1] <= 13 and value[2] <= 14:
#     total += int(key)
#     print(key, value[0], value[1], value[2])
#   else:
#     print(key, value[0], value[1], value[2], "OVER!")
# print(total)

# --- Day 2: Part Two: Cube Conundrum ---

f = open("./Day-02/list.txt", "r")

def getMax(line):
  """
  Finds the most of cubes pulled out in a single game

  Parameters:
  -line (str): a sentence that needs to be parsed into respective colors

  Returns:
  red (int): the amount of max red cubes pulled out
  green (int): the amount of max green cubes pulled out
  blue (int): the amount of max blue cubes pulled out
  """
  red, green, blue = 0, 0, 0
  word = line.split(" ")

  for i, w in enumerate(word):
    if w.startswith(("red")):
      red += int(word[i-1])
    if w.startswith(("green")):
      green += int(word[i-1])
    if w.startswith(("blue")):
      blue += int(word[i-1])

  return red, green, blue

gameScoreTracker = {}

for line in f:
  red, green, blue = 0, 0, 0

  for newLine in line.split(";"):
    if newLine.startswith("Game"):
      gameID, uniqueLine = newLine.split(":")[0][5:], newLine.split(":")[1][1:]
      tempRed, tempGreen, tempBlue = getMax(uniqueLine)
      if tempRed > red: red = tempRed
      if tempGreen > green: green = tempGreen
      if tempBlue > blue: blue = tempBlue
    else:
      tempRed, tempGreen, tempBlue = getMax(newLine[1:])
      if tempRed > red: red = tempRed
      if tempGreen > green: green = tempGreen
      if tempBlue > blue: blue = tempBlue

  gameScoreTracker[gameID] = int(red) * int(green) * int(blue)

total = 0
for key, value in gameScoreTracker.items():
  total += value
print(total)
