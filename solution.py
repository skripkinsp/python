alEng = 'abcdefghigklmnopqrstuvwxyz'
alRu = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
from collections import Counter


def XOR(st, key):
    result = ''
    stcopy = st
    keycopy = key
    a = len(st)
    b = len(key)
    if a < b:
        stcopy = '0' * (b - a) + st
    elif b < a:
        keycopy = '0' * (a - b) + key
    for i in range(max(a, b)):
        if stcopy[i] == keycopy[i]:
            result += '0'
        else:
            result += '1'
    return result


def binary(a):
    result = 0
    for i in range(len(a)):
        if a[i] == '1':
            result += 2**(len(a) - i)
    return result


def CeaserEng(st):
    st2 = ''
    print("Введите ключ")
    step = int(input())
    for i in range(len(st)):
        up = False
        if st[i].isupper():
            up = True
        a = alEng.find(st[i].lower())
        if a >= 0:
            if up:
                st2 += alEng[(a + step) % 26].upper()
            else:
                st2 += alEng[(a + step) % 26]
        else:
            st2 += st[i]
    return st2


def CeaserRu(st):
    st2 = ''
    print("Введите число")
    step = int(input())
    for i in range(len(st)):
        up = False
        if st[i].isupper():
            up = True
        a = alRu.find(st[i].lower())
        if a >= 0:
            if up:
                st2 += alRu[(a + step) % 33].upper()
            else:
                st2 += alRu[(a + step) % 33]
        else:
            st2 += st[i]
    return st2


def VinigEng(st):
    st2 = ''
    print("Введите ключ")
    codeword1 = input()
    codeword = codeword1.lower()
    lencodeword = len(codeword)
    j = 0
    for i in range(len(st)):
        up = False
        if st[i].isupper():
            up = True
        a = alEng.find(st[i].lower())
        if a >= 0:
            b = alEng.find(codeword[j % lencodeword])
            if up:
                st2 += alEng[(a + b) % 26].upper()
            else:
                st2 += alEng[(a + b) % 26]
            j += 1
        else:
            st2 += st[i]
    return st2


def VinigRu(st):
    st2 = ''
    print("Введите ключ")
    codeword1 = input()
    codeword = codeword1.lower()
    lencodeword = len(codeword)
    j = 0
    for i in range(len(st)):
        up = False
        if st[i].isupper():
            up = True
        a = alRu.find(st[i].lower())
        if a >= 0:
            b = alRu.find(codeword[j % lencodeword])
            if up:
                st2 += alRu[(a + b) % 33].upper()
            else:
                st2 += alRu[(a + b) % 33]
            j += 1
        else:
            st2 += st[i]
    return st2


def Verman(st):
    print('Введите кодовое слово')
    codeword = input()
    size_code = len(codeword)
    size = len(st)
    result = ''
    listofcw = []
    listofst = []
    result_list = []
    for i in codeword:
        a = str(bin(ord(i)))[2:]
        listofcw.append(a)
    for i in st:
        a = str(bin(ord(i)))[2:]
        listofst.append(a)
    for i in range(size):
        result_list.append(XOR(listofst[i % size], listofcw[i % size_code]))
    for i in result_list:
        result += chr(binary(i))
    return result


def Descifr(st):
    df = st
    df.lower()
    b = Counter(st)
    n = (b.most_common(1)[0][0]).lower()
    a = ord(n) - ord('e')
    st2 = ''
    step = a
    for i in range(len(st)):
        up = False
        if st[i].isupper():
            up = True
        a = alEng.find(st[i].lower())
        if a >= 0:
            if up:
                st2 += alEng[(a - step) % 26].upper()
            else:
                st2 += alEng[(a - step) % 26]
        else:
            st2 += st[i]
    return st2

