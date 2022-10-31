with open("count_blabla.txt", "r") as face_monk:
    p = []
    for i in face_monk.readlines():
        for j in i.split():
            p.append(j.strip(':.,!?'))
    otv = {i: p.count(i) for i in p}

print(sorted(otv, key= lambda x: otv[x])[-1])
