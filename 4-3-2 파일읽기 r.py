with open("C:/영양제의정석/새파일.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in [0, 4]:  # 0-based index라 1번째는 0, 5번째는 4
        if i < len(lines):
            print(lines[i], end='')
