import sys, os, numpy as np, re

def get_sub_attrs(str1):
    str1 = str1.replace('\n', '')
    result = re.search('`.*`', str1).group()
    result1 = result.split(' ')

    re_list = []


    for item in result1:
        if len(item) > 2 and item[0] == '`' and item[-1] == '`':
            re_list.append(item.strip('`'))

    return re_list


#对多个表加入水印,读取数据并返回需加水印数据的matrix
def read_sqlfile_to_list(sqlfile, table_names : {}):
    with open(sqlfile, encoding='utf-8', mode='r') as f:
        # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
        sql_list = f.read().split(';')[:-1]

        result_matrix = {}

        index = 0
        while index < len(sql_list):
            line = sql_list[index].replace('\n', '')
            if 'CREATE TABLE' in line:
                attr_list = get_sub_attrs(line)
                if table_names[attr_list[0]] != None:
                    #从attr_list 取出第一个参数，也就是表名，并REMOVE，这样attr_list剩下的就是表的字段名
                    table_name = attr_list[0]
                    attr_list.pop(0)
                    #获取要处理的表项colunm名称
                    attr_name_list : [] = table_names[table_name]
                    #预读取的数据LIST
                    data_list = []
                    col_list = []
                    #找到ATTR-NAME对应的索引,0 = pk
                    for item in attr_name_list:
                        for index_attr in range(len(attr_list)):
                            if item == attr_list[index_attr]:
                                col_list.append(index_attr)
                    
                    primary_key_index = 0
                    
                    #从文件中将对应col数据读取入MATRIX
                    #2种SQL导出文件，有可能 insert into 是分行，有可能都在1行
                    index += 1
                    while index < len(sql_list):
                        if 'INSERT INTO' in sql_list[index] and table_name in sql_list[index]:
                            result = re.findall('(?<=\().*?(?=\))', sql_list[index], flags=0)
                            for item in result:
                                temp = []
                                str_list = item.split(', ')   #split ,后面加个空格，防止内容里有空格

                                for index_str in range(len(str_list)):
                                    if index_str in col_list:
                                        str_temp = str_list[index_str]
                                        str_temp = str_temp.replace(' ', '')
                                        str_temp = str_temp.replace('\'', '')
                                        if str_temp != 'null':
                                            #主键保存为int类型
                                            if primary_key_index == index_str:
                                                temp.append(int(str_temp))
                                            else:
                                                temp.append(float(str_temp))
                                        else:
                                            break
                                        #只有长度正常的数据才能计入
                                        if len(temp) == len(col_list):
                                            data_list.append(temp)
                            index += 1
                        else:
                            break

                    #LIST转numpy
                    np_array = np.asarray(data_list, dtype=float)
                    result_matrix[table_name] = np_array
                else:
                    index += 1
            else:
                index += 1

        return result_matrix


def waternark_embed_alg1():
    pass


if __name__ == "__main__":
    #入参应该包含需要添加水印的表+可插入误差的COL名(可多选)
    table_names = {}
    attrs = []
    attrs.append('id')  #列表第一个是主键
    attrs.append('confidence')
    attrs.append('emotion')
    table_names['monitor_data_history'] = attrs

    result_matrix = read_sqlfile_to_list('\\yuqing_lite.sql', table_names)

    print(result_matrix)
