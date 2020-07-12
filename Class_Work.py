# Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.
a = input("Enter number:")
b = input("Enter number:")
if a > b:
    print("a>b is", a > b)
elif a < b:
    print("a<b is", a < b)
elif a == b:
    print("a=b is not", a == b)

# Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.
a = int(input("Enter number:"))
if a % 2 == 0:
    print("Ви ввели парне число")
else:
    print("Ви ввели не парне число")

# Написати скрипт, який обчислить факторіал введеного числа.
n = int(input("Enter number:"))
fl = 1
for i in range(2, n + 1):
    fl *= i
print("Resuls:", fl)