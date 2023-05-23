"""Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """

num = int(input("Input 3-digit number: "))

a = num%10
b = num//100
c = num//10%10

sum = a+b+c
print(sum)