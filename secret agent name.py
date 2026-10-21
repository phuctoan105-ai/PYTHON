name=input("Enter your secret name:")
badge=input("Enter your badge:")
is_Active= True
superpowers=5
height=5.7

print("Name is",name,"type is",type(name))
print("Badge is",badge,"type is",type(badge))
print("is_Active is",is_Active,"type is",type(is_Active))
print("superpowers is",superpowers,"type is",type(superpowers))
print("Height is",height,"type is",type(height))
print("\n")

print("Height is now float and we will be converting it into integer")
print("Height is",height,"type is",type(height))
height=int(height)
print("Height is",height,"type is",type(height))
print("\n")

print("Superpowers are integers and we will be converting them into float")
print("superpowers is",superpowers,"type is",type(superpowers))
superpowers=float(superpowers)
print("superpowers is",superpowers,"type is",type(superpowers))
print("\n")

print("First character from the name:",name[0])
print("Last character from the name:",name[-1])
a=name[0:4]
b=badge[4:7]
print("Combining both a and b:",a+b)
print(name.upper())
print(badge.lower())

