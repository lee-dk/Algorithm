# def recursion():
#     print('나 불렀음?')
#     recursion()
#
#
# recursion()

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(10))