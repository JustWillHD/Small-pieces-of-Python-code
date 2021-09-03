import random
import time
print("Hi I am the magic 8 ball. Ask me any question and I will answer them precisely")
question = input("Now tell me, what is the question you desire to be answered? ")
print("Shaking")
time.sleep(1.6)
print("Shaking")
time.sleep(1.6)
print("Shaking")
time.sleep(1.6)

a1 = ("Absolutely")
a2 = ("Hmm surely go for it")
a3 = ("Possibly")
a4 = ("Yeah y not")
a5 = ("Don't think that's a good idea")
a6 = ("No way bro")

choice = random.randint(1,6)

if choice == 1:
    print (a1)
elif choice == 2:
    print (a2)
elif choice == 3:
    print (a3)
elif choice == 4:
    print (a4)
elif choice == 5:
    print (a5)
else:
    print (a6)
