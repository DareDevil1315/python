a=10
b=12 
c=0

if a and b and c:
        print("all the numbers have boolean nalue as true")
else:
        print("at least one number has boolean value as false")


a=10
b=-10
c=0

if a>0 or b>0:
        print("either of the numbers is graeter than 0")
else:
        print("no number is greater than 0")

if b>0 or c>0:
        print("either of the numbers are greater than 0")
else:
        print("no number is greater than 0")


a=10
b=12
c=12

print(a!=b)
print(b!=c)

a="python"
b="coding"

if a!=b:
        print(a, 'and',b ,'are diffrent')

a=4
b=5

if (a==1)!=(b==5):
        print('hello')


a=int(input("enetr a number"))

if a%2 !=0:
        print(a,"is not a even number")

height=float(input("eneter your height in  cm "))
weight=float(input("eneter your weight in  kg "))

BMI=weight/(height/100)**2

print("ur BMI is",BMI)

if BMI<=18.4:
        print("you are under weight")
elif BMI <=24.9:
        print("you are healthy")
elif BMI<=29.9:
        print("you are over weight")
elif BMI<=34.9:
        print("you are severly over weight")
else:
        print("you are severly obese")
