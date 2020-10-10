
# 함수 선언부

def isStackFull() :     ## 스택이 무한루프를 돌지 않기 위해 // 스택이 꽉 찼는지 확인
    if (top == SIZE-1) :
        return True
    else :
        return False

def isStackEmpty():
    if (top == 0) :
        return True
    else :
        return False

def pop(data) :
    global stack, top
    if (isStackEmpty()):
        print("스택 없음!")
        return
    top -= 1
    stack[top]=data


def push(data) :        ## 데이터 넣기 함수
    global stack, top
    if (isStackFull()):
        print("스택 꽉참!")
        return
    top += 1
    stack[top]=data


#  전역변수 부
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


# 메인코드 부