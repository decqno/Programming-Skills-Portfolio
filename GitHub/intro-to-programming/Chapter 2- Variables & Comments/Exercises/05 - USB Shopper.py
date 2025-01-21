total_amount=50
price_each=6

sticks_bought=total_amount//price_each
money_spent=sticks_bought*price_each
remaining_money=total_amount%price_each

print("She can buy a total of", sticks_bought, "USB Sticks, spending a total of", money_spent, "euros.")
print("Therefore, she'll only have", remaining_money, "euros left in her wallet.")
