with open("./data.txt", "r") as f:
  data = f.readlines()

increased = 0

for i, num in enumerate(data):
  num = int(num)
  if num > int(data[i-1]):
    increased += 1

print(increased)