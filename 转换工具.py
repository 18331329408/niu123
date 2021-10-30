import pymysql
import os
import xlrd
import xlwt

class DB_Excel_Utils:
    def __init__(self):
        self.con = pymysql.connect(host="localhost",user="root",password="root",database="bank")
        self.cursor = self.con.cursor()

    #  数据库转换成excel表
    def DB_to_Excel(self,table="",filename=""):
        if filename.endswith(".xlsx") or filename.endswith(".xls"): # 判断文件是否是以xlsx或者xls结尾
            self.wb = xlwt.Workbook()
            self.st = self.wb.add_sheet(table)
        # 获取所有字段名
        sql = '''select * from %s''' % (table)
        self.cursor.execute(sql, [])
        # 将所有表头提取出来
        names = []
        for cu in self.cursor.description:
            names.append(cu[0])

        # 将所有数据提取出来
        data = self.cursor.fetchall()

        # 写入excel表格
        # 1.先写表头
        index = 0
        for j,value in enumerate(names):
            self.st.write(index,j,value)

        # 2.写数据
        for i,value in enumerate(data):
            index = index + 1
            for v_k,v_v in enumerate(value):
                self.st.write(index,v_k,v_v)

        # 3.保存数据
        self.wb.save(filename)

    # 公共的拼接sql的方法
    def concatSql(self,sql1,names):
        # 将表头拼接到sql1语句里 : 形成 values(%s,%s,%s.....)
        for i in range(len(names)):
            if i == len(names) - 1:
                sql1 = sql1 + "%s)"
                break
            else:
                sql1 = sql1 + "%s, "
        return sql1

    # excel表转换成数据库
    def Excel_to_DB(self,filename="",sheet=""):
        wb=xlrd.open_workbook(filename=filename,encoding_override=True)
        sql1 = "insert into user1 values("
        # 默认excel表里的第一行就是数据库表的表头
        index = 0
        if sheet.isdigit(): # 判断是否是通过角标来获取选项卡的
            sheet = int(sheet) # 将“0” 转换成 0
            st = wb.sheet_by_index(sheet) # 通过角标获取该选项卡
            # 将第一行当成表头，放到列表["用户名","密码","年龄","地址"]
            names = st.row_values(0)
            sql1 = self.concatSql(sql1,names)
        else:
            st = wb.sheet_by_name(sheet)
            names = st.row_values(0)
            sql1 = self.concatSql(sql1, names)

        # 从第二行开始，将所有数据放入param，并批量执行
        param = []
        for i in range(1,st.nrows):
            param.append(st.row_values(i))

        # 批量执行sql语句
        self.cursor.executemany(sql1,param)
        self.con.commit()
        self.cursor.close()
        self.con.close()


utils = DB_Excel_Utils()
# utils.Excel_to_DB(filename="data.xlsx",sheet="0")

utils.DB_to_Excel(filename="用户数据.xls",table="people")
