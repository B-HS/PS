for _ in range(int(input())):
    k = int(input()) # 층
    n = int(input()) # 호
    apt = [i for i in range(1,n+1)] #0층 미리 채우기
    #1~n
    for _ in range(k): #층만큼 for문
        for i in range(1,n): #미리계산된 리스트의 다음층 계산을위한 해당 호까지의 for문
            apt[i] = apt[i-1] + apt[i] #선택된 i호 = apt i-1(바로 옆 호) + apt(바로 밑호 (왜냐면 그다음 수는 아직 계산x))
    
    print(apt[-1])#계산이 끝까지 가면 마지막 n호의 수가 계산되었으므로 마지막수를 출력 -1