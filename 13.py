ticket = int(input('Ввести количество билетов '))
price = []
for i in range(1, ticket+1):
    age = int(input(f"Возраст {i} посетителя "))
    if age < 18:
        price.append(0)
    elif 18 <= age < 25:
        price.append(990)
    elif age >= 25:
        price.append(1390)
print(price)
total_price = int(sum(price) - sum(price)/10) if ticket > 3 else sum(price)
print ("Сумма к оплате: ", total_price, 'руб')