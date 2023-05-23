"""Задача 8: Требуется определить, 
можно ли от шоколадки размером n × m долек отломить ровно 
k долек, если разрешается сделать один разлом по 
прямой между дольками (то есть разломить шоколадку на два прямоугольника).

3 2 4 -> yes
3 2 1 -> no"""

n = int(input("Input lenght: "))
m = int(input("Input width: "))
k = int(input("Input ammount of pieces: "))

if k%2!=0 and n==k or m==k:
    print("YES")
elif k%2==0 and n*m>=k and n*m%2==0:
    print("YES")
else:
    print("NO")