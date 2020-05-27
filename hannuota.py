def hannoi(num,src,dst,temp=None):
    #src是初始位置，dst是目标位置，temp是临时位置
    global times
    assert type(num)==int, 'num must be integer'
    assert num > 0,'num must>0'
    if num==1:
        print('the {0} times move:{1}==>{2}'.format(times,src,dst))
        times+=1
    else:
        hannoi(num-1,src,temp,dst)
        hannoi(1,src,dst)
        hannoi(num-1,temp,dst,src)
times=1
hannoi(3,'a','b','c')
