# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
limit = 100000
number = int(input("Input the number from 0 before 100 000: "))
if number < 0 or number > limit:
    print("You entered a number out of range")
elif number == 0 or number == 1:
    print("Number is not prime or composite")
else:
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
            if count == 2:
                result = "Prime number"
            else:
                result = "Composite number"
    print(result)