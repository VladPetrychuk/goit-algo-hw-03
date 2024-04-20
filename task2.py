import random

def get_numbers_ticket(min_num, max_num, quantity):

    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        print("Неправильні вхідні параметри.")
        return []

    unique_numbers = set()

    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min_num, max_num))

    return sorted(list(unique_numbers))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)