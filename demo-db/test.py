import re, numpy as np, hmac, random, math, cmath
from numpy import ndarray
from math import pow
from scipy.optimize import curve_fit
import pylab as plt

#=============================================================================
'''
str1 = "CREATE TABLE `directional_setting_website_cate` ( \
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT, \
  `name` varchar(45) NOT NULL DEFAULT '', \
  `crawl_rate` int(11) unsigned NOT NULL DEFAULT '4' COMMENT '抓取频率(小时)\\n默认4小时\\n', \
  `monitoring_items_num` smallint(5) unsigned NOT NULL DEFAULT '0' COMMENT '监控组数目', \
  `created_time` int(11) unsigned NOT NULL DEFAULT '0', \
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, \
  `status` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '状态：0：正常 1：删除', \
  `user_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '用户id', \
  PRIMARY KEY (`id`) \
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COMMENT='定向设置-监控网站组'" 


str1 = str1.replace('\n', '')


result = re.search('`.*`', str1).group()
result1 = result.split(' ')

re_list = []


for item in result1:
    if len(item) > 2 and item[0] == '`' and item[-1] == '`':
        re_list.append(item.strip('`'))


print(re_list)
'''
#=============================================================================
'''
str2 = "INSERT INTO `monitor_data_history` VALUES ('617511', '95', '135', '天津爆料,#天津爆料#【缜密筛查，锁定死亡事故肇事逃逸嫌疑人；迅速出击，驱车三十公里追逃人车俱查获】12月7日16时30分许，滨海新区大港油田红旗路物探公司西侧1公里发生一起交通事故，造成一名电动三轮车驾驶人死', 'IzxiPuWkqea0pTwvYj7niIbmlpkj44CQ57yc5a+G562b5p+l77yM6ZSB5a6aPGI+5q275Lqh5LqL5pWFPC9iPuiCh+S6i+mAg+mAuOWrjOeWkeS6uu+8m+i/hemAn+WHuuWHu++8jOmpsei9puS4ieWNgeWFrOmHjOi/vemAg+S6uui9puS/seafpeiOt+OAkTEy5pyIN+aXpTE25pe2MzDliIborrjvvIzmu6jmtbfmlrDljLrlpKfmuK/msrnnlLDnuqLml5fot6/nianmjqLlhazlj7jopb/kvqcx5YWs6YeM5Y+R55Sf5LiA6LW35Lqk6YCa5LqL5pWF77yM6YCg5oiQ5LiA5ZCN55S15Yqo5LiJ6L2u6L2m6am+6am25Lq65q275Lqh77yM5bCP5a6i6L2m6IKH5LqL5ZCO6YCD6YC444CC5o6l5oql6K2m5ZCO77yMQDxiPuWkqea0pTwvYj7mu6jmtbfkuqToraYg5riv5Y2X5aSn6Zif56uL5Y2z5oiQ56uL5LiT5qGI57uE77yM5YW15YiG5Zub6Lev77yM5LiA6Lev6LSf6LSj5YuY5p+l44CB57u05oqk44CB5aSE572u546w5Zy677yb56ys5LqM6Lev5L6d5omY56eR5oqA5omL5q6177yM5ZCM5pe25a+75om+5LqL5pWF546w5Zy65ZGo6L655bqX6ZO655qE6KeG6aKR55uR5o6n77yM5p+l5om+57q/57Si77yb56ys5LiJ6Lev5rK/6YCD6YC45Y+45py65Y+v6IO955qE6YCD56qc6Lev57q/5byA5bGV5o6S5p+l77yM6LWw6K6/5ZGo6L655YW25LuW55uu5Ye76K+B5Lq677yb56ys5Zub6Lev5a+555Sx5LqL5pWF5Zyw54K56L6Q5bCE55qE6YeN6KaB6Lev5Y+j44CB5bGF5rCR5bCP5Yy66L+b6KGM5biD5o6n77yM5rOo5oSP5Y+R546w44CB5oum5oiq5auM55aR6L2m6L6G44CC55So5pe25LiA5bCP5pe26LCD5Y+W5aSn6YeP55qE55uR5o6n5b2V5YOP77yM57uG6Ie05pG45o6S6IKH5LqL6L2m6L6G55qE6KGM6am26L2o6L+577yM57uI5LqO5pCc6I636IKH5LqL6YCD6YC46L2m6L6G6KeG6aKR5Zu+54mH44CC55Sx5LqO6K+l6L2m54mM54Wn5Lik5L2N5pWw5a2X44CB5a2X5q+N5qih57OK5LiN5riF77yM5Yqe5qGI5rCR6K2m6YGC5bCGMjbkuKrlrZfmr43jgIExMOaVsOWtl+mAkOS4quW9leWFpeafpeivou+8jOe7iOS6juehruiupOiCh+S6i+i9pui+huOAgue7j+i/h+S4jui9pui+hueZu+iusOi9puS4u+iBlOezu+WQjuaIkOWKn+mUgeWumueKr+e9quWrjOeWkeS6uuWPiuWFtuWkp+iHtOaWueS9jeOAguS4uumYsuatouWrjOeWkeS6uue7p+e7remAg+eqnO+8jOawkeitpumpsei9puS4ieWNgeWFrOmHjOa3seWFpeWkquW5s+adkeafkOadkeW6hOW8gOWxleaRuOaOku+8jOacgOe7iOWwhueKr+e9quWrjOeWkeS6uueqpuafkOafkOS4gOS4vuaKk+iOt++8jOW5tui1t+iOt+iCh+S6i+i9pui+hu+8jOaIkOWKn+WRiuegtOS6huS4gOi1t+mHjeWkp+S6pOmAmuiCh+S6i+mAg+mAuOahiOOAguebruWJje+8jOahiOS7tuato+WcqOi/m+S4gOatpeWuoeeQhuS4reOAgu+8iDxiPuWkqea0pTwvYj7kuqTorabvvIk=', null, '3', '1', '1607746470', null, '0', '0.3', '天津', 'm.weibo.cn', '微博', null, '0.9631226062774658', null);"

result = re.findall('(?<=\().*?(?=\))', str2, flags=0)

result_list = []

for item in result:
      temp = []
      str_list = item.split(', ')

      for index in range(len(str_list)):
            if index == 0 or index == 11 or index == 16:
                  str_temp = str_list[index]
                  str_temp = str_temp.replace(' ', '')
                  str_temp = str_temp.replace('\'', '')
                  if index == 0:
                        temp.append(int(str_temp))
                  else:
                        temp.append(float(str_temp))
      result_list.append(temp)


print(result_list)
'''
#=============================================================================
'''
data_dict = {}

data_dict['t1'] = [1,2,3]
data_dict['t2'] = [4,5,6]
data_dict['t3'] = [7,8,9]
data_dict['t4'] = [10,11,12]
data_dict['t5'] = [13,14,15]


for item in data_dict:
      print(data_dict[item])
'''

#=============================================================================
'''
watermark:str = 'test360'

binarr = ''.join([bin(ord(c)).replace('0b', '') for c in watermark])


print(binarr)

#bin 6-7 ascii， 采用动态规划输出结果
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


print(bin_2_str(binarr))
'''
#=============================================================================
'''
data:ndarray = np.array([
		[1,2,3],
		[4,5,6],
		[7,8,9],
		[0,0,0]
	])

print(data.shape[0])
'''
#=============================================================================
'''
seckey = 'accadwde!'
primary = '102'

h = hmac.new(primary.encode('utf-8'), seckey.encode('utf-8'), digestmod='MD5').hexdigest()
h1 = hmac.new(seckey.encode('utf-8'), h.encode('utf-8'), digestmod='MD5').hexdigest()


print(int(h1, 16) % 100)
'''

#=============================================================================

MAX_OPTIOM = 1  #求解全局最优的最大解
MIN_OPTIOM = 0

DISTORTION_BOUND = 1   #误差嵌入类型  1   给出上下界
DISTORTION_TYPE = 2    #误差嵌入类型  2   给出分段的上下界

REF_RATION = 0.5   #0-1   ref的系数,经过实践，RATION越小，MAX和MIN间的差距越大

PATTERN_SEARCH_SHORT_RATION = 0.75   #在单论搜索最大/最小值失败后，步长的缩短系数，此处采用减半策略  
PATTERN_SEARCH_INIT_ADD_SPEED = 3  # >=1
PATTERN_SEARCH_PRECISION = 0.0000001  #模式搜索最小的精度，|a-b|差值小于该值认为a == b

#兼顾效率和区分度，最佳的数据子集大小为200
MIN_DATA_SET_PARTITION = 200


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

      param_alpha = 1.0

      for index in range(combine_vector.shape[0]):
            sum += 1 - 1 / (1 + pow(math.e, param_alpha * (combine_vector[index] - ref_val)))

      return sum / combine_vector.shape[0]



def search_one_round(data_vector:ndarray, addtion_vector:ndarray, constrain_set:[], direction_type:int, forward_len:float):
      #此处用的应该是sqrt均方差，而不是var方差
      tao_val = count_hiding_function_val(data_vector + addtion_vector)

      for index in range(data_vector.shape[0]):
            step_moved = False

            if addtion_vector[index] + forward_len * data_vector[index] <= data_vector[index] *  constrain_set[1] and \
                  addtion_vector[index] + forward_len * data_vector[index] >= data_vector[index] *  constrain_set[0]: #没有超过约束

                  origin_add = addtion_vector[index]
                  addtion_vector[index] = addtion_vector[index] + forward_len * data_vector[index]

                  tao_temp_val = count_hiding_function_val(data_vector + addtion_vector)

                  if direction_type == MAX_OPTIOM:
                        if tao_temp_val > tao_val:
                              tao_val = tao_temp_val
                              step_moved = True
                        else:
                              #恢复数据
                              addtion_vector[index] = origin_add
                  else:
                        if tao_temp_val < tao_val:
                              tao_val = tao_temp_val
                              step_moved = True
                        else:
                              #恢复数据
                              addtion_vector[index] = origin_add

            #如果正向移动没有得到效果，则尝试反向移动一次
            if  step_moved == False and addtion_vector[index] - forward_len * data_vector[index] >= data_vector[index]  * constrain_set[0] and \
                  addtion_vector[index] - forward_len * data_vector[index] <= data_vector[index]  * constrain_set[1]: #没有超过约束

                  origin_add = addtion_vector[index]
                  addtion_vector[index] = addtion_vector[index] - forward_len * data_vector[index]

                  tao_temp_val = count_hiding_function_val(data_vector + addtion_vector)

                  if direction_type == MAX_OPTIOM:
                        if tao_temp_val > tao_val:
                              tao_val = tao_temp_val
                              step_moved = True
                        else:
                              addtion_vector[index] = origin_add
                  else:
                        if tao_temp_val < tao_val:
                              tao_val = tao_temp_val
                              step_moved = True
                        else:
                              addtion_vector[index] = origin_add
            


      #返回一轮最优结果后的函数值和向量
      return tao_val, addtion_vector


#模式搜索最优化
def pattern_search_optiom_with_range(optim_type:int, data_vector:ndarray, constrain_set:[]):

      addtion_vector_1 = []
      #给定随机初始值
      for index in range(data_vector.shape[0]):
            if index % 2 == 0:
                  addtion_vector_1.append(data_vector[index] * random.uniform(0.3, 1) * constrain_set[1])
            else:
                  addtion_vector_1.append(data_vector[index] * random.uniform(0.3, 1) * constrain_set[0])

      addtion_vector = np.asarray(addtion_vector_1)
      
      init_tao_val = count_hiding_function_val(data_vector + addtion_vector)

      not_found_val = True

      short_step_ration = 1.0

      best_addtion_vector = addtion_vector

      #终止条件  --沿最优方向 搜索一轮后，没有更优结果，且缩小步长再次搜索后没有更优结果
      while not_found_val:
            #缩短1次STEP
            #暂时不搜索了，提高运行速度，直接退出，得到当前的最优解
            if short_step_ration < 0.125:
                  not_found_val = False
                  break

            #change
            step_len = (constrain_set[1] - constrain_set[0]) * 0.1 * short_step_ration
            #进行轴搜索
            tao_temp_val, add_fix_vetctor = search_one_round(data_vector, addtion_vector, constrain_set, optim_type, step_len)

            if optim_type == MAX_OPTIOM:   #查找全局最大值
                  if tao_temp_val - init_tao_val > PATTERN_SEARCH_PRECISION:
                        #进行模式搜索，沿着N维向量的当前方向进行
                        init_tao_val = tao_temp_val
                        best_addtion_vector = add_fix_vetctor

                        addtion_vector = add_fix_vetctor + PATTERN_SEARCH_INIT_ADD_SPEED * (add_fix_vetctor - addtion_vector)
                  else:
                        #退回出发点
                        addtion_vector = best_addtion_vector

                        #算短步长继续搜索
                        short_step_ration = short_step_ration * PATTERN_SEARCH_SHORT_RATION

            else:   #查找全局最小值
                  if init_tao_val - tao_temp_val > PATTERN_SEARCH_PRECISION:
                        #进行模式搜索
                        init_tao_val = tao_temp_val
                        best_addtion_vector = add_fix_vetctor

                        addtion_vector = add_fix_vetctor + PATTERN_SEARCH_INIT_ADD_SPEED * (add_fix_vetctor - addtion_vector)
                  else:
                        #退回出发点
                        addtion_vector = best_addtion_vector

                        #算短步长继续搜索
                        short_step_ration = short_step_ration * PATTERN_SEARCH_SHORT_RATION
      
      return best_addtion_vector, init_tao_val

#方式2   给出各个数据的范围，在各自的type范围内变动
def pattern_search_optiom_with_types():
      pass



def count_insert_vector(optim_type:int, distortion_type:int, data_vector:ndarray, constrain_set:[]):
      
      if distortion_type == DISTORTION_BOUND:            
            delta_vetor, X_max_min = pattern_search_optiom_with_range(optim_type, data_vector, constrain_set)

            return delta_vetor, X_max_min

      elif distortion_type == DISTORTION_TYPE:
            pass
      else:
            print('distortion type no support, do nothing')
            return None, None


#从计算出的MAX和MIN队列种计算解码阈值T*
def count_decode_thresh_hold(x_min:ndarray, x_max:ndarray, mean_sqr_err_0:float, mean_sqr_err_1:float, mean_0:float, mean_1:float):
      
      prob_1 = x_max.shape[0] / (x_max.shape[0] + x_min.shape[0])
      prob_0 = 1 - prob_1

      a = (pow(mean_sqr_err_0, 2) - pow(mean_sqr_err_1, 2)) / (2 * pow(mean_sqr_err_0, 2) * pow(mean_sqr_err_1, 2))
      b = ((mean_0 * pow(mean_sqr_err_1, 2)) - (mean_1 * pow(mean_sqr_err_0, 2))) / (pow(mean_sqr_err_0, 2) * pow(mean_sqr_err_1, 2))
      c = math.log((prob_0 * mean_sqr_err_1 / prob_1 * mean_sqr_err_0)) +  ((pow(mean_1, 2) * pow(mean_sqr_err_0, 2)) - (pow(mean_0, 2) * pow(mean_sqr_err_1, 2))) / (2 * pow(mean_sqr_err_0, 2) * pow(mean_sqr_err_1, 2))
      
      print('---------prob0 [%f] prob1 [%f] a [%f] b [%f] c [%f]' % (prob_0, prob_1, a, b, c))

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
            return x1
      else:
            return x2


def gaussian(x,*param):
    u = param[0]
    sig = param[1]

    return np.exp(-(x - u) ** 2 / (2 * sig ** 2))/ ((sig * math.sqrt(2 * math.pi)))

#计算一组统计数据的高斯分布参数
def count_gauss_distribute_params(x_vector:ndarray, y_vector:ndarray):
      #正态分布的初始化的均值和方差数据
      p0=[0.5, 0.75] 

      popt, pcov = curve_fit(gaussian, x_vector, y_vector, p0)

      return popt[0], popt[1]

#将1维的数据，以小数点后2位为精度，分散到0-1为界的X-Y坐标系内，方便后续 正态分布的拟合计算
def convert_data_into_xy(data_vector:ndarray):
      x_list = []
      y_list = []

      for index in range(1, 101):
            x_list.append(round(0.01 * index, 2))
            y_list.append(0)

      for item in data_vector:
            slot = int(round(item, 2) * 100 % 100 )
            y_list[slot] = y_list[slot] + 1

      print(y_list)
      return np.asarray(x_list), np.asarray(y_list)


#解码，从给定的分组种获取水印的BIT位信息
def decode_bit_from_partition(thresh_hold:float, data_vector:ndarray):
      tao_val = count_hiding_function_val(data_vector)

      result = 0

      if tao_val >= thresh_hold:
            result = 1

      print('+++++++ thresh [%f] tao [%f] result [%d]' % (thresh_hold, tao_val, result))

      return result


#约束集暂时按最大最小 这里按百分比的绝对值给出
constrain_set = [-0.05, 0.05]

max_list = []
min_list = []

max_result_list = []
min_result_list = []

for index_1 in range(50):

      data_vector_min = []
      for index in range(MIN_DATA_SET_PARTITION):
            data_vector_min.append(random.uniform(1, 20))

      data_vector_max = []
      for index in range(MIN_DATA_SET_PARTITION):
            data_vector_max.append(random.uniform(1, 20))

      delta_vetor_min, Xmin = count_insert_vector(0, DISTORTION_BOUND, np.asarray(data_vector_min) , constrain_set)
      min_list.append(Xmin)
      #保存计算后的数据，用于验证
      min_result_list.append(np.asarray(data_vector_min) + delta_vetor_min)

      delta_vetor_max, Xmax = count_insert_vector(1, DISTORTION_BOUND, np.asarray(data_vector_max) , constrain_set)
      max_list.append(Xmax)

      #保存计算后的数据，用于验证
      max_result_list.append(np.asarray(data_vector_max) + delta_vetor_max)

      print('--------------- sample [%d] min = [%f] max = [%f] ' % (index_1, Xmin, Xmax))
      

min_x, min_y = convert_data_into_xy(np.asarray(min_list))
gauss_min_mean, gauss_min_mean_sqrt = count_gauss_distribute_params(min_x, min_y)

max_x, max_y = convert_data_into_xy(np.asarray(max_list))
gauss_max_mean, gauss_max_mean_sqrt = count_gauss_distribute_params(max_x, max_y)

#绘制图像
plt.plot(min_x,min_y,'b+:',label='bit_0')
plt.plot(min_x,max_y,'c+:',label='bit_1')
p_min = [gauss_min_mean, gauss_min_mean_sqrt]
p_max = [gauss_max_mean, gauss_max_mean_sqrt]
plt.plot(min_x,gaussian(min_x,*p_min),'ro:',label='fit_bit_0')
plt.plot(min_x,gaussian(min_x,*p_max),'o:',label='fit_bit_1')
plt.legend()
plt.show()
#绘制结束

result = count_decode_thresh_hold(np.asarray(min_list), np.asarray(max_list), gauss_min_mean_sqrt, gauss_max_mean_sqrt, gauss_min_mean, gauss_max_mean)


print('------------ thresh = [%f] min mean = [%f]  max mean = [%f]' % (result, np.mean(min_list), np.mean(max_list)))


print('---------------------------- bit 0 results')
for index in range(len(min_result_list)):
      bit_con = decode_bit_from_partition(result, min_result_list[index])

print('---------------------------- bit 1 results')
for index in range(len(max_result_list)):
      bit_con = decode_bit_from_partition(result, max_result_list[index])

