# Get user inputs
initial_deposit = float(input('Enter initial deposit: '))
duration_years = float(input('Enter duration (yrs): '))
compounding_months = float(input('How would you like your deposit compounded (enter number of months):\n'))

# Define the annual interest rate
annual_interest_rate = 0.05  # annual interest rate


# Function to calculate compound interest
def compound_interest(principal, annual_rate, months, years):
    amount = principal * (1 + annual_rate / months) ** (months * years)
    amount = round(amount, 2)
    return amount


# Calculate the total amount and profit
total_amount = compound_interest(initial_deposit, annual_interest_rate, compounding_months, duration_years)
profit = round(total_amount - initial_deposit, 2)

# Print the results
print(f'Total amount after {duration_years} years is Kshs: {total_amount}')
print(f'You have gained Kshs: {profit}')

