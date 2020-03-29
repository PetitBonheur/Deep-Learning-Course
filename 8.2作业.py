import tensorflow as  tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
x=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])


x1=x*y
x2=(tf.reduce_sum(x1)-x1[0])*10

x3=tf.reduce_sum(x)-x[0]
y1=tf.reduce_sum(y)-y[0]

s1=x2-x3*y1

x4=x**2

s2=10*(tf.reduce_sum(x4)-x4[0])-tf.reduce_sum(x)**2

w=s1/s2
print("W为{0}".format(w.numpy()))

b=((tf.reduce_sum(y)-y[0])-w*(tf.reduce_sum(x)-x[0]))/10
print("b为{0}".format(b.numpy()))
