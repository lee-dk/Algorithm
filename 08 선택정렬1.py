import random
def findMinPos(ary):
    minIdx = 0
    for i in range(0, len(ary)):
        if(ary[minIdx] > ary[i]):
            minIdx = 1
    return minIdx


#전역변수부
before = [random.randint(100,999) for _ in range(20)]
after = []

#메인코드부
print('정렬 전 -->', before)
for _ in range(len(before)):
    minPos = findMinPos(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 -->', after)
