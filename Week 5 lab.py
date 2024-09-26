#1.)
# Miles to KM
def miles_to_KM():
    kilometers = float(input('Enter the Km: '))
    miles = kilometers * .6214
    print(f'{miles:,.2f} miles is equal to {kilometers:,.2f} kilometers')
# Calling the function
miles_to_KM()
#---------------------------------------------------------------

#2.)
#Sales tax program
def taxes():
    #The constants and user input
    state_tax = 0.05
    county_tax = 0.025
    
    purchase = float(input('Enter the purchase amount: '))
    #The calculations
    total_state = purchase *  state_tax
    total_county = purchase * county_tax
    total_purchase = purchase + total_state + total_county
    #The outputs
    print(f'Total state tax: {total_state:,.2f}')
    print(f'Total county tax: {total_county:,.2f}')
    print(f'Subtotal: {total_purchase:,.2f}')
# Calling the function
taxes()
#---------------------------------------------------------------

#3.)
#Insurance costs
def insurance():
    # Constants and user inputs
    suggested_insurance = .8
    building_cost = float(input('Enter the cost of building replacement: $'))
    #Outputs
    insurance_cost = building_cost * suggested_insurance
    print(f'You should spend at least {insurance_cost:,.2f} to insure your property.')
# Calling the function
insurance()
#---------------------------------------------------------------

#4.)
# Auto costs
def monthly_car_bills():
    loan = float(input("Enter monthly loan payment: $"))
    insurance = float(input("Enter monthly insurance cost: $"))
    gas = float(input("Enter monthly gas cost: $"))
    oil = float(input("Enter monthly oil cost: $"))
    tires = float(input("Enter monthly tires cost: $"))
    maintenance = float(input("Enter monthly maintenance cost: $"))
    
    total_monthly = loan + insurance + gas + oil + tires + maintenance
    total_annual = total_monthly * 12
    
    print(f"Total monthly cost: ${total_monthly:.2f}")
    print(f"Total annual cost: ${total_annual:.2f}")

# Calling the function
monthly_car_bills()
#---------------------------------------------------------------

#5.)
# Property Taxes
def property_taxes():
    value_actual = float(input("Enter the value of the property: $"))
    value_assess = value_actual * .6
    tax = (value_assess / 100) * .72
# Printing the outputs
    print(f"Assessment value: ${value_assess:.2f}")
    print(f"Property tax: ${tax:.2f}")

# Calling the function
property_taxes()
#---------------------------------------------------------------

#6.)
# Stadium Seating
def seating_costs():
    #The constants for costs
    ClassA = float(20.00)
    ClassB = float(15.00)
    ClassC = float(10.00)
    #How many were sold
    Bought_A = int(input("Enter the amount of Class A tickets sold: "))
    Bought_B = int(input("Enter the amount of Class B tickets sold: "))
    Bought_C = int(input("Enter the amount of Class C tickets sold: "))
    # Getting totals
    Total_A = Bought_A * ClassA
    Total_B = Bought_B * ClassB
    Total_C = Bought_C * ClassC
    Total_income = Total_A + Total_B + Total_C
    
# Printing the outputs
    print(f"Profit from Class A seating: ${Total_A:.2f}")
    print(f"Profit from Class B seating: ${Total_B:.2f}")
    print(f"Profit from Class C seating: ${Total_C:.2f}")
    print(f"Total sales profit: ${Total_income:.2f}")

# Calling the function
seating_costs()
#---------------------------------------------------------------

#7.)
# Painting company rates
def paints():
    #The constants and inputs
    square_feet_per_gallon = 112
    labor_per_gallon = 8
    hourly_labor_cost = 35.00
    
    wall_feet = float(input('Enter the square feet of wall space to be painted: '))
    paint_cost = float(input('Enter the price of paint per gallon: $'))
    #Calculating totals
    gallons_needed = wall_feet / square_feet_per_gallon
    hours_of_work = gallons_needed * labor_per_gallon
    paint_cost = gallons_needed * paint_cost
    labor_cost = hours_of_work * hourly_labor_cost
    total_job = paint_cost + labor_cost
    
# Printing the outputs
    print(f"Gallons of paint required: {gallons_needed:.2f}")
    print(f"Hours of labor: {hours_of_work:.2f}")
    print(f"Total cost of paint: ${paint_cost:,.2f}")
    print(f"Cost of labor: ${labor_cost:,.2f}")
    print(f'Total costs:$ {total_job:,.2f}')

# Calling the function
paints()
#---------------------------------------------------------------

#8.)
# Monthly sales tax
def monthly_tax():
    #The constants and inputs
    state_tax = 0.05
    county_tax = 0.025
    
    month_profit = float(input('Enter the total sales for this month: $'))
    #Calculating totals
    state_tax_total = month_profit * state_tax
    county_tax_total = month_profit * county_tax
    total_tax = state_tax_total + county_tax_total
    
# Printing the outputs
    print(f"County sales tax: ${county_tax_total:.2f}")
    print(f"State sales tax: ${state_tax_total:.2f}")
    print(f"County sales tax: ${total_tax:.2f}")

# Calling the function
monthly_tax()
#---------------------------------------------------------------

#8.)
# Monthly sales tax
def monthly_tax():
    #The constants and inputs
    state_tax = 0.05
    county_tax = 0.025
    
    month_profit = float(input('Enter the total sales for this month: $'))
    #Calculating totals
    state_tax_total = month_profit * state_tax
    county_tax_total = month_profit * county_tax
    total_tax = state_tax_total + county_tax_total
    
# Printing the outputs
    print(f"County sales tax: ${county_tax_total:.2f}")
    print(f"State sales tax: ${state_tax_total:.2f}")
    print(f"County sales tax: ${total_tax:.2f}")

# Calling the function
monthly_tax()
#---------------------------------------------------------------

#9.)
# Feet to inches
# The main function
def main():
    feet = int(input('Enter a number of feet: '))
    #Conversion
    print(feet, 'is equal to', feet_to_inches(feet), 'inches')
#Feet to inches function
def feet_to_inches(feet):
    # Convert feet to inches
    return feet * 12

main()
#---------------------------------------------------------------

#10.)
# Random number generators
import random
# The main function
def quiz():
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)
    correct_answer = num1 + num2
    your_answer = int(input(f'What is the sum of {num1} and {num2}?: '))
    if your_answer == correct_answer:
        print('That is correct! Congratulations')
    else:
        print(f'Sorry, but the correct answer is {correct_answer}')
# Calling the function
quiz()