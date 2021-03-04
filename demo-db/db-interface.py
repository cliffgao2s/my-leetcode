import sys, os, numpy as np, re, hmac
from numpy import ndarray
import db_watermark_alg as alg

#将STR转换为二进制
def str_2_bin(str_in):
    return ''.join([bin(ord(c)).replace('0b', '') for c in str_in])

#返回所有可能的字符组合
def bin_2_str(bin_in):
      result_list = []

      if bin_in[0] == '0':
            return result_list

      if len(bin_in) < 6:
            return result_list

      if len(bin_in) == 6:
            return chr(int(bin_in, 2))

      if len(bin_in) == 7:
            return chr(int(bin_in, 2))

      if bin_in[6] != '0':
            #先按6BIT位切分
            subArr1 = bin_in[0:6]
            subArr2 = bin_2_str(bin_in[6:])

            str1 = chr(int(subArr1, 2))
            if len(subArr2) > 0:
                  for item in subArr2:
                        result_list.append(str1 + item)

      if bin_in[7] != '0':
            #再尝试7BIT切分
            subArr1 = bin_in[0:7]
            subArr2 = bin_2_str(bin_in[7:])

            str1 = chr(int(subArr1, 2))
            if len(subArr2) > 0:
                  for item in subArr2:
                        result_list.append(str1 + item)


      return result_list

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
        sql_list = f.read().split(';\n')[:-1]     #以 ; + 换行符 作为切割依据
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
                    attr_name_list = table_names[table_name]
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
                    #2种SQL导出文件，有可能 insert into 是分行，有可能都在1行, 通过RE表达式 区分出 ()内的数据
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

#切割数据集，根据secret-key
def partition_data_set(partition_nums:int, secret_key:str, origin_data_set:ndarray):
    sub_sets = []

    for index in range(partition_nums):
        temp_list = []
        sub_sets.append(temp_list)

    for index in range(origin_data_set.shape[0]):
        h1 = hmac.new(str(int(origin_data_set[index][0])).encode('utf-8'), secret_key.encode('utf-8'), digestmod='MD5').hexdigest()
        h2 = hmac.new(secret_key.encode('utf-8'), h1.encode('utf-8'), digestmod='MD5').hexdigest()

        #计算出数据子集的SLOT，并修改插入
        slot = int(h2, 16) % partition_nums
        sub_list = sub_sets[slot]
        sub_list.append(origin_data_set[index])
        sub_sets[slot] = sub_list

    result_list = []
    for item in sub_sets:
        result_list.append(np.asarray(item))

    return np.asarray(result_list)

#param3 允许误差  FLOAT，比如 0.03 表示 可以在单个值嵌入 3%以内的误差
#param4 
def embed_watermark_bit(bit_val:int, sub_dataset:ndarray, permit_distortion:float, constrait_set: []):
    if int(bit_val) == 1:  #max option problem using pattern search
        pass
    elif int(bit_val) == 0: #min option
        pass
    else:  #do nothing
        pass
        
    return sub_dataset

#单个加水印数据集的最小数量
MIN_DATASET_SIZE = 150
#单个加水印的BIT位的最小冗余组数量
MIN_BIT_RUDENT = 3

def check_data_min_size(watermark:str, dataset_size:int):
    bin_list = str_2_bin(watermark)

    watermark_len = len(bin_list)

    if watermark_len * MIN_DATASET_SIZE * MIN_BIT_RUDENT < dataset_size:
        return False
    
    return True

#加入水印
def waternark_embed_alg1(input_matrix : {}, secrect_key:str, watermark:str):
    output_matrix = {}

    #实际上只目前只会执行一次FOR循环
    for item in input_matrix:
        #step0 计算data set分段数量
        binarr = str_2_bin(watermark)
        watermark_len = len(binarr)
        dataset_origin:ndarray = input_matrix[item]

        if check_data_min_size(watermark, dataset_origin.shape[0]) == False:
            print('!!!!!! [%s] dataset size is too small, short your watermark or insert more data 2 handle' % (item))
            continue
        
        partition_nums = watermark_len * MIN_BIT_RUDENT

        #step1 将数据集分组
        sub_dataset = partition_data_set(partition_nums, secrect_key, dataset_origin)

        #误差范围
        #constrain_set = [[0, 0.3], [0.3, 0.7], [0.7, 1]]

        constrain_set = [-0.1, 0.1]
        #记录最小和最大的值，用于计算T*阈值
        min_list = []
        max_list = []
        #初始化空的NUMPY数组  用于返回值
        result_vals = np.empty((0, 2))
        #step2 将水印按BIT位加入,水印只支持  数字 字母 + 常用字符 !等，从ASCII 33开始，保证至少为6位
        for index in range(len(sub_dataset)):
            #sub_arr  [[a, b], [c, d], [e, f]]
            sub_arr:ndarray = sub_dataset[index]
                
            #对于超过最小值下限的数据集才嵌入水印，控制误差
            if sub_arr.shape[0] > MIN_DATASET_SIZE:
                slot = int(index % watermark_len)
                #输入第二列数据
                addtion_vector, x_min_max = alg.count_insert_vector(binarr[slot], alg.DISTORTION_BOUND, sub_arr[:,1], constrain_set)
                #最终的回写数据
                sub_arr[:,1] = sub_arr[:,1] + addtion_vector

                if int(binarr[slot]) == 0:
                    min_list.append(x_min_max)
                else:
                    max_list.append(x_min_max)

                result_vals = np.append(result_vals, sub_arr)

        #step 2.1 计算阈值T*
        min_x, min_y = alg.convert_data_into_xy(np.asarray(min_list))
        gauss_min_mean, gauss_min_mean_sqrt = alg.count_gauss_distribute_params(min_x, min_y, np.mean(min_x), np.var(min_x))

        max_x, max_y = alg.convert_data_into_xy(np.asarray(max_list))
        gauss_max_mean, gauss_max_mean_sqrt = alg.count_gauss_distribute_params(max_x, max_y, np.mean(max_x), np.var(max_x))

        threash_hold = alg.count_decode_thresh_hold(np.asarray(min_list), np.asarray(max_list), gauss_min_mean_sqrt, gauss_max_mean_sqrt, gauss_min_mean, gauss_max_mean)

        print('------------- threash = [%f]' % (threash_hold))
        outlist = []
        outlist.append(result_vals)
        outlist.append(threash_hold)

        output_matrix[item] = outlist
        

    return output_matrix





#抽取水印,返回所有可能的字母
def waternark_extract_alg1(input_matrix : {}):
    pass


if __name__ == "__main__":
    #入参应该包含需要添加水印的表+可插入误差的COL名(可多选)
    table_names = {}
    attrs = []
    #暂时只支持对1个ATTR加水印
    attrs.append('id')  #列表第一个是主键
    attrs.append('emotion')
    table_names['monitor_data_history'] = attrs

    result_matrix = read_sqlfile_to_list('\\yuqing_lite.sql', table_names)

    #输出 为字典，每个字典TUNPLE下是LIST 0 = 反写的NUMPY数组  1= 阈值
    output_matrix = waternark_embed_alg1(result_matrix, 'sxcqq1233aaa', 'a')

    print(output_matrix['monitor_data_history'][0])




