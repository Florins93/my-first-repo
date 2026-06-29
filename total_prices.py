def calculate_total_prices(products):
    total_prices = []

    for product in products.values():
        total = product["quantity"] * product["price"]
        total_prices.append(total)

    return total_prices