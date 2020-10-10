import random
def selectionSort(arr):
    n = len(arr)    #4개 라고가정하면
    for i in range(0, n-1): #사이클3회
        minIdx = i
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                minIdx = k
        # tmp = ary[i]
        # ary[i] = ary[minIdx]
        # ary[minIdx] = tmp
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary

#전역변수부
ary = [random.randint(100,999) for _ in range(20)]

#메인코드부
print('정렬 전 -->', ary)
ary = selectionSort(ary)
print('정렬 후 -->', ary)
