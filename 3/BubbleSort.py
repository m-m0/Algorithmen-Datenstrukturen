def main():
    a = [12, 34, 12, 45, 2, 56, 2, 4, 6, 7]
    print(a)
    BubbleSortMax(a)
    print(a)

# minimum wandert nach vorne
def BubbleSortMin(a):
    i = 0

    while i < len(a):
        j = len(a) - 1
        while j > i:
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            j -= 1
        i += 1
    return a

# maximum wandert nach hinten
def BubbleSortMax(a):
    i = len(a)

    while i > 0:
        j = 0
        while j < i - 1:
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            j += 1
        i -= 1
    return a

if __name__ == '__main__':
    main()
