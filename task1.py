# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого 
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше 
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("Input the length of side a: "))
b = int(input("Input the length of side b: "))
c = int(input("Input the length of side c: "))

if a > (b + c) or b > (a + c) or c > (a + b):
    result = "A triangle with such sides doesn't exist"
elif a == b == c:
    result = "Equilateral triangle"
elif a != b != c != a:
    result = "Scalene triangle"
elif a == b != c or a != b == c or a == c != b:
    result = "Isosceles triangle"
print(result)