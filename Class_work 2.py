# Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.
a=input("Enter number:")
b=list(a); my1 = min(a); my2 = max(a)
print("Min numbers:{} Max numbers:{}".format(my1, my2))
# В інтервалі від 1 до 10 визначити числа
#  парні, які діляться на 2,
#  непарні, які діляться на 3,
#  числа, які не діляться на 2 та 3.
ev1 = []
ev2 = []
ev3 = []
for i in range(10):
    if i%2==0:
        ev1.append(i)
    elif i%3==0:
        ev2.append(i)
    else:
        ev3.append(i)
print("Ev1 results:{}\nEv2 results:{}\nEv3 results:{}\n".format(ev1,ev2,ev3))
# Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
n = int(input("Enter number:"))
fl = 1
for i in range(2, n + 1):
    fl *= i
print("Resuls:", fl)