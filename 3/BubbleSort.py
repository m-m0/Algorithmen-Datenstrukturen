import random

def main():
    a = [int(random.random()*100) for _ in xrange(50)]
    print(a)
    print(BubbleSortMax(a))

# Minimum wandert nach vorne
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

# Maximum wandert nach hinten
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
