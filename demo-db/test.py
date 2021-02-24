import re


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

