product_name = 'Laptop'
price = 2490.99
discount = 0.10

first_letter = product_name[0]
# f - форматирование строк
# \n - перевод каретки
print(f'First letter is {first_letter} of {product_name}.', )

count = 2
total_price = price * count

# or and True False
has_discount = True
is_member = True
final_price = total_price

if has_discount and is_member:
    final_price = round(total_price - total_price*discount, 2)
print(f'Price with discount: {final_price} of products {product_name}\n')
