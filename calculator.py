#ask user for charge of food
food_charge = float(input('Charge for food: '))

#calculate tip (18% of food)
food_tip = 0.18 * food_charge

#calculate sales tax (7% of food)
sales_tax = 0.07 * food_charge

#display tip amount
print('Tip = $'+ str(round(food_tip,2)))

#display sales tax
print('Sales tax = $'+ str(round(sales_tax,2)))

# display grand total = charge of food + tip + sales_tax
print('Grand total = $'+ str(round(food_charge + food_tip + sales_tax)))