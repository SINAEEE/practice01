
# 문제12
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

for i in range(1,99):
    i=str(i)
    if('3' in i):
        print(i," 짝")
    elif('6' in i):
        print(i," 짝")
    elif('9' in i):
        print(i," 짝")
    else:
        continue

