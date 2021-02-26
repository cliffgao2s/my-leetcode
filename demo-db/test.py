import re, numpy as np, hmac, random
from numpy import ndarray

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
MIN_OPTIOM = 2

DISTORTION_BOUND = 1   #误差嵌入类型  1   给出上下界
DISTORTION_TYPE = 2    #误差嵌入类型  2   给出分段的上下界

REF_RATION = 0.1   #0-1   ref的系数

PATTERN_SEARCH_SHORT_RATION = 0.5   #在单论搜索最大/最小值失败后，步长的缩短系数，此处采用减半策略  
PATTERN_SEARCH_INIT_ADD_SPEED = 3  # >=1
PATTERN_SEARCH_PRECISION = 0.000001  #模式搜索最小的精度，|a-b|差值小于该值认为a == b


def count_hiding_function_val(ref_val:float, combine_vector:ndarray):
      sum = 0

      for index in range(combine_vector.shape[0]):
            if combine_vector[index] >= ref_val:
                  sum += 1 

      return sum / combine_vector.shape[0]


def search_one_round(data_vector:ndarray, addtion_vector:ndarray, constrain_set:[], direction_type:int):
      ref_val = np.mean(data_vector + addtion_vector) + REF_RATION * np.var(data_vector + addtion_vector)
      tao_val = count_hiding_function_val(ref_val, data_vector + addtion_vector)

      print('---------- 1 round enter ref = [%f] tao = [%f]' % (ref_val, tao_val))

      for index in range(data_vector.shape[0]):
            step_moved = False

            #轴移动的步长  待商榷??? 固定值 OR 固定比例
            forward_len = data_vector[index] / 100

            if addtion_vector[index] + forward_len <= data_vector[index] *  constrain_set[1]: #没有超过约束
                  origin_add = addtion_vector[index]
                  addtion_vector[index] = addtion_vector[index] + forward_len

                  ref_temp_val = np.mean(data_vector + addtion_vector) + REF_RATION * np.var(data_vector + addtion_vector)
                  tao_temp_val = count_hiding_function_val(ref_temp_val, data_vector + addtion_vector)

                  #print('------- index [%d] forward tao = [%f] lasttao = [%f]' % (index, tao_temp_val, tao_val))

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
            if  step_moved == False and addtion_vector[index] - forward_len >= data_vector[index]  * constrain_set[0]: #没有超过约束
                  origin_add = addtion_vector[index]
                  addtion_vector[index] = addtion_vector[index] - forward_len

                  ref_temp_val = np.mean(data_vector + addtion_vector) + REF_RATION * np.var(data_vector + addtion_vector)
                  tao_temp_val = count_hiding_function_val(ref_temp_val, data_vector + addtion_vector)

                  #print('------- index [%d] backward tao = [%f] lasttao = [%f]' % (index, tao_temp_val, tao_val))

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
def pattern_search_optiom_with_range(optim_type:int, data_vector:ndarray, addtion_vector:ndarray, constrain_set:[]):
      
      mean_val = np.mean(data_vector + addtion_vector)
      es_val = np.var(data_vector + addtion_vector)

      ref_val = mean_val + REF_RATION * es_val

      init_tao_val = count_hiding_function_val(ref_val, data_vector + addtion_vector)

      not_found_val = True

      #终止条件  --沿最优方向 搜索一轮后，没有更优结果，且缩小步长再次搜索后没有更优结果
      while not_found_val:
            #进行轴搜索
            tao_temp_val, add_fix_vetctor = search_one_round(data_vector, addtion_vector, constrain_set, optim_type)
            if optim_type == MAX_OPTIOM:   #查找全局最大值
                  if tao_temp_val - init_tao_val > PATTERN_SEARCH_PRECISION:
                        #进行模式搜索，沿着N维向量的当前方向进行
                        init_tao_val = tao_temp_val
                        addtion_vector = addtion_vector + PATTERN_SEARCH_INIT_ADD_SPEED * (add_fix_vetctor - addtion_vector)
                  else:
                        #缩短1次STEP
                        #暂时不搜索了，提高运行速度，直接退出，得到当前的最优解
                        not_found_val = False

            else:   #查找全局最小值
                  if init_tao_val - tao_temp_val > PATTERN_SEARCH_PRECISION:
                        #进行模式搜索
                        init_tao_val = tao_temp_val
                        addtion_vector = addtion_vector + PATTERN_SEARCH_INIT_ADD_SPEED * (add_fix_vetctor - addtion_vector)
                  else:
                        #缩短1次STEP
                        not_found_val = False
      

      return addtion_vector, init_tao_val

#方式2   给出各个数据的范围，在各自的type范围内变动
def pattern_search_optiom_with_types():
      pass



def count_insert_vector(optim_type:int, distortion_type:int, data_vector:ndarray, constrain_set:[]):
      #初始化的嵌入量向量，默认为全0
      addtion_vector = []
      #init delta vector
      for item in data_vector:
            addtion_vector.append(0.0)

      if distortion_type == DISTORTION_BOUND:            
            delta_vetor, X_max_min = pattern_search_optiom_with_range(optim_type, data_vector, np.asarray(addtion_vector), constrain_set)

            return delta_vetor, X_max_min

      elif distortion_type == DISTORTION_TYPE:
            pass
      else:
            print('distortion type no support, do nothing')
            return None, None


#数据集填入随机数据
data_vector = [18.333082920288682, 14.458876629688948, 5.698143762730364, 9.02734240691901, 11.826959991647417, 12.22261717335091, 5.594381773561297, 10.304687605239836, 13.460494103599345, 16.372969186871515, 3.7073787901024415, 9.07831533172766, 13.048752128375899, 9.92205860845082, 6.2027132014078585, 1.912678241043102, 14.627788144975082, 1.4261248625738374, 14.266181722049204, 11.418059154342656, 18.116621277154938, 2.33306983754081, 9.384136646396696, 6.207623294180499, 17.389504277626568, 4.520149458189752, 18.727560611382543, 11.748007478958998, 18.11425814598217, 12.864792826113321, 12.175812863668106, 12.882439947032823, 10.608652394179124, 12.725949801948135, 10.940272729307896, 1.3736930990783582, 17.16836115934502, 8.44554684244844, 16.428343471704604, 14.087152076529458, 8.767809893572316, 1.617268601576109, 5.234675636304963, 10.825045177485368, 13.148262806447503, 15.58068159591609, 18.51893123025372, 15.175945565420323, 10.238050151633033, 10.276148509703141, 8.279193130377928, 11.728405963481924, 2.9729674320594404, 10.684963418753917, 18.40972142645674, 14.154785570478344, 11.703405819856435, 17.596318615189155, 12.980750389530735, 18.492451271483535, 5.732598917147146, 3.8955003781347646, 6.962402912880885, 5.172744308136853, 19.33975020775755, 14.269799010256733, 16.485566876882068, 7.981693476327598, 17.614080889642494, 5.690756280918868, 12.317599250232886, 16.058473904564263, 6.833318904119311, 2.146112724608478, 15.690097483163768, 3.4040482266766467, 15.139735244345385, 12.671683006077414, 12.00280183952903, 2.173410088506466, 10.80481476545556, 18.29441949678893, 11.633120264965623, 18.649002257615603, 4.432068361618346, 19.901255300862214, 19.97926581148344, 7.5244743192573775, 1.1724878283772253, 11.27854079756692, 7.5596168756838065, 3.173217330142718, 16.64567556000265, 3.182549910327042, 11.308122954837788, 7.297410032749411, 10.230298448106822, 9.787436771504597, 5.977038107413642, 8.908088867946145, 13.310613064454566, 18.323251231029825, 5.4092247254673005, 7.5887783295134845, 3.491835522604966, 12.379239488625732, 14.85909288052503, 11.238192652355602, 2.143655649780899, 16.521625714865294, 6.789954292572946, 14.461749215326593, 7.641234918571055, 18.101607614268218, 2.8295523941081795, 2.2004496860973903, 
3.477281483440868, 16.219037736224067, 13.699798090133964, 15.438429470615278, 5.061647383542287, 5.011958047183512, 9.456771556690065, 14.579350858375447, 3.579958441617513, 4.104047608899172, 17.768607210973332, 19.78981397859725, 5.415244321745304, 18.185201838909094, 8.831074438075202, 6.718582025519084, 7.5241568253036135, 11.826186335010874, 6.297162836314578, 1.7782759366499903, 10.573042157714656, 8.951260453239232, 5.719541363467497, 9.50322043645322, 12.273762483150565, 15.977772149719923, 3.97261621784699, 18.206620170885408, 9.320309977053231, 19.458763656481295, 15.081373764862695, 17.486464976145914, 15.414653097954746, 12.51796579503913, 9.184765262428755, 3.818334173231303, 7.169935955083834, 14.931805365077077, 2.2818649762471184, 13.31582875381693, 10.335980857364866, 10.75237883762369, 15.320925128929938, 10.295983727165797, 4.347255845237984, 9.834395277564607, 14.722048980172369, 13.293369087842269, 12.281359488666832, 19.428256331123862, 9.477647660958729, 1.4840047181253506, 15.69808907462745, 15.530607282985777, 5.255387889985462, 17.917361142302966, 14.800865928064843, 16.511819899580267, 18.595544170936908, 11.187766121575176, 16.29685512800056, 17.300257131197274, 14.367085710216186, 3.8861016035043696, 18.52149595712215, 16.98425028151451, 15.30950214821312, 16.712717986259516, 8.996590288394192, 13.370170201010263, 11.580358308931016, 5.820572352235475, 14.952188248663408, 15.976834131294824, 13.642381540722003, 10.638165551549012, 12.64525111043191, 1.1190112385149789, 11.15691349418911, 16.833569618004354, 11.677498385709765, 13.442187940526358, 2.089167254507084, 10.187241131739157, 1.6716889191617557, 3.2636184639621324, 4.647539489346797, 19.896544105138574, 14.9276973427832, 18.401652200927842, 10.475650652380848, 4.522933568937311, 3.03254822172766, 2.465347367431888, 1.696198010359974, 12.921807382214553, 7.707766850554925, 4.492274967598355, 10.500787535530106, 15.84532976804672, 18.664862830129213, 13.0032678537954, 14.687031959771488, 14.755369161575539, 2.378942086268137, 6.97886420955615, 8.790974967799865, 16.775248878752436, 13.768411632253363, 1.7856312239774104, 1.6803626791036324, 10.743675125178665, 1.6881568886938547, 9.20434944441394, 8.188740785407827, 13.976904597076595, 8.30935532608102, 9.818084674320174, 2.2201213633462764, 8.28183362894989, 11.650627252343755, 4.3556318505146825, 10.651220522934482, 6.464819179999475, 3.4491675786254308, 15.860840820417964, 11.918834958740362, 16.181928930105876, 7.318129303655745, 1.0162486762881247, 18.7576275053445, 10.764261396531992, 13.640977317248508, 4.280764868121041, 1.646355725173625, 14.648840865478622, 6.530297236231196, 4.092305011401756, 16.336829318560063, 8.448033351914543, 9.186420671736329, 16.68347894587039, 17.70961178564304, 9.578784559014938, 13.70008570835995, 13.553166520905602, 3.1278650270581108, 3.9600613022435662, 11.889227141465161, 15.805270957344181, 12.425238731650627, 1.0837641923674064, 6.465599130383823, 19.361115280327287, 3.3169227681781193, 15.755588855164845, 2.8323784019579423, 7.771044846024549, 3.238208043650318, 16.59808207348693, 6.660652635407502, 10.632193096474559, 17.407401778415935, 18.942939223266336, 14.411301277833019, 13.573712753037915, 17.29095606127013, 12.745634832807006, 4.689505597876739, 8.171392810175961, 15.66182685589309, 16.62114425173251, 3.803522550682715, 18.116084710524863, 3.0327007517876754, 1.510288054810661, 15.573917509054624, 17.31044071362765, 8.453374745222547, 13.486037396004587, 18.342935324340345, 6.8929794330495895, 4.1780651105601505, 4.155262139897989, 9.789882361599775, 5.919157456131138, 4.132417565041717, 13.78524077974237, 18.85886753352173, 8.39780451190701, 7.185875981207647, 1.0951759298104267, 19.54993245664591, 10.419179802759276, 9.757726267379718, 15.08993004240721, 10.382012385762968, 12.950096532632234, 8.595647393310083, 14.281803653303514, 9.804876515150678, 15.106134814344209, 17.277182295749437, 16.766933195705462, 12.474932713808732, 15.697411554126049, 12.138416628371553, 8.821212496572347, 2.5296333008017315, 14.417303778297764, 17.970689094621267, 19.159775118813943, 4.676444079369263, 17.53871069219852, 14.21196169796157, 8.57844420450358, 2.776733613788328, 19.932006788552847, 2.374824462553221, 4.001666922447261, 13.150651786612597, 11.57721379854596, 17.270408062369025, 11.790560561568645, 4.293862547959206, 7.956470433905832, 7.999330318217644, 4.795677568920502, 13.770146411046012, 9.543110657275369, 12.351789201513345, 5.990523465031036, 14.852458969695029, 16.26450633430985, 6.840769765095375, 4.041858174721243, 1.5200747383292725, 1.8010459787660023, 8.08972535225297, 10.889387708356127, 9.324279806275937, 11.951028672983425, 7.10150750872248, 17.420596545699315, 16.144760984727597, 11.872914361167325, 3.264690176656224, 2.423260778480156, 9.912811213030801, 2.930829130818535, 15.043239287473975, 9.92839881155577, 6.547488104679984, 18.15757802680196, 18.985502423590063, 17.71659803588177, 1.9816548604763815, 15.14605194273837, 10.328887221217936, 11.158526724605702, 6.977297886982599, 2.415058059869316, 19.552437389685487, 14.800689489795456, 14.358715721605067, 8.594372335506298, 9.735930260445109, 14.493144141462878, 18.305501086171212, 12.244469742550566, 4.468240657257326, 9.213416504827975, 5.32412602329995, 8.183344951355275, 8.981170811028448, 9.194037065301002, 7.094022950106412, 14.601799391423521, 7.579701618346537, 11.439034896460345, 2.938425876091977, 17.161614111491513, 5.588865439147188, 18.939215247453063, 10.468570649060457, 13.733902939648173, 17.23123025741976, 11.813825514512565, 14.687868571134388, 6.395100672708933, 6.714397661783296, 13.765931504791183, 16.226310110916593, 18.50739031897511, 8.444207189898927, 17.847523409903115, 18.938653786796824, 15.376093741392872, 9.335658941348282, 2.7652314776491043, 5.64506865273923, 10.859039449353808, 5.140957987064095, 2.1563754989038895, 10.649878222953909, 13.331723624569038, 14.483070622434818, 12.82033641052725, 7.30712431031583, 13.247543869497811, 7.818606869095605, 11.317040084198801, 15.167423664175955, 1.0061936975057035, 14.72357406398534, 3.527254848978161, 6.441510069251901, 8.841183147054213, 6.015170956547379, 6.047483491960391, 11.6791992470962, 9.100415173152765, 13.028297998869405, 8.73227410767485, 12.407569764303256, 17.453426355450368, 11.362689263566981, 10.480743858144868, 13.837985712559403, 4.384716322925293, 3.336751494776338, 15.708444767730253, 14.216100840447863, 
19.127939675620077, 5.03734786082225, 8.376212254442043, 5.791355545140048, 9.660420467963982, 12.64847869416329, 17.749322657468287, 6.258822376612362, 10.788455321188366, 10.881734739011767, 10.756440082385149, 13.884839830774306, 2.2868947179579893, 16.730799197537443, 19.125895030699596, 4.262246739793937, 11.75160026619697, 10.360936806520215, 16.359202355500692, 12.85936880596589, 9.67996530119227, 19.819912874852488, 5.000391100534218, 17.59083481108317, 9.301367741975447, 19.347311142474155, 17.889157389413505, 17.1001424322074, 14.032710754689463, 13.703509367086069, 15.282170745447784, 5.406319167103985, 4.500706497337966, 6.139827399672246, 11.179305786001365, 19.435674197463157, 15.985905111123063, 19.975793547998897, 4.78144534910322, 7.402868074391057, 11.154949140183165, 7.520500694031163, 17.475047896336584, 10.053086689945767, 8.99405745183362, 15.44045966283755, 8.272358209861686, 9.711977213130883, 6.216249322889076, 1.8834716047264595, 9.864777506071384, 5.769563061654876, 16.971075967601443, 19.776024605774857, 2.043475136289881, 7.709817409647306, 1.1616350435193739, 12.814267678274131, 16.39233267987275, 2.041831666490347, 17.694327732098564, 9.914856615993193, 10.109775942471934, 5.228875066490568, 9.589153699070902, 7.133304169975775, 7.436084413357179, 7.7671324959344705, 6.774187209605269, 11.2628111379236, 6.273817361128873, 18.035368955113046, 19.950954394831516, 4.112710917139918, 10.964236070746706, 11.718110227301613, 12.98091577056897, 4.499091017103492, 16.139484833824095, 16.419467863151297, 15.809735985834157, 3.618417870824602, 2.8811155448407364, 7.552931234252162, 14.871728956226683, 9.972112682692792, 7.898280928992725, 3.6889137180299993, 19.172445172749455, 16.904080449342214, 16.602594529951467, 18.443366117619924, 13.975102666017081, 17.863719654082033, 6.27397634915158, 18.1813193153245, 17.85239391651318, 9.11090083593632, 7.380868267972044, 15.049348104727612, 2.4682486168085322, 1.1837755123018832, 19.455224087758246, 18.750237111108977, 9.927027153800479, 11.865864570666899, 14.310217424220909, 8.063603420952859, 13.464932759166704, 3.3893406623320304, 6.827602574024704, 10.698590368352331, 1.6802147701945156, 17.760038451653614, 12.240269894252318, 12.40230751221472, 3.7857521627242967, 7.3445887951627, 5.2592995803140274, 19.279384643346866, 19.473942855130367, 16.46888124146546, 4.652174432427157, 4.435228393557756, 18.106283601081127, 
4.925715252178382, 14.619076460462844, 8.890044717204567, 3.5762488319759878, 13.966371048075942, 5.081509878759368, 4.9853156497077125, 15.835467267129644, 8.586261125018266, 19.475202538708125, 2.060649787218117, 19.6571704937074, 19.694402437923152, 2.217730988317652, 11.585947596148714, 14.253930084251158, 13.925556894847126, 8.791547221765626, 5.834441814923284, 14.519780612457547, 3.951450502973544, 19.979412214927176, 7.363119369092191, 19.237773878963907, 10.675111357840727, 12.50025728772011, 5.435971970869682, 1.4852605640732923, 7.526694730107058, 16.101656257663066, 1.45646249837837, 14.639593520434675, 8.302307294133488, 13.883107459505196, 14.024392044826731, 12.877266823638802, 18.088150513711074, 13.107852548826141, 16.18344196584836, 19.810211452662532, 18.165474980930885, 14.875838310857516, 17.361164981029454, 12.465358213434184, 1.5132435909639335, 10.832663832391255, 5.6073862500506095, 14.586341256824587, 18.83899574529568, 14.845566633604605, 3.731557347926407, 5.213484917169704, 5.075552682590401, 19.23988557226599, 18.309538969969456, 18.287980668701522, 5.561219751417378, 10.948109236075728, 1.8241620603760524, 15.235890351325445, 19.46845690651345, 19.326049793094764, 1.7402439314183882, 16.173828254302435, 5.118323129947281, 10.549310340619433, 7.952693517686904, 15.470043206862675, 19.270685381768658, 12.216180355023795, 10.03679094047498, 8.728270649434684, 13.74521236110801, 10.95599793365924, 19.24453172312624, 14.010802040693477, 10.270508860506634, 10.828329519920016, 5.5248120854009155, 1.6856183852398323, 7.190946862672307, 11.242637322113398, 6.827170018439551, 15.40411016734782, 6.766449182199544, 15.539684426477603, 4.403984038344445, 3.097156785906069, 3.6417455669858314, 19.877297364468447, 4.5113081216188125, 12.040524288566791, 11.034979218596087, 10.664914294624028, 12.769489562113206, 16.851210507819456, 1.8948265874494448, 2.7850853455914644, 8.110479400907582, 17.341978390585634, 13.835797585345231, 18.094675594496564, 2.159336065713189, 14.891413104617678, 13.364894050641606, 8.6375942923402, 18.269455138953735, 8.225732765226336, 6.503680087584676, 14.10948016849361, 16.739995912292372, 16.98692543709309, 2.4682866195483033, 3.1731893258021793, 6.288671901434636, 10.506548907016812, 3.255481530948262, 15.203249115490516, 10.548475471036319, 17.294619534116755, 13.248498162443576, 15.619248305872805, 19.079112735463326, 14.150065796949265, 
11.970628141826419, 3.682955362083801, 11.129199171458758, 1.0791127310027706, 19.608955809138436, 14.731235341746439, 3.3124702687774947, 8.6057046673309, 16.095146001053806, 10.923760992085334, 4.338989261130935, 5.360602366676643, 17.180973453526203, 5.466502615415634, 18.56457418391944, 16.807184827030277, 8.430603705608796, 19.85091745625207, 6.45232319967889, 13.12173666127967, 1.8771974978895198, 4.093347556972818, 11.613476454959956, 19.225898926058555, 1.2637576900734382, 
4.073290976069866, 9.597314942184722, 11.163853508009014, 1.4635756431627363, 2.943323760043952, 6.716343676867513, 4.2315347821478175, 14.919940016050218, 11.373733757680357, 1.7596116114884301, 1.3148437813410925, 7.945119483543811, 19.24540754045226, 12.554135999652019, 10.651325715563193, 5.534292084307065, 13.740215862762748, 3.780312941594739, 1.509704345528188, 6.064640168673847, 10.497308304505536, 8.92876533589742, 1.9888974307800584, 7.43742969272991, 14.939023748637128, 
9.328827737055079, 2.9603633052562346, 9.91740162051118, 11.761531685470528, 9.945143318177884, 10.982541148831483, 9.660140971111078, 1.5246091220020186, 13.222447873693007, 18.914619525722156, 6.039032858915252, 1.1906054425637813, 18.29913930908912, 13.258023369189731, 4.61715290994018, 3.4458892688346054, 8.945449400758037, 10.598965868560702, 19.50807851483849, 13.22143337099287, 13.16109070213782, 1.438575907306169, 11.665371916478565, 10.064538065931766, 9.91789313440073, 11.610849145228674, 3.157162201278481, 2.444270151624857, 2.614224720809079, 17.96711185682994, 3.0954959264706297, 14.258322293513533, 10.242730332125603, 14.083387994835462, 17.62744698408435, 15.147582668747361, 19.36198081943689, 12.146272892343642, 16.457875843347203, 19.047739533969278, 8.727915198162739, 18.991877806882588, 3.200415573501117, 9.909040196278895, 10.432128927411089, 8.406534836252346, 13.913859755287044, 14.385272146587676, 12.615379296027774, 11.262583218897447, 4.688425773299297, 15.277397615163359, 14.873017600475691, 1.6421649171284614, 9.996879514294147, 2.85467393061998, 8.34442609127432, 14.308324850281407, 13.7105467846495, 11.67432270244065, 12.559658667407964, 7.818862658545403, 18.293983576980214, 12.025149595476854, 6.203089779642678, 18.88101041552015, 11.060143511602178, 18.023438412106888, 11.831915058900876, 15.739842299033453, 3.738657514393071, 4.584958035773926, 10.704032659491759, 7.421136517002598, 16.45242982085633, 
11.26191321033486, 19.734243685162475, 12.594583718981058, 12.819398711574605, 12.326448886754216, 12.654967413679046, 12.097874224308354, 3.1155391189595116, 2.953701376009141, 19.017694821682113, 12.743506595964163, 1.0709639452942532, 15.933739396656648, 19.530906575461778, 3.218683236889531, 15.420604147622655, 11.502330771411208, 7.774707352071044, 18.63043053818279, 10.607849178841416, 12.44395051195598, 15.570065936552638, 11.89064390066978, 3.448178709516915, 17.163383433495262, 6.534098133384702, 10.08510380698913, 14.712452545967036, 12.796245193675569, 3.8862189679492523, 6.320996520710624, 13.589534163662325, 17.31212071011654, 
1.7481334700693143, 11.164883159938455, 14.74281084471834, 6.041114121262429, 19.336193802530484, 2.131126420827764, 18.946078633512858, 15.036626956419447, 10.350837917885734, 19.549450207709064, 8.902236818664775, 15.930771328143365, 13.112995421942944, 17.742927695204806, 17.349935401358074, 14.959792445831509, 19.54207553509848, 6.888561867392731, 11.113274730475148, 12.045183305551149, 6.957508366056709, 3.2857267231377336, 10.346276771105169, 5.668540580942772, 17.69294619366561, 4.231209545970708, 13.819581915981875, 8.489308120432533, 15.59328005511023, 2.090220944248758, 19.357251807485174, 4.797769638792467, 9.560707906968753, 11.412023934968405, 19.451526827956645, 4.8092741181544385, 19.945416062767368, 12.821699458747776, 6.799366691745565, 8.683203050233498, 16.58503627722444, 10.796819567630214, 1.9373962427906304, 15.755644486094845, 11.823388468870892, 12.235227766726535, 13.331960217766202, 7.0576739215618165, 13.826631287221135, 4.01530689668291, 18.383791665407728, 3.820685904560826, 15.78057442827363, 7.626677103862034, 8.451804071397454, 16.763728279784328, 15.141350356662898, 11.938198478372005, 2.8196281739506457, 14.923608907691216, 16.87882789414822, 17.120449605013558, 4.606188776734549, 15.286431955772747, 15.304412986242761, 6.59513716631964, 2.4761883478220654, 9.255272952947971, 2.8893113397851917, 9.995402792206214, 6.892420371113506, 10.049034315638771, 10.404772767462694, 7.244137668534371, 10.608928082996364, 1.2229951461865194, 4.215067179100668, 11.784268038755366, 16.79404166423255, 15.654430366593578, 5.57177466481565, 17.37167021427944, 3.057105513501253, 17.785923970759942, 3.5803787327707837, 1.3040556405847392, 6.29909125575058, 11.334470376062521, 12.738379139700925, 8.599637118580223, 3.5362940822121196, 4.895910480744828, 10.052417454026628, 7.373470113055998, 11.021497729630306, 12.190657963342476, 5.4141196404767795, 14.275991465837716, 3.112796120177074, 14.27242006193777, 7.816019459653374, 3.6988210248361306, 12.842891882043551, 13.97422686203735, 1.398782359308703, 5.39302374872382, 3.032633662051709, 1.7313580710361505, 6.328293211702042, 11.368590210624399, 16.103247047603197, 19.21303105629546, 1.982274159954188, 4.966792186897717, 19.461515572683695, 17.52683538121051, 4.095867436800434, 1.8197394575009236, 19.856643296016156, 12.870307388465678, 14.8700488909472, 17.15398897729584, 8.079482796619015, 4.814163729599394, 12.392233104966873, 18.035959551192526, 1.4604366032051752, 15.090400303458733, 14.466004008389207, 11.864406529345533, 17.67632777350778, 3.9014454790577315, 1.14299799876328, 7.808105535170634, 11.340164950889987, 15.471252991340622, 5.862822591203017, 3.9498124408996653, 16.02371749417268, 12.693271184801752, 2.406201769584305, 9.553245558354574, 8.913841591378441, 3.46376992690938]

#约束集暂时按最大最小 这里按百分比的绝对值给出
constrain_set = [-0.05, 0.05]

'''
for index in range(1000):
      data_vector.append(random.uniform(1,20))  #data_vector.append(random.random())
'''

#print('-----------------------------INPUT')
#print(data_vector)

delta_vetor, Xmax = count_insert_vector(MIN_OPTIOM, DISTORTION_BOUND, np.asarray(data_vector) , constrain_set)

#print('-----------------------------OUTPUT')
#print(delta_vetor)