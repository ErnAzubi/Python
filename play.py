products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

index = 0;
sum_of_prices = 0;
new_prices = []
total_revenue = 0;
less_than_30 = [];

while index < len(prices):
    sum_of_prices = sum_of_prices + prices[index]
    new_prices.append(prices[index] - 5)
    total_revenue = total_revenue + (prices[index] * last_week[index])
    index = index + 1


less_than_30 = [product for product, price in zip(products, new_prices) if price < 30]

#average price for products
avg_prices = sum_of_prices / len(prices)
avg_daily_sales = total_revenue/7

print("The total price average for all products is: ", round(avg_prices,2));
print("New price list is: \n", new_prices);
print("Total revenue generated from all packages: "+ str(total_revenue) +' $' );
print(f'Average daily revenue:${avg_daily_sales}')
print(f'Prices less than $30 are: \n {less_than_30}')
