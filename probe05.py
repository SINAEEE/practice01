

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

#문제5.
#1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에
# 중복 없이 각 단어를 순서대로 출력하세요.

print()
result = s.upper().replace(',','').replace('.','').replace('\n','').split()

s=set(result)
r2=sorted(s)

for i in r2:
    print(i)

print()


