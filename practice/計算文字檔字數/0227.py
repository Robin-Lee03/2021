products = []
while True:
    name = input('Enter a product: ')
    if name == '-1':
        break
    price = int(input('Enter a price: '))
    p = [name, price]

    products.append(p)
print(products)

