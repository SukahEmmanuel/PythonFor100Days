import random
customers = []
names = input("Enter the names:\n").split(", ")
customers.extend(names)
person_paying = random.choice(customers)
print(f"{person_paying} is going to buy the meal today!")