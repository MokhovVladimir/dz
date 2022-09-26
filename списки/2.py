num = input()

s = {}
for i in range(10):
    s.setdefault(i, num.count(str(i)))
print(s)
