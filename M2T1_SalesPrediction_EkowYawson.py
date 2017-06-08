#Sales Prediction
#7 June 2017
#CTI-110 M2T1 - Sales Prediction
#Ekow Yawson


#User input projected amount of total sales
projected_sales = float(input("Input the \
projected amount of total sales \
for the current AY.\nUse the following format -- xxxxxx.xx: "))

#calc of profit -- 23% of total anual sales
profit = 0.23 * projected_sales

#output annual profit
print("The total projected profit for current year is: ")
print(format(profit, ',.2f'))
input("Press Enter to exit.")
