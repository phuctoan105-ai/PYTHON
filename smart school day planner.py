print("==========SMART SCHOOL DAY PLANNER==========")
print("Answer 3 questions.")
day=input("What is the day today? (Monday-Sunday)").strip().capitalize()
weather=input("What is the weather today? (sunny/rainy/cloudy)").strip().lower()
homework=input("Is the homework done or not? (yes/no)").strip().lower()
print(f"PLan for {day}:")
if day in ("Saturday","Sunday"):
    print("It's the weekend ! Enjoy it!")
elif day== "Monday":
    print("First day of the week, Good luck")
elif day in ("Tuesday","Wednesday","Thursday"):
    print("Halfway to reach the weekend. Keep going!")
elif day=="Friday":
    print("LAst day of the week ! Congrats !")
else:
    print("Couldn't identify the day... Check the spelling.")
if weather=="sunny" and homework=="yes":
    print("Great job ! Go to the park to relax.")
if weather=="rainy" or weather=="cloudy":
    print("Weather tip: Bring an umbrella with you.")
if not homework=="yes":
    print("Your homework is not done, go finish it !")
if weather=="rainy" and not homework=="yes":
    print("Best plan : Stay at home and finish your homework.")
else:
    print("Stay at home. It might rain.")

print()
print("Your plan is complete ! Have a great day ! And good luck for tomorrow.")