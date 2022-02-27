per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input('ввести сумму'))
stavki=per_cent.values()
deposit=list(map(round,[(lambda x: x*(money)/100)(x) for x in stavki] ))
print(deposit)
print('Максимальная сумма, которую вы можете заработать -',(max(deposit)), 'руб')

