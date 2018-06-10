

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

print()
result = s.upper().replace(',','').replace('.','').replace('\n','').split()

s=set(result)
r2=sorted(s)

for i in r2:
    print(i)

print()


