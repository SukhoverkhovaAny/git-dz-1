# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:


LOWER_LIMIT = 0
UPPER_LIMIT = 1000

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)

count = 10
while count > 0:
    number = int(input("Input the number: "))
    if number > num:
        print("Less")
    elif number < num:
        print("More")
    else:
        print("Congratulations, you guessed right")
    count -= 1
else:
    print("No more attempts")