# for문은 여러개의 리스트 중에서 하나씩 뽑아서 쓸때 쓰인다
# while문은 반복작업을 할때 쓰인다



test_list = ['one', 'two', 'three'] 
for a in test_list:        #리스트 하나씩 빼와서 a변수에 넣는다. 하나씩.
    print(a)

print("="*40)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)   # + - / * 다된다



