value_one = input("I can magically determine which one of any three numbers is the largest. Please enter your first number here: ")
value_two = input("And the second:")
value_three = input("And the third: ")

if value_one > value_two and value_one > value_three:
    print(value_one, "is the biggest number!")
elif value_two > value_one and value_two > value_three:
    print(value_two, "is the biggest number!")
elif value_three > value_one and value_three > value_two:
    print(value_three, "is the biggest number!")
else:
    print("What you talkin' 'bout Willis?")