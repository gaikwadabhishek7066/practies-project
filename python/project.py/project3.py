'''
inputs we need from the user
#total rent
# total food ordered for snacking
# Electricity units spend
# charge per unit
# person living in room/flat
# 
# output
# total amount you've to pay is
# '''

rent = int(input("Enter the amount hostel/flat to pay: "))
food = int(input("Enter the amount  food ordered to pay: "))
electricity_spend = int(input("Enter the amount electricity units spend: "))
charge_per_unit = int(input("Enter the charge per units: "))
person = int(input("Enter the wperson living in room/flat: "))

total_bill = electricity_spend * charge_per_unit

output = ( rent + food + total_bill )//person

print("each person will be pay = ", output)