#Programming concepts
#Assignment 1
#Question 1
# Ali Abouei / aboua0949
#setpember 28

print("Welcome , This is a length unit convertor ")
print()
x = int(input("Enter the number you want to convert, in meters!"))

inches = (x * 100/2.54)
feet = (inches/12)
yards = (feet/3)
miles = (yards/1760)

print(x,"meters is",inches,"inches!")
print(x,"meters is",feet,"feet!")
print(x,"meters is",yards,"yards!")
print(x,"meters is",mile ,"miles!")