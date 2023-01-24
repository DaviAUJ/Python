mtz = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
        mtz[i].append(int(input(f"Valor para [{i}, {c}]: ")))

for i in range(0, 3):
    print(f"[{mtz[i][0]:^5}][{mtz[i][1]:^5}][{mtz[i][2]:^5}]")
 