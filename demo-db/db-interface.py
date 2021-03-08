import sys, os, numpy as np, re, hmac, time
from numpy import ndarray
import db_watermark_alg as alg

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
    fs = open(sqlfile, encoding='utf-8', mode='r')

    result_matrix = {}
    attr_matrix = {}
    
    data_list = []   #读出数据的结果集合
    col_list = []    #表需要修改的属性字段索引值
    table_name = ''  #表名
    attr_list = []   #表需要修改的属性字段名

    for item in table_names:
        table_name = item
        attr_list = table_names[item]
        break

    read_target_table = False
    primary_key_index = 0

    #改为按行读取，尝试读取大文件
    while True:
        # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
        line = fs.readline()

        #按行读取
        if line:
            if 'CREATE TABLE' in line and table_name in line:
                read_target_table = True
                index_attr = 0

                while True:
                    line_sub = fs.readline()
                    #读到 ; 属性结束退出
                    if ';\n' in line_sub:
                        break

                    for index in range(len(attr_list)):
                        if attr_list[index] in line_sub:
                            col_list.append(index_attr)
                            attr_list.pop(index)
                            break
                    
                    index_attr += 1

            elif 'INSERT INTO' in line and table_name in line and read_target_table == True:         
                #从文件中将对应col数据读取入MATRIX
                #2种SQL导出文件，有可能 insert into 是分行，有可能都在1行, 通过RE表达式 区分出 ()内的数据
                #result = re.findall('(?<=\().*?(?=\))', line, flags=0)
                result = re.findall('(?<=\().*?(?=\);)', line, flags=0)
                #print(result)
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
                                break
            
            else:
                #后续退出条件，如果继续往下读表，出现了其他的CREATE TABLE  则退出读文件
                if read_target_table == True and ('CREATE TABLE' in line and table_name not in line):
                    break

        else:
            break
    
    #LIST转numpy
    np_array = np.asarray(data_list, dtype=float)
    result_matrix[table_name] = np_array
    attr_matrix[table_name] = col_list

    #释放文件句柄
    fs.close()

    return result_matrix, attr_matrix

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

#加入水印
def waternark_embed_alg1(input_matrix : {}, secrect_key:str, watermark:str, constrain_set:[], type:int):
    print('--------------------------------EMBED-----------------------------------------------')
    print('------seckey = [%s] watermark = [%s]' % (secrect_key, watermark))
    output_matrix = {}

    #实际上只目前只会执行一次FOR循环
    for item in input_matrix:
        #step0 计算data set分段数量
        binarr = alg.str_2_bin(watermark)
        watermark_len = len(binarr)
        dataset_origin:ndarray = input_matrix[item]

        partition_nums = alg.count_partitions(dataset_origin.shape[0], watermark_len)

        if partition_nums <= 0:
            print('!!!!!! [%s] dataset size [%d] is too small for watermarklen [%d]  min [%d], short your watermark or insert more data 2 handle' % (item, dataset_origin.shape[0], watermark_len, watermark_len * alg.MIN_DATA_SET_PARTITION * alg.MIN_BIT_RUDENT))
            continue
        else:
            print('!!!!! [%s] dataset has [%d] partitions' % (item, partition_nums))

        #step1 将数据集分组
        sub_dataset = partition_data_set(partition_nums, secrect_key, dataset_origin)

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
            if sub_arr.shape[0] > alg.MIN_DATA_SET_PARTITION * 0.75:
                slot = int(index % watermark_len)
                #输入第二列数据
                addtion_vector, x_min_max = alg.count_insert_vector(int(binarr[slot]), type, sub_arr[:,1], constrain_set)
                #最终的回写数据
                sub_arr[:,1] = sub_arr[:,1] + addtion_vector

                if binarr[slot] == '0':
                    #print('---------- insert slot [%d] 0 val = [%f] mean = [%f]  add_mean = [%f]' % (slot, x_min_max, np.mean(sub_arr[:,1]), np.mean(addtion_vector)))
                    min_list.append(x_min_max)
                else:
                    #print('---------- insert slot [%d] 1 val = [%f] mean = [%f]  add_mean = [%f]' % (slot, x_min_max, np.mean(sub_arr[:,1]), np.mean(addtion_vector)))
                    max_list.append(x_min_max)

                result_vals = np.append(result_vals, sub_arr)

        #step 2.1 计算阈值T*
        min_x, min_y = alg.convert_data_into_xy(np.asarray(min_list))
        gauss_min_mean, gauss_min_mean_sqrt = alg.count_gauss_distribute_params(min_x, min_y, np.mean(min_x), np.var(min_x))

        max_x, max_y = alg.convert_data_into_xy(np.asarray(max_list))
        gauss_max_mean, gauss_max_mean_sqrt = alg.count_gauss_distribute_params(max_x, max_y, np.mean(max_x), np.var(max_x))

        threash_hold = alg.count_decode_thresh_hold(np.asarray(min_list), np.asarray(max_list), gauss_min_mean_sqrt, gauss_max_mean_sqrt, gauss_min_mean, gauss_max_mean)

        outlist = []
        outlist.append(threash_hold)
        outlist.append(result_vals)
        outlist.append(partition_nums)

        output_matrix[item] = outlist
        

    return output_matrix


#将修改完结果写入目标文件
def write_result_2_file(srcfile:str, outfile:str, output_matrix : {}, col_matrix : {}):
    fd = open(outfile, encoding='utf-8', mode='w+')
    fs = open(srcfile, encoding='utf-8', mode='r')
    
    #暂时只处理第一个
    key = ''
    for item in output_matrix:
        key = item
        break
    
    fixlist:ndarray = output_matrix[key][1]
    fixlist = fixlist.reshape(int(fixlist.shape[0] / 2), 2)

    col_list = col_matrix[key]

    while True:
        strline = fs.readline()

        if strline:
            if 'INSERT INTO'  in strline and key in strline:
                find_val = False
                #修改数据写入
                for item in fixlist:
                    pkstr = '\'' + str(int(item[0])) + '\''
                    if pkstr in strline:
                        str_list = strline.split(', ')

                        strline_new = ''
                        for index in range(len(str_list)):
                            if index in col_list and index != 0:
                                strline_new += '\'' + str(item[1]) + '\'' + ', '
                            else:
                                if index < len(str_list) - 1:
                                    strline_new += str_list[index] + ', '
                                else:
                                    strline_new += str_list[index]

                        fd.write(strline_new)

                        find_val = True
                        break
                
                #如果没有修改数据则正是写入
                if find_val == False:
                    fd.write(strline)
            else:
                fd.write(strline)
        else:
            break

    fd.close()
    fs.close()

def vote_for_bits(bin_list:[]):
    vote_list = ''
    for item in bin_list:
        num1 = 0
        num0 = 0

        for item1 in item:
            if item1 == 1:
                num1 += 1
            else:
                num0 += 1
        
        if num1 > num0:
            vote_list += '1'
        else:
            vote_list += '0'
    
    return vote_list

#抽取水印,返回所有可能的字母
def waternark_extract_alg1(input_matrix : {}, partition_nums:int, secret_key:str, thresh_hold:float, watermark_len:int):
    print('--------------------------------EXTRACT-----------------------------------------------')
    print('---------- partitions = [%d] seckey = [%s] thresh = [%f] watermarklen = [%d]' % (partition_nums, secret_key, thresh_hold, watermark_len))
    bin_list = []

    for index in range(watermark_len):
        temp = []
        bin_list.append(temp)

    for item in input_matrix:
        dataset_origin:ndarray = input_matrix[item]

        #----------------------------------------------------------------------------------------------------
        #step1 将数据集分组
        sub_dataset = partition_data_set(partition_nums, secret_key, dataset_origin)

        #----------------------------------------------------------------------------------------------------
        #step2 分组解析BIT位数据
        for index in range(len(sub_dataset)):
            #sub_arr  [[a, b], [c, d], [e, f]]
            sub_arr:ndarray = sub_dataset[index]
                
            #对于超过最小值下限的数据集才嵌入水印，控制误差  hash不均匀，加入个系数
            if sub_arr.shape[0] > alg.MIN_DATA_SET_PARTITION * 0.75:
                slot = int(index % watermark_len)

                bit_con = alg.decode_bit_from_partition(thresh_hold, sub_arr[:,1])

                slot_sub = bin_list[slot]
                slot_sub.append(bit_con)
                bin_list[slot] = slot_sub

                #print('+++++++++++ slot [%d] index [%d] mean [%f] thresh [%f]'  % (slot, index, np.mean(sub_arr[:,1]), thresh_hold))
        #----------------------------------------------------------------------------------------------------
        #step3 根据BIN LIST解析结果投票
        
        print(bin_list)

        vote_list = vote_for_bits(bin_list)

        return alg.bin_2_str(vote_list)



if __name__ == "__main__":
    
    #入参应该包含需要添加水印的表+可插入误差的COL名(可多选)
    table_names = {}
    attrs = []
    #暂时只支持对1个ATTR加水印
    attrs.append('id')  #列表第一个是主键
    attrs.append('emotion')
    table_names['monitor_data_history'] = attrs

    #误差范围
    constrain_set = [[0, 0.3], [0.3, 0.7], [0.7, 1]]
    #constrain_set = [-0.1, 0.1]

    INFILE = '\\yuqing_lite.sql'
    OUTFILE = '\\yuqing_lite_out.sql'
    secret_key = 'sxcqq1233aaa'
    water_mark = 'a'

    
    #解析文件，读取需要修改的数据   +  表的ATTR索引
    result_matrix, col_matrix = read_sqlfile_to_list(INFILE, table_names)

    #输出 为字典，每个字典TUNPLE下是LIST 0 = 反写的NUMPY数组  1= 阈值
    output_matrix = waternark_embed_alg1(result_matrix, secret_key, water_mark, constrain_set, alg.DISTORTION_TYPE)

    print('---------------- thresh [%f] nums [%d]' % (output_matrix['monitor_data_history'][0], output_matrix['monitor_data_history'][2]))

    write_result_2_file(INFILE, OUTFILE, output_matrix, col_matrix)



    #解码水印步骤

    result_matrix, col_matrix = read_sqlfile_to_list(OUTFILE, table_names)

    #watermark_list = waternark_extract_alg1(result_matrix, output_matrix['monitor_data_history'][2], secret_key, output_matrix['monitor_data_history'][0], len(alg.str_2_bin(water_mark)))
    
    watermark_list = waternark_extract_alg1(result_matrix, 21, secret_key, 0.357046, 7)

    print(watermark_list)
    
        







