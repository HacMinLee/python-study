# add_data.py
f = open("C:/영양제의정석/새파일.txt",'a',encoding='utf-8')
for i in range(11, 20):
    data = "%d번째 줄 추가요~.\n" % i
    f.write(data)
f.close()
