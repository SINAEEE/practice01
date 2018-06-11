
# 문제11.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def sum(*args):
    result=0
    for i in args:
        result += i

    return result


print(sum(1,2))
print(sum(1,2,3))
print(sum(1,1,1,1,1,1))
print(sum(1,2,3,4,5,6,7,8,9,10))

