print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

t_count = name1.count("t") + name2.count("t")
r_count = name1.count("r") + name2.count("r")
u_count = name1.count("u") + name2.count("u")
e_count = name1.count("e") + name2.count("e")
l_count = name1.count("l") + name2.count("l")
o_count = name1.count("o") + name2.count("o")
v_count = name1.count("v") + name2.count("v")

true_count = (t_count + r_count + u_count + e_count) * 10
love_count = l_count + o_count + v_count + e_count
compatibility = true_count + love_count
if compatibility < 10 or compatibility > 90:
    print(f"Your score is {compatibility}%, you go together like coke and mentos. ")
elif compatibility > 40 and compatibility < 50:
    print(f"Your score is {compatibility}%, you are alright together.")
else:
    print(f"Your score is {compatibility}%")