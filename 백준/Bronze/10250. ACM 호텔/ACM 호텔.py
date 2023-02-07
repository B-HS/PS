for i in range(int(input())):
    h,w,guest = map(int,input().split())
    floor = guest%h
    room_number = guest//h+1
    if guest%h ==0:
        floor = h
        room_number -=1
    print(floor*100+room_number)