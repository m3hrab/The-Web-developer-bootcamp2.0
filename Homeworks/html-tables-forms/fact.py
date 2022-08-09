n = input()
numbers = list(n)
result = 0
for number in numbers:
    number = int(number)
    total = 1
    for i in range(number,1,-1):
        total = total * i
    
    result += total

if result == int(n):
    print("%s is a strong number"%n)
else:
    print("%s is not a strong number"%n)
    
