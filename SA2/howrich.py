# Lucy Langenberg
# howrich.py computes the accumulated wealth of an account after a certain number of years

#establishing constants - by convention, in all caps
INTEREST_RATE = 0.05
INITIAL_DEPOSIT = 1

#number of years after which we're checking the account balance
YEARS_FINAL = 2021

#initializing variables
years = 1
wealth = INITIAL_DEPOSIT

#while loop to calculate compound interest
while years <= YEARS_FINAL:
    wealth = wealth * (1 + INTEREST_RATE)
    years = years + 1

print(str(YEARS_FINAL) + " years after the initial deposit, the account contains $" + str(wealth) + ".")