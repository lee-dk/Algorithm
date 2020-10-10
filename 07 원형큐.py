#함수선언부
def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear + 1) % SIZE == front):
        return True
    else:
        return False
def isQueueEmpty():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False
def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data
def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


#전역변수부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

#메인코드부
enQueue('A')
enQueue('B')
enQueue('B')
print(queue)
enQueue('D')
deQueue(); deQueue(); deQueue()
enQueue('E')
enQueue('F')
print(queue)
