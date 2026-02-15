a=5
print("type of a:",type(a))
b=2.5
print("type of b:",type(b))
c="coding"
print("type of c:",type(c))
d=True
print("type of d:",type(d))

name="Penguin"
age=15
is_student=True
weight=38.5
print("Name :",name)
print("Data Type of Name",type(name))
print("Age :",age)
print("Data Type of Age",type(age))
print("is_student :",is_student)
print("Data Type of is_student",type(is_student))
print("Weight :",weight)
print("Data Type of Weight",type(weight))
print("/n After Type Casting")
age=str(age)
print(age)
print("Data Type of age is",type(age))
weight+int(weight)
print(weight)kush
print("Data Type of Weight is",type(weight))

text=str(input("Enter a string:"))

revText=text[::-1]
print("Reverse of the given string is:")
print(revText)