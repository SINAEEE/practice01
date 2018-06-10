
# 문제7.
# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전,
# 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.

num = input("금액 : ")
num=int(num)

def cal(num):
    r,r1 = divmod(num,50000)
    r2,r3 = divmod(r1,10000)
    r4,r5 = divmod(r3,5000)
    r6,r7 = divmod(r5,1000)
    r8,r9 = divmod(r7,500)
    r10,r11 = divmod(r9,100)
    r12,r13 = divmod(r11,50)
    r14,r15 = divmod(r13,10)
    r16,r17 = divmod(r15,5)
    r18,r19 = divmod(r17,1)

    return r,r2,r4,r6,r8,r10,r12,r14,r16,r18


keys=("50000원","10000원","5000원","1000원","500원","100원","50원","10원","5원","1원")
values =cal(num)

d=dict(zip(keys,values))

for k,v in d.items():
    print("{0} : {1}개".format(k,v))


