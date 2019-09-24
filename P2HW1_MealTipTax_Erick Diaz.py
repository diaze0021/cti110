#For this assignment you will create a program that calculates the total amount of a meal purchased at a restaurant
#September 18, 2019
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Erick Diaz
#

#Assume 6% sales tax
#Assume 15% Tip

#3.charge of food meal cost $19 
#4.Tips for the meal is 30%, .30
#5.Taxs for the meal is 6%, .06
#6.For taxes and tips together will be, .06 * .30 is $25.84  
#7.Cost for meal is $19 plus tips and taxes will be $25.84 

meal = float(input("How much did your meal cost?"))
total_cost = meal + (meal * .06) + (meal * .30)

print ("your total meal cost is $ %.2f" % total_cost)
