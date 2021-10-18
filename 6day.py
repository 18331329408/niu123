import random
print("***************************")
print("*    中国银行账户管理系统    *")
print("***************************")
print("*          1、开户         *")
print("*          2、存钱         *")
print("*          3、取钱         *")
print("*          4、转账         *")
print("*          5、查询         *")
print("*          6、再见         *")
print("***************************")

#开户逻辑
bank={}#空的银行账户数据库
#'Frank': {'account': 10936377, 'password': '123', 'country': '中国', 'province': '山东', 'street': '蓝翔', 'door': '001'},
bank_name="中国银行M78分行"
#传入参数添加到字典里面
def bank_add(account,username,password,country,province,street,door):
    if username in bank:#说明用户已存在
        return 2
    elif len(bank)>=100:
        return 3
    else:
        bank[username]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
#     地址
def useradd():
    account=random.randint(10000000,99999999)
    username=input("请输入您的用户名")
    password=input("请输入您的用户密码")
    print("下面请输入你的详细地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    add=bank_add(account,username,password,country,province,street,door)
    if add == 3:
        print("数据库已满请到其他银行开户")
    elif add ==2:
        print("请输入其他用户名")
    elif add== 1:
        print("开户成功,下面是你的详细信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s 
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
# 存钱
def inmoney():

        username=input("请输入用户名")
        money=int(input("请输入存款金额"))
        if username in bank:
            bank[username]["money"]= bank[username]["money"]+money
            print("存入金额：",bank[username]["money"])
        else:
            print("没有此用户")

# 取钱

def outmoney():
    username = input("请输入用户名")
    if username in bank:

        password= input("请输入密码")
        if password == bank[username]["password"]:
            money= int (input("请输入取款金额"))
            if bank[username]["money"]>money:
                bank[username]["money"]=bank[username]["money"]-money

                print("取款成功")
                return 0
            else:
                print("余额不足")
                return 3
        else:
            print("密码输入错误")
            return 2
    else:
        print("用户名输入错误")
        return 1

# 转账

def bank_zhuangzhang():
    in_username = input("请输入要转入的用户名：")
    out_username = input("请输入要转出的用户名：")
    if in_username and out_username in bank:
        out_password = input("请输入要转出账号的密码：")
        if out_password == bank[out_username]["password"]:
            out_money = int(input("请输入要转出的金额："))
            if out_money <= bank[out_username]["money"]:
                bank[out_username]["money"] = bank[out_username]["money"] - out_money
                bank[in_username]["money"] = bank[in_username]["money"] + out_money
                print("转账成功")
                return 0
            else:
                print("余额不足")
                return 3
        else:
            print("密码输入错误")
            return 2
    else:
        print("用户名输入错误")
        return 1



# 查询
def bank_Find():
    Find_username = input("请输入要查询的用户名：")
    if Find_username in bank:
        Find_password = input("请输入要查询账号的密码：")
        if Find_password == bank[Find_username]["password"]:
            print(bank[Find_username])
        else:
            print("密码错误")
    else:
        print("用户名错误")






# 操作
while 1:
    index=int(input("请输入您的操作"))
    if index ==1:
        print("1、开户")
        useradd()
        print(bank)
    elif index ==2:
        print("2、存钱")
        inmoney()
    elif index ==3:
        print("3、取钱")
        outmoney()
    elif index ==4:
        print("4、转账")
        bank_zhuangzhang()
    elif index ==5:
        print("5、查询")
    elif index ==6:
        print("6、再见")


