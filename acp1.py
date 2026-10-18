import keyword
print("The 35 keywords are :  \n")
print(keyword.kwlist)
print(len(keyword.kwlist))

name=input("Enter your name:")
goal=input("Enter one skill you want to get :")
when=input("Enter the month you want to reach it by:")

dailyminutes=30
print("\nMY PERSONAL GOAL PLAN\n")

print("Name:",name)
print("Goal:",goal)
print("When:",when)
print("Daily Minutes:",dailyminutes)

print("Status:",end=" ")
print("\nNot started\n")

print("Reminder - Practise every day !")
print(name,"wants to learn a new skill, which is",goal,"by",when)