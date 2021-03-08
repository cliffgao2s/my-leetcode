
import numpy as np, math
import pylab as plt
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp

#===================================================================
'''
x = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 
0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0]

y_min = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 8, 8, 16, 7, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


y_max = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 8, 6, 12, 5, 5, 5, 6, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def gaussian(x,*param):
    u = param[0]
    sig = param[1]

    return np.exp(-(x - u) ** 2 / (2 * sig ** 2))/ ((sig * math.sqrt(2 * math.pi)))
    #return param[0]*np.exp(-np.power(x - param[1], 2.) / (2 * np.power(param[2], 2.)))
 
p0=[0,math.sqrt(0.2)] 

#popt = 修正后的参数
popt_min, pcov_min = curve_fit(gaussian,x,y_min,p0)
popt_max, pcov_max = curve_fit(gaussian,x,y_max,p0)

plt.plot(x,y_min,'b+:',label='bit_0')
plt.plot(x,y_max,'c+:',label='bit_1')
plt.plot(x,gaussian(x,*popt_min),'ro:',label='fit_bit_0')
plt.plot(x,gaussian(x,*popt_max),'o:',label='fit_bit_1')
plt.legend()
plt.show()
'''

#===================================================================
'''
t1 = np.array([1,2,3,4,5])

t2 = np.array([0,1,2,3,4])

t1 = t1 + t2 * 3

print(t1)
'''

#===================================================================
'''
t1 = np.array([1,2,3,4,5])

def test_input(t1):
    t2 = np.array([0,1,2,3,4])
    t1 = t1 + t2
    return t1

t3 = test_input(t1)
print(t1)
print(t3)
'''
#===================================================================
'''
import random

data_vector_min = []
for index in range(100):
    data_vector_min.append(random.uniform(1, 100))

print(data_vector_min)
'''
#===================================================================
'''
val = [[1, 0.9], [2, 0.33], [3, 0.41] , [4, 0.19]]

val1 = np.asarray(val)

print(val1[:,1])

add = [1,2,3,4]

val1[:,1] = val1[:,1] + np.asarray(add)

print(val1)
'''
#===================================================================  验证NUMPY数组的初始化和合并
'''
val = np.empty((0,0))

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

val = np.append(val, v1)
val = np.append(val, v2)

print(val)
print(val.shape)

val = val.reshape(2,3)
print(val)
print(val.shape)
'''

#===================================================================
'''
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


print(bin_2_str('1100001'))
'''
#======================================================
'''
MIN_BIT_RUDENT = 3
MIN_DATA_SET_PARTITION = 200

def count_partitions(data_set_len:int, watermark_len:int):
      if watermark_len * MIN_BIT_RUDENT * MIN_DATA_SET_PARTITION > data_set_len:
            return 0

      addtion_num = 2

      while True:
            if watermark_len * ( MIN_BIT_RUDENT + addtion_num)* MIN_DATA_SET_PARTITION < data_set_len:
                   addtion_num += 2
            else:
                  return  watermark_len * MIN_BIT_RUDENT + addtion_num - 2


print(count_partitions(10000, 7))
'''
#=====================================================
import base64

def encap_rtn_datas(thresh:float, secrect:str, partition_nums:int, watermark:str):
    result = ''
    seprate_str = '|^|'

    result += str(thresh) + seprate_str + secrect + seprate_str + str(partition_nums) + seprate_str + watermark

    result = result.encode('utf-8')

    return base64.b64encode(result)


def decode_rtn_datas(input:str):
    input1 = base64.b64decode(input).decode("utf-8")
    seprate_str = '|^|'
    strlist = input1.split(seprate_str)

    return float(strlist[0]), strlist[1], int(strlist[2]), strlist[3]

result = encap_rtn_datas(0.357046, 'sxcqq1233aaa', 21, 'a')

print(result)
print(decode_rtn_datas(result))