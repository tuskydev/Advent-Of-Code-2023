# --- Day 3: Gear Ratios: Part One ---

# f = open("./Day-03/list.txt")

# data = []
# symbols = []
# total = 0

# for line in f:
#   data.append(line.rstrip())

# for line in data:
#   for i in line:
#     if not i.isdigit() and i != "." and i not in symbols:
#       symbols.append(i)

# for i, line in enumerate(data):
#   # Checking neighbors and counting streaks, ticking saved flag
#   streak = False
#   saved = False
#   num = ""

#   for ii, char in enumerate(line):
#     # Setting up all lists
#     prevLine = []
#     currLine = []
#     nextLine = []
#     currLine = line
#     if i != 0:
#       prevLine = data[i-1]
#     if i+1 != len(data):
#       nextLine = data[i+1]

#     if char.isdigit():
#       # Left wall
#       if ii == 0:
#         prevLine = prevLine[:2]
#         currLine = currLine[1:2]
#         nextLine = nextLine[:2]
#       # Right wall
#       elif ii+1 == len(line):
#         prevLine = prevLine[ii-1:len(line)]
#         currLine = currLine[ii-1:ii]
#         nextLine = nextLine[ii-1:len(line)]
#       # In the middle
#       else:
#         prevLine = prevLine[ii-1:ii+2]
#         currLine = currLine[ii-1:ii+2]
#         nextLine = nextLine[ii-1:ii+2]

#       # Check if the number is next to a symbol
#       for element in prevLine:
#         if element in symbols:
#           saved = True
#       for element in currLine:
#         if element in symbols:
#           saved = True
#       for element in nextLine:
#         if element in symbols:
#           saved = True

#       streak = True
#       num += str(char)
#       if ii +1 == len(line) and streak and num and saved:
#         total += int(num)
#         num = ""
#         streak = False
#         saved = False
#     else:
#       if streak and num and saved:
#         total += int(num)
#         num = ""
#         streak = False
#         saved = False
#       else:
#         streak = False
#         saved = False
#         num = ""

# print("this is total",total)

# --- Day 3: Gear Ratios: Part Two ---

f = open("./Day-03/list.txt")

data = []
symbols = ["*"]
total = 0
starDict = {}

for line in f:
  data.append(line.rstrip())

for i, line in enumerate(data):
  for ii, char in enumerate(line):
    if char == "*":
      starDict[f"{i}{ii}"] = []
# starDict["13"].append(354)
print(starDict)

for i, line in enumerate(data):
  # Checking neighbors and counting streaks, ticking saved flag
  streak = False
  saved = False
  num = ""
  location = ""

  for ii, char in enumerate(line):
    # Setting up all lists
    prevLine = []
    currLine = []
    nextLine = []
    currLine = line
    if i != 0:
      prevLine = data[i-1]
    if i+1 != len(data):
      nextLine = data[i+1]

    if char.isdigit():
      # Left wall
      if ii == 0:
        prevLine = prevLine[:2]
        currLine = currLine[1:2]
        nextLine = nextLine[:2]
      # Right wall
      elif ii+1 == len(line):
        prevLine = prevLine[ii-1:len(line)]
        currLine = currLine[ii-1:ii]
        nextLine = nextLine[ii-1:len(line)]
      # In the middle
      else:
        prevLine = prevLine[ii-1:ii+2]
        currLine = currLine[ii-1:ii+2]
        nextLine = nextLine[ii-1:ii+2]

      # Check if the number is next to a symbol
      for element in prevLine:
        if element in symbols:
          if not saved:
            location += str(i-1) + str(data[i-1].find("*"))
          saved = True
      for element in currLine:
        if element in symbols:
          if not saved:
            location += str(i) + str(data[i].find("*"))
          saved = True
      for element in nextLine:
        if element in symbols:
          if not saved:
            location += str(i+1) + str(data[i+1].find("*"))
          saved = True

      streak = True
      num += str(char)
      if ii +1 == len(line) and streak and num and saved:
        starDict[f"{location}"].append(int(num))
        num = ""
        streak = False
        saved = False
        location = ""
    else:
      if streak and num and saved:
        starDict[f"{location}"].append(int(num))
        num = ""
        streak = False
        saved = False
        location = ""
      else:
        streak = False
        saved = False
        num = ""
        location = ""

for key, value in starDict.items():
  tempTotal = 1
  if len(value) > 1:
    for v in value:
      tempTotal *= v
  total += tempTotal
print(starDict)
print(total)
