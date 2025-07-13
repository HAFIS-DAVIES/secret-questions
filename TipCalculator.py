print("Welcome to Red Lobster Tip Calculator!")
bill = float(input("What is the bill ? : \n $ " ))
tip = int(input("How much Tip would you like to give? (5%, 10%, 15% or 20%) \n"))
people = int(input("how many friends are sharing the bill? : \n"))

bill_with_tip = tip / 100 * bill + bill

bill_per_person = round((bill_with_tip/people), 2)

print(f"your total bill is ${bill_with_tip}")
print(f"each person is to pay : $ {bill_per_person} ")

