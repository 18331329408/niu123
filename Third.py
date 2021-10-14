
import random
# 1、实现输入10个数字，并打印10个数的求和结果


# n=0
# for i in range(0,10):
#     a=int(input("请输入10个数："))
#     n += a
#
# print(n)
#print(n/10)


# 2、从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。


# list=[]
# 
# for i in  range (5):
#     num=int(input("请输入整数"))
#     list.append(num)
# 
# for num in list:
#         max=0
#         if num>list[max]:
#           list [max]=num
# 
# print("列表为最大数为:{},最大数为:{}".format(list,list[max]))









# 3、使用random模块，如何产生 50~150之间的数？


# ran=random.randint(50,150)
# print(ran)




















# 4、从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）



# a=int(input("请输入边长:"))
# b=int(input("请输入边长:"))
# c=int(input("请输入边长:"))
# if a+b>c and b+c>a and c+a>b:
#     print("可以构成三角形")
#     if a==b==c:
#          print("等边三角形")
#     elif a==b!=c or a==c!=b or b==c!=a:
#          print("等腰三角形")
#     elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")



# 5、有以下两个数，使用+，-号实现两个数的调换。


# A=56 B=78实现效果：A=78 B=56
# A=56
# B=78
# c=0
# c=A+B
# B=c-B
# A=c-A
# print(A)
# print(B)
import time


# 6、实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）


# name = 'root'  # 正确的用户名
# passwd = 'admin'  # 正确的密码
# for i in range(0, 3):
#     usr_name = input("用户名：")
#     usr_passwd = input("密码：")
#     if usr_name == name and usr_passwd == passwd:
#         print("登陆成功")
#
#         break
#     elif name != usr_name or passwd != usr_passwd:
#         if i < 2:
#             print("用户名密码错误，请重新输入！")
#         else:
#             print("对不起！机会只有三次，你没珍惜好，可惜你的账号，账号密码已被锁定")
#             time.sleep(10)


# 7、编程实现下列图形的打印（三角形）

# lines = int(input("输入要打印的行数:"))
# for i in range(lines):
#     for j in range(0, lines - i):
#         print(end=" ")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()





# 8、使用while循环实现NxN乘法表的打印

#
# N= int(input("请输入N的值："))
#
# i = 1
# while i<= N:
#         j = 1
#         while j <= i:
#             print("%d*%d=%d" % (j, i, j * i), end="\t")
#             j += 1
#         print()
#         i += 1




# 9、编程实现99乘法表的倒叙打印


# for i in range(-9,0):
#     for j in range(1,10):
#
#         if j==i*(-1):
#
#             print(j,"*",i*(-1),"=",i*j*(-1)," ")
#
#             break
#
#         elif i*j*(-1)>9:
#                 print(j,"*",i*(-1),"=",i*j*(-1)," ",end="")
#
#
#         else:
#
#             print(j,"*",i*(-1),"=",i*j*(-1)," ",end="")



# 10、一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。


# high,up,down=map(int,input().split(' '))
# sum=0
# n=0
# while sum<high:
#     n+=1
#     sum+=up
#     if sum<high:
#         sum-=down
#     else:
#         print(n)
#








# 11、继续完成上午的猜数字游戏的需求功能。
# 1.	添加计数打印功能
# 2.	添加次数金币功能和锁定系统功能。







# 12、用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）


# def factorial(n):
#     if n == 1: return 1
#     return n*factorial(n-1)
# for i in range(1, 21):
#     print(i, '!=', factorial(i))


