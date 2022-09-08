from turtle import distance
"""""
dog_year= 7
human_age = float(input"how old are you?")
human_in_dog_years=dog_year*human_age# the calculation for human in dogs age
print("An age",human_age,"human shoud be",human_in_dog_years,"in dog years")
"""
"""name=input("whats your name?") #asking for input for name from user
last_name=input("whats your last name?") #aksing for last name to be inputed by user
age=int(input("how old are you?")) #asking an age 
print("hi",name,last_name,",you're",age,"years old")"""

humanage =  float(input("Enter your age: ")) #asking for age forom user
dogage = humanage * 7 # one year in human is 7 times in dog year 1
month= dogage % 1 #calculating the quotient of the year 
month = month * 12#Taking the remainder as a month 
days=month%1#calculating the quatent of the month 
days= days*30#taking the remainder as a days since 30 days is one month
print ("your age in dog year is" ,int(dogage),"year",int(month),"month",int(days),"days")
catage= humanage / 9#human age will be divied by 9 
month= catage % 1 #calculating the quotient of the year 
month = month * 12#Taking the remainder as a month
days=month%1#calculating the quatent of the month
days= days*30 #taking the remainder as a days since 30 days is one month
print ("your age in cat year is" ,int(catage),"year",int(month),"month",int(days),"days")
horseage=3*(((((humanage)**2) - 47)/7)+12)# given formula to calculate a humans age in horseage
month= horseage % 1 #calculating the quotient of the year 
month = month * 12#Taking the remainder as a month
days=month%1 #calculating the quatent of the month
days= days*30 #taking the remainder as a days since 30 days is one month
print ("your age in horse year is" ,int(horseage),"year",int(month),"month",int(days),"days")
