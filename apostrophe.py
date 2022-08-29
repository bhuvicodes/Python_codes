names = ["Bhuvi", "Alice", "Vicky", "Sus", "Simmons"]
ages = [18, 19, 20, 21, 22]

for name in names:
    if name[-1] != "s":
        print(f"{name}'s age is {ages[names.index(name)]}")
    else:
        print(f"{name}' age is {ages[names.index(name)]}")
