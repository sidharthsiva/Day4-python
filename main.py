import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

length = len(names) - 1

person_topay = random.randint(0,length)

print(f"{names[person_topay]} is going to buy the meal today!")