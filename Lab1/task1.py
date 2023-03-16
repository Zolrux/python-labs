def count_median(a, b, c):
   return 0.5 * ((2 * (b * b) + 2 * (c * c) - (a * a)) ** (1/2))

a = int(input("Введите сторону треугольника a: "))
b = int(input("Введите сторону треугольника b: "))
c = int(input("Введите сторону треугольника c: "))

res = count_median(a, b, c)
print(f"Длина медианы к стороне а: {res}")