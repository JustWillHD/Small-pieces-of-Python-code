import math
print("Welcome to JustWillHD's Data Plan")
pictures = int(input("How many pictures do you send each month? "))
texts = int(input("How many texts do you send each month? "))
totalwithoutdata = pictures * 0.35 + texts * 0.1
data = float(input("How much MB's of data do you use each month? "))
data /= 500
data = math.floor(data)
if data == 0:
    total = totalwithoutdata + 2.5
    print("your total is £{}:".format(total))
    
    if total > 10:
        print("your better off with a plan")

elif data/data == 1:
    total = 2.5 * data + totalwithoutdata 
    print("your total is £{}".format(total))
    
    if total > 10:
        print("your better off with a plan")
else:
    total = 2.5 * (data + 1) + totalwithoutdata
    print("your total is £{}".format(total))
    
    if total > 10:
        print("your better off with a plan")
    
