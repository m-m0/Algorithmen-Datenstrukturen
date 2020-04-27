def main():
    a = 4
    b = 2
#    iterativ(a, b)
    #recursiv(a, b)

    kgV(a,b)

def iterativ(a, b):
    r = b
    while a % b != 0:
        r = a % b
        a = b
        b = r
    print(r)

def recursiv(a, b):
    if a % b == 0:
        print(b)
    else:
        recursiv(b, a % b)

def kgV(a, b):
    pa = primfaktorzerlegung(a)
    pb = primfaktorzerlegung(b)
    print(pa)
    print(pb)
    s = 0
    if len(pa) > len(pb):
        for c in range(len(pa)):
            countera = 0
            counterb = 0
            for i in range(len(pa)):
                if pa[c] == pa[i]:
                    countera += 1
            for j in range(len(pb)):
                if pa[c] == pb[j]:
                    counterb += 1
            if countera > counterb:
                s += countera * pa[c]
            else:
                s += counterb * pa[c]
    else:
        for c in range(len(pb)):
            countera = 0
            counterb = 0
            for i in range(len(pa)):
                if pb[c] == pa[i]:
                    countera += 1
            for j in range(len(pb)):
                if pb[c] == pb[j]:
                    counter += 1
            if countera > counterb:
                s += countera * pb[c]
            else:
                s += counterb * pb[c]
    print(s)

def primfaktorzerlegung(x):
    l = []
    i = 2
    if x > 2:
        end = x / 2 
        while i <= end:
            if x % i == 0:
                x /= i
                l.append(i)
            else:
                i += 1
    else:
        l.append(x)
    return l

if __name__ == '__main__':
    main()
