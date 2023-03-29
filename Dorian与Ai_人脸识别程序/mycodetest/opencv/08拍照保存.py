#导入模块
import cv2
#摄像头
cap=cv2.VideoCapture(0)

falg = 1
num = 1

while(cap.isOpened()):#检测是否在开启状态
    ret_flag,Vshow = cap.read()#得到每帧图像
    cv2.imshow("Capture_Test",Vshow)#显示图像
    k = cv2.waitKey(1) & 0xFF#按键判断
    if k == ord('s'):#保存
       cv2.imwrite("jhc_picture/"+"jhc"+str(num)+".jpg",Vshow)
       print("success to save"+str(num)+".jpg")
       print("-------------------")
       num += 1
    elif k == ord('q'):#退出
        break
#释放摄像头
cap.release()
#释放内存
cv2.destroyAllWindows()



# **********
# bilibili：竞赛空间
# 公众号：竞赛空间
# 淘宝：竞赛空间
# **********