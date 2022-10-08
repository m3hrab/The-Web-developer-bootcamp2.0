a =  [25, 35, 872, 228, 53, 278, 872]

def check_digit(n):
    n = str(n)
    digits = []
    # make the number into a single digit list
    for i in n:
        digits.append(int(i))
    # remove the duplicate digits in digits
    unique = list(dict.fromkeys(digits))
    # Sort the digits list
    unique.sort()
    return unique

count = 0
for i in range(len(a)-1):
    n = check_digit(a[i])
    for j in range(i+1,len(a)):
        m = check_digit(a[j])
        if n == m:
            count += 1

print(count)



            
