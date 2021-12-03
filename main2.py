with open("./data.txt", "r") as f:
  data = f.readlines()
  data = list(map(int, data))

increased = 0

for i in range(len(data)-3):
  a = data[i]
  b = data[i+3]
  
  if b / a  > 1:
    increased += 1

print(increased)
