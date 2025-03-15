1)
def generate(n):
    for i in range(1, n+1):
        yield i**2
n = int(input())
squares_generate = generate(n)
for square in squares_generate:
    print(square)


2)
def even_numbers_generator(n):
    for i in range(0, n+1, 2):
        yield i
n = int(input())
even_numbers = even_numbers_generator(n)
print(", ".join(map(str, even_numbers)))

3)
def divisible_by_3_and_4(num):
    for i in range(0, num+1):
        if i % 12 == 0:
            yield i
num = int(input())
numbers = divisible_by_3_and_4(num)
for number in numbers:
    print(number)

4)

def generate(a, b):
    for i in range(a, b+1):
        yield i**2
a = int(input())
b = int(input())
squares_generate = generate(a, b)
for square in squares_generate:
    print(square)


5) 
def countdown(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
nums = countdown(n)
for num in nums:
    print(num)

