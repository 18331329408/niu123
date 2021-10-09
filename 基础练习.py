
#1、练习1：华氏温度转换为摄氏温度。
#提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

# F=float(input("请输入华氏度："))
# C=(F-32)/1.8
# print("输出的摄氏度是：",C)



#2、练习2：输入圆的半径计算计算周长和面积。

# num=float(input("请输入圆的半径"))
# circleline=round((2*3.14*num),2)
# circle=3.14*num*num
# print("圆的周长是：",circleline)
# print("圆的面积是:",circle)



#3、练习3：输入年份判断是不是闰年。.

# year=int(input("请输入年份"))
# if (year%4)==0 or (year % 400) == 0:
#     print(year,"是闰年！")
# else:
#     print("今年不是闰年")




#4、练习4：英制单位英寸与公制单位厘米互换。
#提示：需要键盘输入长度，需要键盘输入单位


# long=float(input("请输入长度"))
# danwei=str(input("请输入单位"))
# cm=long*0.39
# incun=long*2.54
# if danwei=="厘米" or danwei=="cm":
#
#     print("转换为英寸是：",cm)
# elif danwei=="英寸" or danwei=="incun":
#         print("转换为厘米是：",incun)








#5、练习5：百分制成绩转换为等级制成绩。

# num=float(input("请输入分数："))
# if(num>100):
#     print("从哪来的这么多分")
# elif num>=90and num<=100:
#     print("A")
# elif num>=80 and num <90:
#         print("B")
# elif num>=70and num<80:
#             print("C")
# elif(num >=60)and (num<70):
#                 print("D")
# else :
#     print("E")


# 6、输入三条边长，如果能构成三角形就计算周长和面积

# a=float(input("请输入变长a:"))
# b=float(input("请输入变长b:"))
# c=float(input("请输入变长c:"))
# if a+b>c and a+c>b and b+c>a :
#     print("周长是：",a+b+c)
#     p = (a + b + c) / 2
#     area = round(((p * (p - a) * (p - b) * (p - c)) ** 0.5),2)
#     print("面积： " , (area))
# else:
#     print("不能构成三角形")

