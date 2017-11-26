a_total = 125
a_bought = 25.32
a_sold = 48.97
a_profit = a_total * (a_sold - a_bought)
b_current = 127.99
b_discount = 0.16 #or 16%
b_sale = b_current - (b_current * b_discount)

print 'Profit from stock a: ${0:,.2f}'.format(a_profit)
print 'Sale price of stock b: ${0:,.2f}'.format(b_sale)
