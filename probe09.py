
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
