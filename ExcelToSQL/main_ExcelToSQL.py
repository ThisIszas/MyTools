# coding:utf-8
import MySQLdb
import xlrd
"""
MySQLdb:1.2.5版本
xlrd:1.0.0版本
使用前请先在下面配置好各变量.
excel_table_name:表示要导入的excel文件
excel_sheet_name:表示要导入到excel文件当前表格的表名.例如:一个test1.xls文件里有test2这个数据表,此处就填写'test2'.
SQL_table_name:表示要被导入数据的数据库表名.例如:被导入数据的table名为:test3,此处就填写test3.
"""


def main_pro(excel_table_name, excel_sheet_name, SQL_table_name, tempDB):

    cursor = tempDB.cursor()  # 获取当前数据库的游标
    data = xlrd.open_workbook(excel_table_name)  # 获取xls文件里的内容
    table = data.sheet_by_name(excel_sheet_name)  # 获取当前表格数据
    nrows = table.nrows  # 当前表格的行数
    ncols = table.ncols  # 当前表格上的列数

    for rows in range(nrows):
        temp_list = []  # temp_list用于暂存一行的数据
        temp_value_string = "("  # temp_value_string用于构造value的值
        for cols in range(ncols):
            values = table.cell(rows, cols).value  # 读出第rows行第cols列的数据
            temp_list.append(values)

        for temp_i in range(ncols):
            if temp_i == ncols-1:
                temp_value_string = temp_value_string + '\'' + temp_list[temp_i] + '\''
            else:
                temp_value_string = temp_value_string + '\'' + temp_list[temp_i] + '\'' + ','
        temp_value_string += ')'
        # print temp_value_string # 不理解可在此处打印temp_value_string查看内容

        sql_sta = u"INSERT INTO %s VALUES %s" % (SQL_table_name, temp_value_string)
        # print sql_sta  # 此处可打印数据库insert语句
        cursor.execute(sql_sta)  # 将insert语句交给游标执行
        tempDB.commit()

if __name__ == '__main__':
    excel_table_name = u'excelFileName.xls'
    excel_sheet_name = u'excelTableName'
    SQL_table_name = u'SQL_TableName'
    tempDB = MySQLdb.Connection('localhost', 'SQL_Username', 'SQL_Password', 'SQL_DatebaseName', charset='utf8')
    # tempDB变量:                服务器地       数据库登录名      数据库密码        要导入数据的数据库名
    main_pro(excel_table_name, excel_sheet_name, SQL_table_name, tempDB)