import re, numpy as np, hmac, random, math, cmath
from numpy import ndarray
from math import pow
from scipy.optimize import curve_fit
import pylab as plt

MAX_OPTIOM = 1  #求解全局最优的最大解
MIN_OPTIOM = 0

DISTORTION_BOUND = 1   #误差嵌入类型  1   给出上下界
DISTORTION_TYPE = 2    #误差嵌入类型  2   给出分段的上下界

REF_RATION = 0.5   #0-1   ref的系数  tail系数  REF越大  HIDING-FUNCTION的值越小，成反比

PATTERN_SEARCH_SHORT_RATION = 0.5   #在单论搜索最大/最小值失败后，步长的缩短系数
PATTERN_SEARCH_LARGE_RATION = 2   #在单次的轴搜索成功后，除了扩大模式范围，同时也增加搜索步长倍数
PATTERN_SEARCH_INIT_ADD_SPEED = 3  # >= 1
PATTERN_SEARCH_PRECISION = 0.00000001  #模式搜索最小的精度，|a-b|差值小于该值认为a == b

#兼顾效率和区分度，最佳的数据子集大小为200
MIN_DATA_SET_PARTITION = 200

MIN_BIT_RUDENT = 3


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

def count_hiding_function_val(combine_vector:ndarray):
      '''
      ref_val = np.mean(combine_vector) + REF_RATION * math.sqrt(np.var(combine_vector))

      sum = 0

      for index in range(combine_vector.shape[0]):
            if combine_vector[index] >= ref_val:
                  sum += 1 

      return sum / combine_vector.shape[0]
      
      '''

      #以下为sigmoid光滑的实现，为了增强模式搜索的实现
      ref_val = np.mean(combine_vector) + REF_RATION * math.sqrt(np.var(combine_vector))

      sum = 0.0

      param_alpha = 8.0

      for index in range(combine_vector.shape[0]):
            sum += 1 - 1 / (1 + pow(math.e, param_alpha * (combine_vector[index] - ref_val)))

      return sum / combine_vector.shape[0]
      

def search_one_round(data_vector:ndarray, addtion_vector:ndarray, constrain_set:ndarray, direction_type:int, forward_len:float):
      #此处用的应该是sqrt均方差，而不是var方差
      tao_val = count_hiding_function_val(data_vector + addtion_vector)
      for index in range(data_vector.shape[0]):
            step_moved = False

            step_temp = (constrain_set[index][1] - constrain_set[index][0]) * forward_len

            if data_vector[index] + addtion_vector[index] + step_temp <= constrain_set[index][1] and \
                  data_vector[index] + addtion_vector[index] + step_temp >= constrain_set[index][0]: #没有超过约束

                  origin_add = addtion_vector[index]
                  addtion_vector[index] = addtion_vector[index] + step_temp

                  tao_temp_val = count_hiding_function_val(data_vector + addtion_vector)

                  if direction_type == MAX_OPTIOM:
                        if tao_temp_val - tao_val > PATTERN_SEARCH_PRECISION:
                              tao_val = tao_temp_val
                              step_moved = True
                        else:
                              #恢复数据
                              addtion_vector[index] = origin_add
                  else:
                        if  tao_val - tao_temp_val > PATTERN_SEARCH_PRECISION:
                              tao_val = tao_temp_val
                              step_moved = True
                        else:
                              #恢复数据
                              addtion_vector[index] = origin_add

            #如果正向移动没有得到效果，则尝试反向移动一次
            if  step_moved == False and data_vector[index] + addtion_vector[index] - step_temp >= constrain_set[index][0] and \
                  data_vector[index] + addtion_vector[index] - step_temp <= constrain_set[index][1]: #没有超过约束

                  origin_add = addtion_vector[index]
                  addtion_vector[index] = addtion_vector[index] - step_temp

                  tao_temp_val = count_hiding_function_val(data_vector + addtion_vector)

                  if direction_type == MAX_OPTIOM:
                        if tao_temp_val - tao_val > PATTERN_SEARCH_PRECISION:
                              tao_val = tao_temp_val
                              step_moved = True
                        else:
                              addtion_vector[index] = origin_add
                  else:
                        if tao_val - tao_temp_val > PATTERN_SEARCH_PRECISION:
                              tao_val = tao_temp_val
                              step_moved = True
                        else:
                              addtion_vector[index] = origin_add
      
      #返回一轮最优结果后的函数值和向量
      return tao_val, addtion_vector


#模式搜索最优化
def pattern_search_optiom(optim_type:int, data_vector:ndarray, constrain_set:ndarray):

      addtion_vector_1 = []
      #给定随机初始值
      for index in range(data_vector.shape[0]):
            addtion_vector_1.append(0.0)

      addtion_vector = np.asarray(addtion_vector_1)
      
      init_tao_val = count_hiding_function_val(data_vector + addtion_vector)

      not_found_val = True

      step_ration = 1.0

      best_addtion_vector = addtion_vector

      back_to_init = True

      #终止条件  --沿最优方向 搜索一轮后，没有更优结果，且缩小步长再次搜索后没有更优结果
      while not_found_val:
            #缩短1次STEP
            #暂时不搜索了，提高运行速度，直接退出，得到当前的最优解
            
            if step_ration < 0.25:
                  not_found_val = False
                  break
            
            #change
            step_len = 0.05 * step_ration
            #进行轴搜索
            tao_temp_val, add_fix_vetctor = search_one_round(data_vector, addtion_vector, constrain_set, optim_type, step_len)

            if optim_type == MAX_OPTIOM:   #查找全局最大值
                  if tao_temp_val - init_tao_val > PATTERN_SEARCH_PRECISION:
                        #进行模式搜索，沿着N维向量的当前方向进行
                        init_tao_val = tao_temp_val
                        best_addtion_vector = add_fix_vetctor

                        back_to_init = True

                        addtion_vector = add_fix_vetctor + PATTERN_SEARCH_INIT_ADD_SPEED * (add_fix_vetctor - addtion_vector)

                        #扩大步长范围
                        step_ration = step_ration * PATTERN_SEARCH_LARGE_RATION
                  else:
                        '''
                        if back_to_init == False:
                              not_found_val = False
                              break
                        
                        back_to_init = True
                        '''

                        #退回出发点
                        if back_to_init:
                              addtion_vector = best_addtion_vector
                              back_to_init = False
                        else:
                              #缩短步长继续搜索
                              step_ration = step_ration * PATTERN_SEARCH_SHORT_RATION

            else:   #查找全局最小值
                  if init_tao_val - tao_temp_val > PATTERN_SEARCH_PRECISION:
                        #进行模式搜索
                        init_tao_val = tao_temp_val
                        best_addtion_vector = add_fix_vetctor

                        back_to_init = True

                        addtion_vector = add_fix_vetctor + PATTERN_SEARCH_INIT_ADD_SPEED * (add_fix_vetctor - addtion_vector)

                        #扩大步长范围
                        step_ration = step_ration * PATTERN_SEARCH_LARGE_RATION
                  else:
                        '''
                        if back_to_init == False:
                              not_found_val = False
                              break
                              
                        back_to_init = True
                        '''

                        #退回出发点
                        if back_to_init:
                              addtion_vector = best_addtion_vector
                              back_to_init = False
                        else:
                              #SHORT步长继续搜索
                              step_ration = step_ration * PATTERN_SEARCH_SHORT_RATION
      
      return best_addtion_vector, init_tao_val


def count_insert_vector(optim_type:int, distortion_type:int, data_vector:ndarray, constrain_set:[]):
      if distortion_type == DISTORTION_BOUND:
            constrain_set_new = []

            for index in range(data_vector.shape[0]):
                  temp = []
                  temp.append(data_vector[index] + data_vector[index] * constrain_set[0])
                  temp.append(data_vector[index] + data_vector[index] * constrain_set[1])
                  constrain_set_new.append(temp)

            delta_vetor, X_max_min = pattern_search_optiom(optim_type, data_vector, np.asarray(constrain_set_new))

            return delta_vetor, X_max_min

      elif distortion_type == DISTORTION_TYPE:
            constrain_set_new = []

            for index in range(data_vector.shape[0]):
                  temp = []
                  
                  for item in constrain_set:
                        if data_vector[index] < item[1] and data_vector[index] >= item[0]:
                              temp.append(item[0])
                              temp.append(item[1])
                              break
                  #如果都没有 说明到达了上界限，因为这里是包左不包右
                  if len(temp) <= 0:
                        temp.append(constrain_set[-1][0])
                        temp.append(constrain_set[-1][1])
                  constrain_set_new.append(temp)
            
            delta_vetor, X_max_min = pattern_search_optiom(optim_type, data_vector, np.asarray(constrain_set_new))

            return delta_vetor, X_max_min
      else:
            print('distortion type no support, do nothing')
            return None, None


#从计算出的MAX和MIN队列种计算解码阈值T*
def count_decode_thresh_hold(x_min:ndarray, x_max:ndarray, mean_sqr_err_0:float, mean_sqr_err_1:float, mean_0:float, mean_1:float):
      prob_1 = x_max.shape[0] / (x_max.shape[0] + x_min.shape[0])
      prob_0 = 1 - prob_1

      result = 0.0

      a = (pow(mean_sqr_err_0, 2) - pow(mean_sqr_err_1, 2)) / (2 * pow(mean_sqr_err_0, 2) * pow(mean_sqr_err_1, 2))
      b = ((mean_0 * pow(mean_sqr_err_1, 2)) - (mean_1 * pow(mean_sqr_err_0, 2))) / (pow(mean_sqr_err_0, 2) * pow(mean_sqr_err_1, 2))
      c = math.log((prob_0 * mean_sqr_err_1 / prob_1 * mean_sqr_err_0)) +  ((pow(mean_1, 2) * pow(mean_sqr_err_0, 2)) - (pow(mean_0, 2) * pow(mean_sqr_err_1, 2))) / (2 * pow(mean_sqr_err_0, 2) * pow(mean_sqr_err_1, 2))
      
      x1 = None
      x2 = None
      discriminant = (b**2)-(4*a*c)

      if discriminant == 0:
            x1 = -(b/(2*a))
      else:
            if discriminant >0:
                  root = math.sqrt(discriminant)
            else:
                  root = cmath.sqrt(discriminant)
            x1 = (-b+root)/(2*a)
            x2 = (-b-root)/(2*a)
      
      if x1 > 0.0 and x1 < 1.0:
            result = x1
      else:
            result = x2

      #优化过程，暂时先增加处理，如果result因精度原因没有落在MIN MAX之间，则简单计算
      if result <= np.mean(x_min) or result >= np.mean(x_max):
            print('!!!!!!!! T* not corect [%f]!!!!!' % (result))
            result = np.mean(x_min) + (np.mean(x_max) - np.mean(x_min)) * 0.33 * (1 +  (prob_0 / (prob_0 + prob_1)))
            print('!!!!!!!! T* fix value  [%f]!!!!!' % (result))

      return result

def gaussian(x,*param):
    u = param[0]
    sig = param[1]

    return np.exp(-(x - u) ** 2 / (2 * sig ** 2))/ ((sig * math.sqrt(2 * math.pi)))

#计算一组统计数据的高斯分布参数
def count_gauss_distribute_params(x_vector:ndarray, y_vector:ndarray, init_mean:float, init_var:float):
      #正态分布的初始化的均值和方差数据
      p0=[]
      p0.append(init_mean) 
      p0.append(init_var) 

      popt, pcov = curve_fit(gaussian, x_vector, y_vector, p0)

      return popt[0], popt[1]

#将1维的数据，以小数点后2位为精度，分散到0-1为界的X-Y坐标系内，方便后续 正态分布的拟合计算
def convert_data_into_xy(data_vector:ndarray):
      x_list = []
      y_list = []

      fit_precision = 0.01
      fit_bits= 2 #位数,和精度一起修改

      precision_val = (int)(1/fit_precision)
      
      for index in range(precision_val):
            x_list.append(round(fit_precision * index, fit_bits))
            y_list.append(0)

      for item in data_vector:
            slot = int(round(item, fit_bits) * precision_val % precision_val)
            y_list[slot] = y_list[slot] + 1
      
      #计算离散数据的概率密度


      return np.asarray(x_list), np.asarray(y_list)


#解码，从给定的分组种获取水印的BIT位信息
def decode_bit_from_partition(thresh_hold:float, data_vector:ndarray):
      tao_val = count_hiding_function_val(data_vector)

      result = 0

      if tao_val >= thresh_hold:
            result = 1

      return result

#根据数据集长度和水印中的01数量计算适合的分组数量
def count_partitions(data_set_len:int, watermark_len:int):
      if watermark_len * MIN_BIT_RUDENT * MIN_DATA_SET_PARTITION > data_set_len:
            return 0

      addtion_num = 2

      while True:
            if watermark_len * ( MIN_BIT_RUDENT + addtion_num)* MIN_DATA_SET_PARTITION < data_set_len:
                   addtion_num += 2
            else:
                  return  watermark_len * MIN_BIT_RUDENT + addtion_num - 2


if __name__ == "__main__":

      #约束集暂时按最大最小 这里按百分比的绝对值给出
      #constrain_set = [-0.05, 0.05]

      constrain_set = [[0, 5], [5, 11], [11, 15], [15, 20]]


      max_list = []
      min_list = []

      max_result_list = []
      min_result_list = []

      for index_1 in range(50):
            #暂时使用同源数据
            data_vector_min = []
            for index in range(MIN_DATA_SET_PARTITION):
                  data_vector_min.append(random.uniform(0, 20))

            data_vector_max = []
            for index in range(MIN_DATA_SET_PARTITION):
                  data_vector_max.append(random.uniform(0, 20))


            delta_vetor_min, Xmin = count_insert_vector(0, DISTORTION_TYPE, np.asarray(data_vector_min) , constrain_set)
            min_list.append(Xmin)
            #保存计算后的数据，用于验证
            min_result_list.append(np.asarray(data_vector_min) + delta_vetor_min)

            delta_vetor_max, Xmax = count_insert_vector(1, DISTORTION_TYPE, np.asarray(data_vector_max) , constrain_set)
            max_list.append(Xmax)

            #保存计算后的数据，用于验证
            max_result_list.append(np.asarray(data_vector_max) + delta_vetor_max)

            print('--------------- sample [%d] min = [%f] max = [%f] ' % (index_1, Xmin, Xmax))


      min_x, min_y = convert_data_into_xy(np.asarray(min_list))
      gauss_min_mean, gauss_min_mean_sqrt = count_gauss_distribute_params(min_x, min_y, np.mean(min_x), np.var(min_x))

      max_x, max_y = convert_data_into_xy(np.asarray(max_list))
      gauss_max_mean, gauss_max_mean_sqrt = count_gauss_distribute_params(max_x, max_y, np.mean(max_x), np.var(max_x))

      print('---------- gaussian min  mean[%f] var[%f]  || max mean[%f] var[%f] ' % (gauss_min_mean, gauss_min_mean_sqrt, gauss_max_mean, gauss_max_mean_sqrt))

      #绘制图像
      '''
      plt.plot(min_x,min_y,'b+:',label='bit_0')
      plt.plot(min_x,max_y,'c+:',label='bit_1')
      p_min = [gauss_min_mean, gauss_min_mean_sqrt]
      p_max = [gauss_max_mean, gauss_max_mean_sqrt]
      plt.plot(min_x,gaussian(min_x,*p_min),'ro:',label='fit_bit_0')
      plt.plot(min_x,gaussian(min_x,*p_max),'o:',label='fit_bit_1')
      plt.legend()
      plt.show()
      '''
      #绘制结束

      result = count_decode_thresh_hold(np.asarray(min_list), np.asarray(max_list), gauss_min_mean_sqrt, gauss_max_mean_sqrt, gauss_min_mean, gauss_max_mean)


      print('------------ thresh = [%f] min mean = [%f]  max mean = [%f]' % (result, np.mean(min_list), np.mean(max_list)))

      num0 = 0
      for index in range(len(min_result_list)):
            bit_con = decode_bit_from_partition(result, min_result_list[index])
            if bit_con == 0:
                  num0 += 1

      print('---------------------------- bit 0 results [%d] in [%d]' % (num0, len(min_result_list)))

      num1 = 0
      for index in range(len(max_result_list)):
            bit_con = decode_bit_from_partition(result, max_result_list[index])
            if bit_con == 1:
                  num1 += 1
      print('---------------------------- bit 1 results [%d] in [%d]' % (num1, len(max_result_list)))
