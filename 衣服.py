'''
统计:全年的销售额
    每种衣服 的销售额
    每种衣服的销售总量
    每种衣服的销售额的占比
    每种衣服的销售量的占比

'''

import xlrd
# 打开工作簿
wb=xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)

# 整体存储数据库
store={}
'''

存储结构:
    风衣:{
        "sum_money":xx,#总销售额
        "sum_count":xx,#总销售量
        },
        "羽绒服":{
            "sum_money":xx,
            "sum_count":xxx,
        }

'''
#获取所有工作簿选项卡个数
nsheet=wb.nsheets
# 现在要获取所有工作簿的表格数据
for i in range (nsheet):#每个选项卡
    #获取第n个选项卡
    st=wb.sheet_by_index(i)
    #获取有多少行
    nrow=st.nrows
    for j in range(1,nrow):
        cell= st.row_values(j)
        if cell [1] in store:
            store[cell[1]]={
                "sum_money":round(store[cell[1]]["sum_money"]+cell[2]*cell[4],2),
                "sum_count":int(store[cell[1]]["sum_count"]+cell[4])
            }
        else:
            store[cell[1]]={
                "sum_money":round(cell[2]*cell[4],2),
                "sum_count":int(cell[4])
            }

# 全年统计总和
all_sum= sum(store[item]["sum_money"] for item in store)
# 全部总销售额
all_count=sum(store[item]["sum_count"]for item in store)
# 全部总销售量
print("全年的统计总销售额:￥",round(all_sum,2))
print("全年的统计总销售量:",round(all_count,2),"件!")
for name in store:
    print("--------------------------------------------")
    print(name,"的销售额占比为:",round(store[name]["sum_money"]/all_sum*100,2),"%")
    print(name,"的销售量占比为:",round(store[name]["sum_count"]/all_sum*100,2),"%")








