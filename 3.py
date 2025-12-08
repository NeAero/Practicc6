x1, y1 = map(int, input("ввод  стрики и стобца первкой клетки").split())
x2, y2 = map(int, input("ввод  стрики и стобца второй клетки").split())

if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")