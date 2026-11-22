result1 = []
n = 10
while n <= 99:
    tens = n // 10
    ones = n % 10
    if n == 2 * (tens + ones) * 3:
        result1.append(n)
    n = n + 1
print("Task 1:", result1)

result2 = []
n = 100
while n <= 999:
    hundreds = n // 100
    tens = (n // 10) % 10
    ones = n % 10
    if hundreds < tens and tens < ones:
        result2.append(n)
    n = n + 1
print("Task 2:", result2)

n = 1
found = False
while found == False:
    temp = n
    reversed_n = 0
    while temp > 0:
        reversed_n = reversed_n * 10 + temp % 10
        temp = temp // 10
    if reversed_n == 4 * n:
        found = True
    else:
        n = n + 1
print("Task 3:", n)

n = int(input("Enter a number for the Harshad check: "))
temp = n
digit_sum = 0
while temp > 0:
    digit_sum = digit_sum + temp % 10
    temp = temp // 10
if n > 0 and n % digit_sum == 0:
    print("Task 4:", n, "is a Harshad number")
else:
    print("Task 4:", n, "is not a Harshad number")

result5 = []
a = 1
while a <= 100:
    b = 1
    while b <= 100:
        if a + b == a * b:
            result5.append((a, b))
        b = b + 1
    a = a + 1
print("Task 5:", result5)