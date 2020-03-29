import tensorflow as  tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
x=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

x1=tf.reduce_sum(x)/10
y1=tf.reduce_sum(y)/10
i=1
s1=0
s2=0
while(i<10):
    s1+=(x[i]-x1)*(y[i]-y1)
    s2+=(x[i]-x1)**2
    i=i+1
w=s1/s2
b=y1-w*x1
print("w为：{0},b为：{1}".format(w,b))