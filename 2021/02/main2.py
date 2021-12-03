position = [0,0]
aim = 0

with open("./data.txt", "r") as f:
  data = f.readlines()

for command, num in map(str.split, data):
  if command == "forward":
    position[0] += int(num)
    position[1] += aim * int(num)
  elif command == "up":
    aim -= int(num)
  else:
    aim += int(num)

xpos, ypos = position

print(xpos * ypos)