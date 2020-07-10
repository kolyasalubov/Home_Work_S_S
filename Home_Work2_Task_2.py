# Задано чотирицифрове натуральне число.
# Знайти добуток цифр цього числа.
num = input("Enter number:")
result = int(num[0])*int(num[1])*int(num[2])*int(num[3])
print("Result: ", result)
# Посортувати цифри, що входять в дане число
# Записати число в реверсному порядку.
num1 = input("Enter number:")
list1 = [int(num1[0]),int(num1[1]),int(num1[2]),int(num1[3])]
list1.sort()
print(list1)
list1.reverse()
print(list1)