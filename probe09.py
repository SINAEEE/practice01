
# 문제9.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

str1 = input("입력 > ")
lst=[]

for i in str1:
    lst.append(i)

lst.reverse()

str2=""
for i in lst:
    str2 += i

print("결과 > ",str2)



"""
str1 = input("입력 > ")

result=str1[::-1]
print(result)
"""

