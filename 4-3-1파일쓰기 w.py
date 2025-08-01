# 새파일 지정한 장소에 만들기
f = open("C:\영양제의정석/새파일.txt", 'w',encoding='UTF-8')#인코딩 UTF-8은 한글깨지면 넣어줌 
#         경로           파일명.성질. 작성가능메모장. 깨짐방지

for i in range(1, 12):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()
