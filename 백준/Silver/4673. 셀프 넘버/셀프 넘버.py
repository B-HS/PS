self = [0 for _ in range(100000)] #만개짜리 스위치 쫙 설정
for n in range (1, 10000):
	self[n+(sum(map(int, str(n))))] = 1 #만개 쫙돌리면서 셀프넘버 아닌 것들 싹 스위치 켜고
    
for i in range(1, 10000):
	if self[i] == 0:
		print(i) # 셀프넘버 싸악 뽑기