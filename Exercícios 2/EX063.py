n = int(input('\nQuantos termos da sequência de fibonacci você quer ver? '))

pool = 0
seqfib = [0, 1]

while pool != n:
    print(seqfib[pool], end=' -> ')
    seqfib.append(seqfib[pool] + seqfib[1 + pool])
    pool += 1
print('FIM')
