#Your life in weeks
age = int(input("What is your current age? "))
max_age = int(input("How many years do you think you have to live on earth? "))
days = 365
weeks = 52
months = 12
time_left = max_age - age
print(f"You have {time_left * days} days, {time_left * weeks} weeks, and {time_left * months} months left.")