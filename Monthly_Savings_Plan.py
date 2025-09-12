# prompt for the current age.
current_age = int(input("Please enter your current age: "))

#prompt for the age tp retire.
retire_age = int(input("Please enter the age you want to retire at: "))

#prompt for the desire earnings amount at retirement.
earnings_amount = int(input("Please enter the amount of your desired earnings ar retirement: "))

#prompt for the interest rate.
interest_rate = float(input("Please enter the interest rate: "))

#calculate the numbers of years until retirement.
years_until_retirement = retire_age - current_age
print(f"You have {years_until_retirement} years until retirement.")

#calculate the numbers of months until retirement.
months_until_retirement = years_until_retirement *12
print(f"You have {months_until_retirement} months until retirement.")

# future_amount = present_amount * (1 + interest_rate) ** (time_periods)

# Calculate the monthly interest rate
monthly_interest_rate = interest_rate / 12

# Determine the ideal monthly savings amount based on the desired savings, the number of months left until retirement, and the interest rate.
monthly_savings = (earnings_amount * monthly_interest_rate) / ((1 + monthly_interest_rate) ** months_until_retirement -1)

# display the amount
print(f"You should save ${monthly_savings:.2f} per month to achieve your retirement goal.")
