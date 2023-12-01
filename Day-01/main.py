handle = open("./Day-01./list.txt", "r")

total = int()
for line in handle:
  twoDigits = ""
  for char in line[:]:
    if char.isdigit():
      twoDigits += char
      break
  for char in line[::-1]:
    if char.isdigit():
      twoDigits += char
      break

  total += int(twoDigits)

print("This is total:", total)