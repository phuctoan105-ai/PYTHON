name=input("Enter your name:")
club=input("Enter the name of your club:")

member_number = 8
points=9.5
is_active=True

print("Name is",name,"type is",type(name))
print("Club is",club,"type is",type(club))
print("Member number is",member_number,"type is",type(member_number))
print("Points are",points,"type is",type(points))
print("is_active",is_active,"type is",type(is_active))
print("\n")

a=name[0:3]
b=club[-1]

print("Your badge code is:",a+b)
badge_code=a+b
print("\n")
print("\n")
print("==========FINAL CODE BADGE==========")
print("Your name is",name,"and its type is",type(name))
print("Your current club is",club,"and its type is",type(club))
print("Your member number is",member_number,"and its type is",type(member_number))
print("Points are",points,"and its type is",type(points))
print("Last but not the least, your badge code is therefore:",badge_code,"and its type is",type(badge_code))

