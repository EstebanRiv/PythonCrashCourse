# Local variables
totalNumber = 0
count = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    elif (number.isnumeric() == False):
     print("Invalid input")
    else:
        totalNumber += int(number)
        count += 1

print("Total = ", totalNumber)
print("Count = ", count)
print("Average = ", totalNumber/count)