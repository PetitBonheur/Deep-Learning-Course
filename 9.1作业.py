import tensorflow as tf
import numpy as np

import os  

os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   

x1=np.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
x2=np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
y=np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
x0=np.ones(len(x1))
X=tf.constant(np.stack((x0,x1,x2),axis=1))
Y=tf.constant(np.array(y).reshape(-1,1))


Xt=tf.transpose(X)
XtX_1=tf.linalg.inv(tf.matmul(Xt,X))
XtX_1_Xt=tf.matmul(XtX_1,Xt)
W=tf.matmul(XtX_1_Xt,Y)


print("请输入房屋的面积和房间数，预测房屋的销售价格")
x1_test=float(input("商品房面积："))
x2_test=int(input("房间数："))
if(x1_test>=20 and x1_test<=500):
    if(x2_test>=1 and x2_test<=10):

        y_pred=W[1]*x1_test+W[2]*x2_test+W[0]
        print("预测价格：",y_pred.numpy(),"万元")
    else:
        print("房间数应该在1-10之间")
else:
    print("房屋面积应该在20-500之间")