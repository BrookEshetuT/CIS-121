"""
Brook Taffese
sep08,2022

tax Brackets & Fedral income tax rates
"""
import sys


tax = 0.0 #insalizing variable

earnedIncome = float(input("Enter the amount of income you earned in 2021: ")) #asking user to input there information
if earnedIncome < 0:
	print("You made less than 0$. Contact an accountant")

print("Are you married or single?")#asking if the user is married or not for calculating te tax
maritalStatus = input("Type m for married and s for single: ")#giving to option to the user to select



while maritalStatus == "m" and maritalStatus == "s":#giving two condtions so in this case we have s and m 
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")#taking the input agin 
if maritalStatus == "s":#taking the the input s and calculating ther tax
  if earnedIncome <= 9950:#giving the condtion 
     tax= earnedIncome * (0.1)# if it is the above condition is correct do 10%
     print("This year you owe",tax,"in taxes")#print the calculated tax 
  elif earnedIncome <=40525 :# giving other condition 
     tax= ((earnedIncome - 9950) * 0.12) + (0.1 * 9950)#we subtract the diffrnce b/n the two income and claclulating the tax in based on the percent (we do in  a broken down form)
     print("This year you owe",tax,"in taxes")#print the calculated tax 
  elif earnedIncome <= 86375:# giving other condition 
     tax= ((earnedIncome - 40526) * 0.22) + (0.12 * (40525 - 9950)) + (0.1 * 9950)#we subtract the diffrnce b/n the two income and claclulating the tax in based on the percent (we do in  a broken down form)
     print("This year you owe",tax,"in taxes")#print the calculated tax 
  else:# if the user input to morethan the above condtion we are going to tell the user that its too much for the calcultor 
    print("you made too much for this calcultor")  
    


if maritalStatus == "m":
   if earnedIncome <= 19900:#giving the condtion 
    tax= earnedIncome * 0.1# if it is the above condition is correct do 10%
    print("This year you owe",tax,"in taxes")#print the calculated tax 
   elif earnedIncome <=81050:#giving other condition 
    tax= (earnedIncome -19900) * (0.12) + (0.1 * 19990)#we subtract the diffrnce b/n the two income and claclulating the tax in based on the percent (we do in  abroken down form)
    print("This year you owe",tax,"in taxes")#print the calculated tax 
   elif earnedIncome <= 172750:#giving other condition 
    tax= (earnedIncome - 81051) * (0.22)+ (0.12 * (81051 - 19901)) + (0.1 * 19900)#we subtract the diffrnce b/n the two income and claclulating the tax in based on the percent (we do in a broken down form)
    print("This year you owe",tax,"in taxes")#print the calculated tax 
   else:
    print("done")

#print("This year you owe",tax,"in taxes")#print the calculated tax 
