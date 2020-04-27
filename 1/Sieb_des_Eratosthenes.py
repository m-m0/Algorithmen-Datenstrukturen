def main():
    k = int(input("Enter a number: "))
    printTable(k)
    printPrimes(k)

def printTable(k):
    for i in range(k + 1):
        if i % 10 == 0 and i != 0:
            print(i)
        elif i == 0:
            pass
        elif i == 1:
            print(" ", end="  ")
        elif i < 10:
            print(i, end="  ")
        else:
            print(i, end= " ")

def printPrimes(k):
    table = []
    primes = []
    for i in range(2, k+1):
        table.append(i)
    
    for i in range(len(table)):
        j = table[i]
        if j != 0:
            primes.append(j)
            l = j
            c = 2
            while j < len(table): 
                j = l * c
                c += 1
                if j - 1 > len(table):
                    break
                table[j - 2] = 0
    print(primes)    


if __name__ == '__main__':
    main()
