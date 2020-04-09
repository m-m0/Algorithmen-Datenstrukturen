import random

def main():
    a = [int(random.random()*100) for _ in xrange(50)]
    print(a)
    print(InsertionSortMin(a))

# Sortierung ueber Maximum
def InsertionSortMax(a):
    j = 1

    while j < len(a):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key
        j += 1
    return a

# Sortierung ueber Minimum
def InsertionSortMin(a):
    j = len(a) - 1

    while j >= 0:
        key = a[j]
        i = j + 1
        while i < len(a) and a[i] < key:
            a[i-1] = a[i]
            i += 1
        a[i-1] = key
        j -= 1
    return a
    
if __name__ == '__main__':
    main()
