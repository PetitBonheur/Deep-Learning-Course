import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
(train_x,train_y),(test_x,test_y)=mnist.load_data()

for i in range(16):
    num = np.random.randint(1,50000)
    plt.subplot(4,4,i+1)
    
    plt.axis("off")
    plt.imshow(train_x[num],cmap="gray")
    plt.title("标签："+str(train_y[num]),fontsize=16)
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.suptitle("MNIST测试集样本",fontsize=20,color="red")
plt.show()