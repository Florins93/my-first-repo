import csv
from total_prices import calculate_total_prices
from total_sum import total_sum
from calculate_average_price import calculate_average

def read_products(file):
    products = {}

    with open(file, "r") as fisier:
        reader = csv.DictReader(fisier, skipinitialspace=True)

        for row in reader:
            products[row["product_name"]] = {
                "quantity": int(row["product_quantity"]),
                "price": float(row["product_price"])
            }

    return products

products = read_products("products/product_info.csv")

prices = calculate_total_prices(products)

sum = total_sum(prices)

average = calculate_average(prices)

print(f'Suma totala a produselor este : {sum}')

print(f'Media preturilor este: {average}')