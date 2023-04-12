import random
import os
aa = 0
while aa < 1:
    print("======================================")
    num1 = [1,2,3,4,5]                       #定义三个任务位置的列表
    #第一次随机位置开始
    wz1= random.sample(num1,1)                 #随机出来一个位置，目前是列表形态
    weizhi1 = str(wz1[0])                       #赋值给weizhi1，方便输出
    print('有害垃圾回收的位置是：'+weizhi1)
    num1.remove(int(weizhi1))                   #删除掉这个位置的可能性
    #第一次终结
    wz1 = random.sample(num1,1)
    weizhi1 = str(wz1[0])
    print('垃圾处理站的位置是：'+weizhi1)
    num1.remove(int(weizhi1))
    #第二次终结
    #第三次
    wz1 = random.sample(num1,1)
    weizhi1 = str(wz1[0])
    print('废料运输的位置是：'+weizhi1)
    num1.remove(int(weizhi1))
    #第三次终结
    #开始随机后三个位置
    wz1 = random.sample(num1,1)
    weizhi1 = str(wz1[0])
    #print('附加题的位置是:'+weizhi1)
    num1.remove(int(weizhi1))

    print('===========================================')
    zhusun = input('按回车重新随机')

   # os.system('pause')         目前不可用
