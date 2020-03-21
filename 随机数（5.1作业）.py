import numpy as np
np.random.seed(612)
b=np.random.rand(1000)
i=int(input("请输入一个0-100的数字:"))
if(i>100 or i<0):
    print("输入的数字超过范围")
else:
    n=i-1
    j=1
    while(n<1000):
        print("{0}\t{1}\t{2}\t" .format(j,n+1,b[n]))
        n=n+i
        j=j+1
