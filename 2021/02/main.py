position = [0,0]

with open("./data.txt", "r") as f:
  data = f.readlines()

for i in data:
  command, num = i.split() 
  if command == "forward":
    position[0] += int(num)
  elif command == "up":
    position[1] -= int(num)
  else:
    position[1] += int(num)

xpos, ypos = position

print(xpos * ypos)
