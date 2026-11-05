temperature= int(input("Enter the tempature:"))
if temperature>25:
    clothes="Wear T-shirt"
else:
    clothes=("Wear jacket")
raining=input("Is it raining? (yes/no)")
if raining=="yes":
    umbrella=("Take an umbrella with you.")
else:
    umbrella="not required"

wind=int(input("Enter the speed of the wind in km/h:"))
if wind > 30:
    day=("It's a windy day.")
else:
    day=("It's a calm day.")
puddles=input("Are there any puddles? (yes/no)")
if puddles=="yes":
    shoes=("Wear boots.")
else:
    shoes=("Wear normal shoes.")

print("============Summary============")
print("The temperature is",temperature)
print(clothes)
print("Is it raining?",raining)
print(umbrella)
print("What is the wind speed:",wind)
print(day)
print("Puddles:",puddles)
print(shoes)