import solution

print("Введите имя файла")
filename = input()
print("Введите режим")
rezh = input()

with open(filename, 'r') as f, open('output.txt', 'w') as d:
    if rezh == 'Ces':
        a = f.read()
        b = solution.CeaserEng(a)
    if rezh == 'Vin':
        a = f.read()
        b = solution.VinigEng(a)
    if rezh == 'Ver':
        a = f.read()
        b = solution.Verman(a)
    if rezh == 'Desc':
        a = f.read()
        b = solution.Descifr(a)
    d.write(b)
