n = 1999
result = True

for i in range(2, n):
    if n % i == 0:
        result = False
            
print(result)