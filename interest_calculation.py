print ("Welcome to Investment Calculator!")

while True:
    amount_invested = int(input("Enter the value you wish to invest: "))
    while amount_invested < 0 or amount_invested > 50000 :
        print("Invalid input, please try again!")
        amount_invested = int(input("Enter the value you wish to invest: "))

    interest_rate = int(input("Enter the interest rate: "))
    while interest_rate < 0 or interest_rate > 15 :
          print("invalid input, please try again!")
          interest_rate = int(input("Enter the interest rate: "))

    investment_duration = int(input("Enter the number of years in which you wish to invest: "))
    while investment_duration < 0 :
          print("Invalid input, please try again!")
          investment_duration = int(input("Enter the number of years in which you wish to invest: "))
    
    months = investment_duration * 12
    monthly_interest_rate = interest_rate / 12 / 100
    monthly_investment = amount_invested/12
    total_value = 0

    for month in range(1, months+1):
         total_value += amount_invested
         total_value += total_value * monthly_interest_rate

         if month % 12 == 0:
              print(f"Year {month // 12}: ${round(total_value, 2)}")
    print(f"Total:\t{round(total_value, 2)}")

            
    if (choice := input("Would you like to invest (y/n)?: ")) == 'n':
        break  
print ("Completed by Daniel Arterbury")
