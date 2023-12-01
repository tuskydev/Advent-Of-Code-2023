dir = "./Day-01./list.txt"
handle = open(dir, "r")

total = int()

for line in handle:
  twoDigits = ""
  for char in line[:]:
    # print("FIRST LOOP",char)
    if char.isdigit():
      twoDigits += char
      break
  for char in line[::-1]:
    if char.isdigit():
      print("second loop:",char)
      twoDigits += char
      break

  total += int(twoDigits)

print("This is total:", total)