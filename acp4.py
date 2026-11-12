time= int(input("Enter homework time in minutes"))
if time>60:
    print("Start now because this is a long homework session.")
else:
    print("Finish quickly. This is a short homework session.")

free= input("Is there any free time after homework? (yes/no)")
if free=="yes":
    print("Pick a hobby")

print("===========DAILY PLAN==========")
print("The amount of time you will spend on your homework:",time)
print("If you have free time after homework:",free)
