# Lucy Langenberg
# comparing Brutus's and Portia's accounts - when does the amount of money in Brutus's exceed Portia's?

BRUTUS_INTEREST_RATE = 0.05
PORTIA_INTEREST_RATE = 0.04

BRUTUS_INITIAL_DEPOSIT = 1
PORTIA_INITIAL_DEPOSIT = 100000

years = 1
brutus_wealth = BRUTUS_INITIAL_DEPOSIT
portia_wealth = PORTIA_INITIAL_DEPOSIT

# while Brutus's wealth is less than Portia's, calculate annual compound interest for both accounts
while brutus_wealth <= portia_wealth:
    brutus_wealth = brutus_wealth * (1 + BRUTUS_INTEREST_RATE)
    portia_wealth = portia_wealth * (1 + PORTIA_INTEREST_RATE)
    years = years + 1

    # every year, check to see if Brutus has more money yet; if yes, print results
    if brutus_wealth > portia_wealth:
        print(str(years) + " years after their initial deposits, Brutus's wealth exceeded Portia's.")
        print("Brutus's wealth: $" + str(brutus_wealth))
        print("Portia's wealth: $" + str(portia_wealth))