"""Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с 
номером. Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. Т.е. 
билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no"""

ticketNumber = int(input("Input ticket number: "))

a = ticketNumber//100000
b = ticketNumber//10000%10
c = ticketNumber//1000%10
d = ticketNumber//100%10
e = ticketNumber//10%10
f = ticketNumber%10

if a+b+c == d+e+f:
    print("You've got a lucky ticket")
else:
    print("You've got standart ticket")