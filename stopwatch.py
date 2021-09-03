import time
print("Set a timer!")
length = int(input("How long do you want your timer to last?: "))
length -= 1
while length >= 0:
  time.sleep(1)
  print(length)
  length -= 1
