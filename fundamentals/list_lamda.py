# just a little exercise to learn more about list_comprehension,
# filter and map with lamda.

products = [
    {"name": "Laptop", "price": 1200, "in_stock": True},
    {"name": "Mouse", "price": 25, "in_stock": False},
    {"name": "Keyboard", "price": 45, "in_stock": True},
    {"name": "Monitor", "price": 300, "in_stock": True},
    {"name": "Headphones", "price": 80, "in_stock": False},
    {"name": "Phone", "price": 800, "in_stock": True},
    {"name": "Keyboard", "price": 1200, "in_stock": False},
]

response_with_list_comprehension = sorted(
    [product["name"].lower() for product in products if product["price"] > 100 and product["in_stock"] == True],
    reverse=True
)

filter_result = filter(lambda product: product["price"] > 100 and product["in_stock"] == True, products)
map_result = map(lambda product: product["name"].lower(), filter_result)
response_with_lambda = sorted(list(map_result), reverse=True)

print(response_with_list_comprehension)
print(response_with_lambda)
