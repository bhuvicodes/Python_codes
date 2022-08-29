#Unit Consumption of lesser than 200 units:	
bill_101_200_1 = 1.5


#Unit Consumption less than 500 Units:
bill_101_200_2 = 2
bill_201_500_2 = 3
#total amount for 200 units
pay_upto_200_2 = 100 * bill_101_200_2
#total amount for 500 units
pay_upto_500_2 = 300 * bill_201_500_2


#Unit Consumption above 500 Units:
bill_101_200_3 = 3.5
bill_201_500_3 = 4.6
bill_501 = 6.6

#total amount for 200 units
pay_upto_200_3 = 100 * bill_101_200_3
#total amount for 500 units
pay_upto_500_3 = 300 * bill_201_500_3


#getting total units as input
units = int(input("Enter the total units consumed = "))

pay_units_200 = units - 100
pay_units_501 = units - 500

total_amount = 0

while units > 100:

    if pay_units_200 > 100 and pay_units_200 <= 400:
        total_amount = pay_upto_200_2 + (pay_units_200 - 100) * bill_201_500_2
        print(f"Total Current Bill of {units} units = Rs. {total_amount}\nNOTE: *Without extra charges*")  
        
    elif pay_units_501 > 0:
        total_amount = pay_upto_200_3 + pay_upto_500_3 + pay_units_501 * bill_501
        print(f"Total Current Bill of {units} units = Rs. {total_amount}\nNOTE: *Without extra charges*")
    else:
        total_amount = pay_units_200 * bill_101_200_1
        print(f"Total Current Bill of {units} units = Rs. {total_amount}\nNOTE: *Without extra charges*")
        
    break

else:
    print(f"Your current bill of {units} unit(s) is free...!")