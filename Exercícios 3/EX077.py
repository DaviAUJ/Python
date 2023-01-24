words = ("Aprender", "Programar", "Linguagem", "Python", 
"Curso", "Gratis", "Estudar", "Praticar", "Trabalhar", 
"Mercado", "Programador", "Futuro")

for i in words:
    print(f"\nNa palavra '{i}' temos: ", end='')

    for v in i:
        if v.lower() in 'aeiou':
            print(f'[{v.lower()}]', end='')
