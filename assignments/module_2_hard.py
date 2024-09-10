def get_password(n):
    result = ''
    for i in range(1, n):
        for k in range (2, n):
            if n % (i+k) == 0 and i<k:
                result += str(i)+str(k)
    return result
    
for i in range(3, 21):
    print(i, '-', get_password(i))
