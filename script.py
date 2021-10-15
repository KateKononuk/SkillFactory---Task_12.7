per_cent = {
    'ТКБ': 5.6, 
    'СКБ': 5.9, 
    'ВТБ': 4.28, 
    'СБЕР': 4.0
}

deposit = []
money = int(input())
deposit.append(int(money * round(per_cent.get('ТКБ') /100, 4)) )
deposit.append(int(money * round(per_cent.get('СКБ') /100, 4) ))
deposit.append(int(money * round(per_cent.get('ВТБ') /100, 4) ))
deposit.append(int(money * round(per_cent.get('СБЕР') /100, 4) ))
print(deposit)
print('Максимальная сумма, которую вы можете заработать - ' + str(max(deposit)))
