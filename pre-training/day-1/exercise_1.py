# Variables
name: str = "Rohaan"
age: int = 24
drinks_coffee: bool = True
salary: float = 110000.0

# Formatted sentence
print(f"My name is {name}. I am {age} years old. It is {drinks_coffee} that I drink coffee, and my salary is Rs. {salary}.")

RETIREMENT_AGE: int = 60
CUPS_PER_DAY: int = 3
PRICE_PER_CUP: int = 150
DAYS_IN_WEEK: int = 7

# Calculations
years_to_retirement: int = RETIREMENT_AGE - age
weekly_coffee_budget: int = CUPS_PER_DAY * PRICE_PER_CUP * DAYS_IN_WEEK

# Results
print(f"Years until retirement: {years_to_retirement}")
print(f"Weekly coffee budget: Rs. {weekly_coffee_budget}")
