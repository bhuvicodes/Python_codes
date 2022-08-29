total_water = int(input("Enter the total amount of water in the bottle in %: "))



while total_water < 100:

    add_water = int(input("Enter the amount of water you want to add: "))

    if total_water + add_water == 100:
        total_water += add_water
        print(f"The water bottle is full!!! ***  {total_water}%  ***")
        break

    elif total_water + add_water <= 100:
        total_water += add_water
        print(f"The water is still low :( ***  {total_water}%  ***")

    else:
        print(f"The water is TOO HIGH! :( ***  {total_water}%  ***")
        


else:
    print("Your bottle is already full!!!")