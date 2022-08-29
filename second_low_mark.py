if __name__ == '__main__':
    records = []
    names = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
    marks = [x[-1] for x in records]
    marks.sort()
    low = marks[1]

    for i in records:
        if i[-1] == low:
            names.append(i[0])
            names.sort()
    for name in names:
        print(name) 