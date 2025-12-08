x1, y1 = map(int, input("ввод  стрики и стобца первкой клетки").split())
x2, y2 = map(int, input("ввод  стрики и стобца второй клетки").split())

if (x1==x2 or y1==y2) or (abs(x1 - x2) == abs(y1 - y2)):
    print("YES")
else:
    print("NO")