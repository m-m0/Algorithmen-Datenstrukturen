import random
import numpy as np

def main():
    a = np.array([int(random.random()*100) for _ in xrange(50)])
    print(a)
    MergeSort(a, 0, len(a)-1)
    print(a)


def MergeSort(a, f, l):
    if f < l:
        m = (f + l + 1) / 2
        MergeSort(a, f, m-1)
        MergeSort(a, m, l)
        Merge(a, f, l, m)

def Merge(a, f, l, m):
    n = l - f + 1
    a1f = f
    a1l = m - 1
    a2f = m
    a2l = l
    anew = np.zeros(len(a))
    i = 0

    while i < n:
        if a1f <= a1l:
            if a2f <= a2l:
                if a[a1f] <= a[a2f]:
                    anew[i] = a[a1f]
                    a1f += 1
                else:
                    anew[i] = a[a2f]
                    a2f += 1
            else:
                anew[i] = a[a1f]
                a1f += 1
        else:
            anew[i] = a[a2f]
            a2f += 1
        i += 1

    i = 0
    while i < n:
        a[f+i] = anew[i]
        i += 1


if __name__ == '__main__':
    main()
