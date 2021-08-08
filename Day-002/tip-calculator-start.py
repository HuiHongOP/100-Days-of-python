#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


print("Welcome to the tip calculator!\n")

#Ask user for total amount of the bill
total_bill = float(input("What was the total bill? "))

#Ask user for input tip percetange
percentage_tip = int(input("What is the tip percentage you guys want to give? 12, 15, or 18? "))

#The number of people  is splitting among the bill
number_of_split = int (input("How many people are going to split up the bill? "))

#Converter tip percentage multiplier
tips_multiplier= 1+(percentage_tip/100)

#The price that each person is going to pay
each_person_price = (total_bill/number_of_split)* tips_multiplier

#Setting the decimal place to the hundredths
decimal_precision= "{:.2f}".format(each_person_price)

#Display the output of individual price
print(f"Each person should pay: {decimal_precision}")
