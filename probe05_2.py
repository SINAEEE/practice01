


s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

print()
result = s.upper().replace(',','').replace('.','').replace('\n','').split()

r2=sorted(result)

d={}

for i in r2:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for k,v in d.items():
    print("{}:{}".format(k,v))

