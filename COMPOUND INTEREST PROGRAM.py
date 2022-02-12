# WRITE A PROGRAM THAT WILL TAKE IN AN INITIAL AMOUNT, KNOWN AS THE PRINCIPLE
# AND ADD AN INTEREST RATE OVER TIME - THIS IS KNOWN AS THE COMPOUND INTEREST
# THE FORMULA IS A = P(1 + R/100)^t
# WHERE A is the total amount
# P IS THE PRINCIPLE AMOUNT
# R IS THE INTEREST RATE
# T IS THE TIME SPAN
# THE COUMPOUND INTEREST IS GIVEN BY A-P

print("This program will give you your compound interest rate.")
print("Please enter values below:")
principal = float(input("Please enter principle amount: "))
time = float(input("Please enter the amount of time (in years) you would like to save: "))
rate = 8.25
total = principal * (1 + rate/100) ** time
compInterest = total - principal
print("Your gain was " + str(compInterest))


