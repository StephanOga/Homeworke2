
#Вариант сперебором
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)


#Вариант с квадратным уравнением
summa, proizv = int (input('Ввдите суммы двух чисел')) , int(input('Введите произведение двух чисел'))
i = 1
x = -summa
y = proizv
d = x**2 - 4*i*y
x1 = (-x-d**0,5)/(2*i)
x2 = (-x+d**0,5)/(2*i)
print(x1,x2)
