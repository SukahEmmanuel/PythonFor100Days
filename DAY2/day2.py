#Tip Calculator
print("Welcome to the tip calculator.")
total_bill =  float(input("What is the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, 15?"))
number_of_people = int(input("How many people to split the bill? "))
total_bill_due = total_bill + (total_bill * percentage_tip / 100)
individual_bill_due = total_bill_due / number_of_people
#I can also round the number to two decimal places using:
#final_amount_due = "{:2f}".format(individual_bill_due)
print(f"Each person should pay: ${round(individual_bill_due, 2)}")