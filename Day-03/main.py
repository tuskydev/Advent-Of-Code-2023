# --- Day 3: Gear Ratios: Part One ---

f = open("./Day-03/list.txt")

data = []
symbols = []

for line in f:
  data.append(line.rstrip())

for line in data:
  for i in line:
    if not i.isdigit() and i != "." and i not in symbols:
      symbols.append(i)

for i, line in enumerate(data):
  prevLine = []
  currLine = []
  nextLine = []
  streak = True
  saved = False
  currLine = line
  num = ""

  # Setting up all lists
  if i != 0:
    prevLine = data[i-1]
  if i+1 != len(data):
    nextLine = data[i+1]

  # Checking neighbors and counting streaks, ticking saved flag
  for ii, char in enumerate(line):
    # Left wall
    if ii+1 == 1:
      prevLine = prevLine[:2]
      currLine = currLine[1:2]
      nextLine = nextLine[:2]
    # Right wall
    elif ii+1 == len(line):
      prevLine = prevLine[ii-1:len(line)]
      currLine = currLine[ii-1:len(line)-1]
      nextLine = nextLine[ii-1:len(line)]
    # In the middle
    else:
      prevLine = prevLine[ii-1:ii+2]
      currLine = currLine[ii-1:ii+2]
      nextLine = nextLine[ii-1:ii+2]
    print(prevLine, currLine, nextLine)
    # tempPrevLine = [][line[i][ii-1]:line[i][ii+2]]
    # tempCurrLine = []
    # tempNextLine = []
    # print(tempPrevLine)
    # if char.isdigit():
    #   if streak:
    #     num += char

    #     if currLine[i][ii-1] in symbols or currLine[i][ii+1] in symbols:
    #       print("hi!!")
    #       saved = True


    #     streak = True
    # else: streak = False










# --- Day 3: Gear Ratios: Part Two ---
