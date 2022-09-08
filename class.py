
#income= float(input("Enter your income:"))
#if income > 450000:
   # print("damn u rich")
#else:
#    print("you got it!")    
""""
cp = float(input("enter the right number:"))
answer=2
if cp== answer:
    print("yay")
while cp>answer or cp<answer:
    print(answer)
    answer=answer +1
else:
    print("you have reached your limt")    """

chance=0
win=0
num=4

while chance <=3 and win !=1:
    user= int(input("guss the number:"))
    if user==num:
         print("yay")
         win=1
    else:
        chance+=1