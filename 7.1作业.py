import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

img=Image.open("lena.tiff")
img_r,img_g,img_b= img.split()
plt.figure(figsize=(10,10))

plt.subplot(221)
plt.axis("off")
img_small=img_r.resize((50,50))
plt.imshow(img_small,cmap="gray")
plt.title("R-缩放",fontsize=14)

plt.subplot(222)

img1=img_g.transpose(Image.FLIP_LEFT_RIGHT)
img2=img1.transpose(Image.ROTATE_270)
plt.imshow(img2,cmap="gray")
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
plt.axis("off")
img_b1=img_b.crop((0,0,150,150))
plt.imshow(img_b1,cmap="gray")
plt.title("B-裁剪",fontsize=14)

img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
plt.subplot(224)
plt.axis("off")
plt.imshow(img_rgb)
plt.title("BGB",fontsize=14)

img_rgb.save("test.png")

plt.subplots_adjust(top=0.85)
plt.suptitle("图像基本操作",fontsize=20,color="blue")
plt.show()
