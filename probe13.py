

num=input("숫자를 입력하세요 : ")
num=int(num)

r=0
if num%2==0:
    n=num+1
    for i in range(1,n,1):
        #print(i)
        if i%2==0:
           r += i
    print("결과 값 : ",r)
else:
    n=num+1
    for i in range(1,n,1):
        #print(i)
        if i%2==1:
           r += i
    print("결과 값 : ",r)


