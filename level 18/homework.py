
num1 = int(input("შეიყვანეთ პირველი რიცხვი (num1): "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი (num2): "))

total_sum = 0 


if num1 > num2:
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            print(i)
            total_sum += i 

else:
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i)
            total_sum += i


print(f"დაბეჭდილი რიცხვების ჯამი: {total_sum}")
