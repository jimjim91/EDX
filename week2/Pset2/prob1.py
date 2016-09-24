#function to calculate balance after one year if only the minimum
#monthly is paid each month
"""
balance - outstanding balance on credit card
annualInterestRate - annual interest rate as a decimal
monthlyRepaymentRate - minimum monthly payment rate as a decimal

Monthly interest rate= (Annual interest rate) / 12.0

Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)

Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)

Updated balance each month = (Monthly unpaid balance) +
                             (Monthly interest rate x Monthly unpaid balance)

"""
balance = 5000
annualInterestRate = 0.18
monthlyRepaymentRate = 0.02


#For each month
for month in range(1, 13):
    monthlyPayment = monthlyRepaymentRate * balance
    print("monthlyPayment ", monthlyPayment)
    unpaidBalance = balance - monthlyPayment
    print("unpaidBalance ", unpaidBalance)
    interest = annualInterestRate/12 * unpaidBalance
    print("interest", interest)
    updateBalance = unpaidBalance + (interest * unpaidBalance)
    print("updateBalance ", updateBalance)
    balance = balance+interest
    print("balance ", balance)
    print "Month", month, "Remaining balance: ", round(balance, 2)

    #compute the monthly payment, based on previous month's balance
    #

    #Update the outstanding balance by removing the payment,
    #then charging interest on the result

    #Output the month, the minimum monthly payment and the remaining balance

    #keep track of the total amount of paid over all the past months so far
