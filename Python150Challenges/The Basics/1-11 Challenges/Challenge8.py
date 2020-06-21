# 008  Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

total_price = float(input("Enter the Total Bill: "))
dinners = int(input("Enter the no. of dinners: "))

each_bill_pay = str(total_price / dinners)
print("Each person must pay: " + each_bill_pay)

