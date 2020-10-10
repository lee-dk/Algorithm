class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNode():
    current = node
    print(current.data, end='-->')
    while (current.link != None):
        current = current.link
        print(current.data, end='-->')
    print()

#전역변수부
memory = []
head, cur, pre = None, None, None #시작노드, 현재노드, 앞노드
dataAry = ['다현', '정연', '쯔위']

#메인코드부
if __name__=='__main__':
    node = Node()
    node.data = dataAry[0]
    head = node
    memory.append(node)
    for data in dataAry[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
    printNode(head)