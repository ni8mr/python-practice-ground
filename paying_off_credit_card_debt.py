# -*- coding: utf-8 -*-

""" Problem set 2: Introduction to Computer Science and Programming(MIT Courseware) """ 

""" Suppose, each month, a credit card statement will come with the option for us to pay a minimum
 amount of our charge, usually 2% of the balance due. However, the credit card company earns 
 money by charging interest on the balance that we don’t pay. So even if we pay credit card 
 payments on time, interest is still accruing on the outstanding balance. We will demonstrate it in following
 programs. 

 Say we’ve made a $5,000 purchase on a credit card with 18% annual interest rate and 2% minimum monthly payment rate. 
 If we want to know the remaining balance after a year, we can use the following equations. 
 Minimum monthly payment = Minimum monthly payment rate x Balance 
 (Minimum monthly payment gets split into interest paid and principal paid) 
 Interest Paid = Annual interest rate / 12 months x Balance 
 Principal paid = Minimum monthly payment – Interest paid 
 Remaining balance = Balance – Principal paid 

 This is a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month. 
 User input: the outstanding balance on the credit card, annual interest rate, minimum monthly payment rate.
 For each month, this will print the minimum monthly payment, remaining balance, principle paid in 
 the format shown in the test cases below. All numbers should be rounded to the nearest penny. Finally, this 
 will print the result, which shall include the total amount paid that year and the remaining balance. 
 Test case 1: 
 Enter the outstanding balance on your credit card: 4800 
 Enter the annual credit card interest rate as a decimal: .2 
 Enter the minimum monthly payment rate as a decimal: .02 
 Month: 1 
 Minimum monthly payment: $96.0 
 Principle paid: $16.0 
 Remaining balance: $4784.0 
 Month: 2 
 Minimum monthly payment: $95.68 
 Principle paid: $15.95 
 Remaining balance: $4768.05 
 Month: 3 
 Minimum monthly payment: $95.36 
 Principle paid: $15.89 
 Remaining balance: $4752.16 
 Month: 4 
 Minimum monthly payment: $95.04 
 Principle paid: $15.84 
 Remaining balance: $4736.32 
 Month: 5 
 Minimum monthly payment: $94.73 
 Principle paid: $15.79 
 Remaining balance: $4720.53 
 Month: 6 
 Minimum monthly payment: $94.41 
 Principle paid: $15.73 
 Remaining balance: $4704.8 
 Month: 7 
 Minimum monthly payment: $94.1 
 Principle paid: $15.69 
 Remaining balance: $4689.11 
 Month: 8 
 Minimum monthly payment: $93.78 
 Principle paid: $15.63 
 Remaining balance: $4673.48 
 Month: 9 
 Minimum monthly payment: $93.47 
 Principle paid: $15.58 
 Remaining balance: $4657.9 
 Month: 10 
 Minimum monthly payment: $93.16 
 Principle paid: $15.53 
 Remaining balance: $4642.37 
 Month: 11 
 Minimum monthly payment: $92.85 
 Principle paid: $15.48 
 Remaining balance: $4626.89 
 Month: 12 
 Minimum monthly payment: $92.54 
 Principle paid: $15.43 
 Remaining balance: $4611.46 
 RESULT 
 Total amount paid: $1131.12 
 Remaining balance: $4611.46 
 Test case 2:
 In recent years, many credit card corporations tightened restrictions by raising their 
 minimum monthly payment rate to 4%. As illustrated in the second test case below, people 
 will be able to pay less interest over the years and get out of debt faster
 Enter the outstanding balance on your credit card: 4800 
 Enter the annual credit card interest rate as a decimal: .2 
 Enter the minimum monthly payment rate as a decimal: .04 
 Month: 1 
 Minimum monthly payment: $192.0 
 Principle paid: $112.0 
 Remaining balance: $4688.0 
 Month: 2 
 Minimum monthly payment: $187.52 
 Principle paid: $109.39 
 Remaining balance: $4578.61 
 Month: 3 
 Minimum monthly payment: $183.14 
 Principle paid: $106.83 
 Remaining balance: $4471.78 
 Month: 4 
 Minimum monthly payment: $178.87 
 Principle paid: $104.34 
 Remaining balance: $4367.44 
 Month: 5 
 Minimum monthly payment: $174.7 
 Principle paid: $101.91 
 Remaining balance: $4265.53 
 Month: 6 
 Minimum monthly payment: $170.62 
 Principle paid: $99.53 
 Remaining balance: $4166.0 
 Month: 7 
 Minimum monthly payment: $166.64 
 Principle paid: $97.21 
 Remaining balance: $4068.79 
 Month: 8 
 Minimum monthly payment: $162.75 
 Principle paid: $94.94 
 Remaining balance: $3973.85 
 Month: 9 
 Minimum monthly payment: $158.95 
 Principle paid: $92.72 
 Remaining balance: $3881.13 
 Month: 10 
 Minimum monthly payment: $155.25 
 Principle paid: $90.56 
 Remaining balance: $3790.57 
 Month: 11 
 Minimum monthly payment: $151.62
 RESULT 
 Total amount paid: $2030.15 
 Remaining balance: $3615.74  """

outstanding_balance = float(raw_input("Enter the outstanding balance of your credit card: "))
annual_interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
minimum_monthly_payment_rate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))


monthly_interest_rate = annual_interest_rate/12.0
paid_amount = 0

for i in range(1,13):
	print("Month: "+ str(i))
 	minimum_monthly_payment = minimum_monthly_payment_rate * outstanding_balance
 	print("Minimum monthly payment: $"+ str(round(minimum_monthly_payment,2)))
 	paid_interest = monthly_interest_rate * outstanding_balance
 	paid_principal = minimum_monthly_payment - paid_interest
 	print("Principal paid: $"+ str(round(paid_principal, 2)))
 	outstanding_balance = outstanding_balance - paid_principal
 	print("Remaining balance: $"+ str(round(outstanding_balance,2)))
 	paid_amount = paid_amount + minimum_monthly_payment
 	if i ==12 :
 		print("RESULT\nTotal amount paid: $" + str(round(paid_amount,2)) + "\nRemaining balance: $"+ str(round(outstanding_balance,2)))
 	



