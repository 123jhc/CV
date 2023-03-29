import os

imagePath = './jhc_picture/jhc11.jpg'
# print(os.path.split(imagePath)[1].split('.')[0][3:])
name = str(os.path.split(imagePath)[1].split('.',1)[0][0:3])
print(name)