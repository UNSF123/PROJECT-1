from numpy import add, subtract, divide

select = int(input("Select operations form 1, 2, 3 :"))

number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))
    
elif select == 3:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))   
else:
        print("Invalid input")

