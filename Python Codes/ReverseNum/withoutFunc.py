num = int(input("Enter Number: "))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)


'''
num = int(input("Enter Number: "))
print(str(num)[::-1])
'''