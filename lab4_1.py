# Варіант 12
# 
#   Дано список цілих чисел. Потрібно стиснути його,
#   перемістивши всі ненульові елементи в ліву частину списку,
#   не змінюючи їх порядок, а всі нулі - в праву частину.
#   Порядок ненульових елементів змінювати не можна,
#   додатковий список використовувати не можна,
#   завдання потрібно виконати за один прохід по списку.
#   Роздрукуйте отриманий список.
# 
# Дзюба Владислав

input_numbers = input()

numbers_str_list = input_numbers.split()

numbers = []
for num_str in numbers_str_list:
    numbers.append(int(num_str))

result = []

for num in numbers:
    if num != 0:
        result.append(num)

for num in numbers:
    if num == 0:
        result.append(num)

print(result)

