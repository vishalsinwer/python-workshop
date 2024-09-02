day_of_week = input("enter the day of week: ").lower()
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("i will practice")
else:
    print("i will learn")  

num1 = int(input("enter the first no.: "))
num2 = int(input("enter the second no.: "))

choice = input("enter the opertaion: (options +, - , * , / , %)")

if choice == "+":
    sum_of_no = num1 + num2
    print("addition:" , sum_of_no)
elif choice == "-":
    sum_of_no = num1 - num2
    print("subtraction:" , sum_of_no)
elif choice == "*":
    sum_of_no = num1 * num2
    print("multiplication:",sum_of_no)
elif choice == "/":
    sum_of_no = num1 / num2
    print("division:",sum_of_no)   
else:
    print("invalid")      