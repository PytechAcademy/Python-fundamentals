# Calculate Profit and loss
SP = float(input('Enter the selling price: '))
CP = float(input('Enter the cost price: '))
if SP > CP:
    profit = SP - CP
    pp = (profit/CP)*100
    round_pp = round(pp, 2)
    print("Profit is {} and Profit Percentage is {}".format(profit,round_pp))
elif CP > SP:
    loss = CP - SP
    lp = (loss/CP)*100
    round_lp = round(lp,2)
    print("Loss is {} and Loss Percentage is {}".format(loss, round_lp))
else:
    print("There is no profit no loss.")
