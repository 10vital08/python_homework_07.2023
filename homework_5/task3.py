"""
Напишите однострочный генератор словаря, который принимает на вход
три списка одинаковой длины: имена str, ставка int, премия str с
указанием процентов вида “10.25%”. В результате получаем словарь с
именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

list_1 = ['Василий', 'Григорий', 'Борис']
list_2 = [1000, 500, 20000]
list_3 = ['10.2%', '5.76%', '30%']

gen_dict = {list_1[i]: list_2[i] * (float(list_3[i][:-1]) / 100) for i in range(len(list_1))}

print(gen_dict)