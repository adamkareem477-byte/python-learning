
business= input ("What's your business name?")
sold= int(input("How many products were sold?"))
price= float (input("How much do you sell the product for?"))
cost= float (input("How much does the product cost?"))
print (f"Bussiness name: {business}")
print (f"Products sold: {sold}")
print (f"Price per product: {price}")
print (f"cost per product: {cost}")
def calculate_profit(sold,price,cost):
    profit= (sold*price-sold*cost)
    return profit
profit= calculate_profit(sold,price,cost)
revenue= (sold*price)
total= (sold*cost)
print (f"Total revenue:{revenue}")
print (f"Total costs:{total}")
print (f"Profit: {profit}")
print (f" Great job! Your business made {profit} profit") 



