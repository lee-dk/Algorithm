import random

#함수선언부
def quickSort(ary):
    n = len(ary)
    if n <= 1:
        return ary
    pivot = ary[len(ary) // 2] # 기준값을 중간
    leftAry, rightAry = [],[]
    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
        return quickSort(leftAry) + [pivot] + quickSort(rightAry)





# 전역변수부
ary = [random.randint(100, 999) for _ in range(20)]

# 메인코드부
ary = quickSort(ary)
print('정렬 전 -->', ary)
