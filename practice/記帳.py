product = []
while True:
    name = input('請輸入商品名稱: ')
    if name == '-100':
        break
    price = input('請輸入商品價格: ')
    # p = []
    # p.append(name)
    # p.append(price)
    p = [name, price]
    product.append(p)
print(product)

for p in product:
    print(p[0],'的價格是: ', p[1])

with open('product.csv','w', encoding='utf-8')as f:
    f.write('商品,價格\n')
    for p in product:
        f.write(p[0]+','+ p[1] + '\n')