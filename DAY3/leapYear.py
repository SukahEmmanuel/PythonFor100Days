year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year!")
    elif year % 400 == 0:
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year!")
else:
    print(f"{year} is not a leap year!")

#Another way to solve it is
# if year % 4 ==0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")