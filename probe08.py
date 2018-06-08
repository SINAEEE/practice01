

lst = []
print("5개의 정수를 입력하세요 : ")
for i in range(0,5):
    lst.append(input())
    lst[i] = num(lst[i])


print(lst)