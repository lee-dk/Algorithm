#빈 배열 준비
katok = []

#배열 재일뒤에 친구 추가하는 함수
def add_data(friend):
    katok.append(None) #빈칸 추가
    kLen = len(katok) # 배열의 길이
    katok[kLen-1] = friend


def insert_data(position, friend): #위치 데이터
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

add_data('다현')
add_data('정연')
add_data('쯔위')
print(katok)

insert_data(1, '사나')
print(katok)

delete_data(2)
print(katok)