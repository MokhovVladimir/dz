n = [int(i) for i in input().split()]
if len(n) == 1:
    print("NO")
else:
    for i in range(1, len(n)):
        if n[i] <= n[i-1]:
            print("NO")
            break
    else:
        print("YES")
