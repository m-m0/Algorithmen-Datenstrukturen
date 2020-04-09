import random

def main():
    a = [int(random.random()*100) for _ in xrange(50)]
    print(a)
    print(SelectionSortMax(a))

# Minimum an richtige Stelle setzen
def SelectionSortMin(a):
    i = 0

    while i < len(a) - 1:
        j = i 
        minimum = j
        while j < len(a) - 1:
            if a[j] < a[minimum]:
                minimum = j
            j += 1
        a[i], a[minimum] = a[minimum], a[i]
        i += 1
    return a

# Maximum an richtige Stelle setzen
def SelectionSortMax(a):
    i = len(a) - 1

    while i >= 0:
        j = i
        maximum = j
        while j >= 0:
            if a[j] > a[maximum]:
                maximum = j
            j -= 1
        a[i], a[maximum] = a[maximum], a[i]
        i -= 1
    return a

if __name__ == '__main__':
    main()
