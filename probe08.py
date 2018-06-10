
# 문제 8.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

lst = []
print("5개의 정수를 입력하세요 : ")
for i in range(0,5):
    lst.append(input())

t=0
for i in lst:
    i = int(i)
    t += i

avg = t/5

print("리스트 : ",lst)
print("평균 : ",avg)

