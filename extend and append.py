product_list_samsung = ['galexyA1','galexyA2','galexy A3','Galaxys 10','galaxy s10 pro']
product_list_xiami = ["note 8 pro","not 7 light",'note 10 pro','mi 10']
while True:
    new_product =input("Enter new product: -f to finish-")
    if new_product == "f":
        break
    brand = input("Enter brand name: x for xiami s for samsung:")
    if brand == 's':
       product_list_samsung.append(new_product)
    if brand == 'x':
        product_list_xiami.append(new_product)


print("Samsung product list is :")

for product in product_list_samsung:
    print(product)

print("xiami product list is :")
for product in product_list_xiami:
    print(product)

print("\n")
all_products = product_list_samsung
all_products.extend(product_list_xiami)
print("all products are:")

for product in all_products:
    print(product)






