def in2cm_table(start,end,step):
    lst=[]
    for i in range(start,end+1,step):
        lst.append((i, i*2.54))
        
    return lst