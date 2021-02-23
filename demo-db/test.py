import re

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


'''
result = re.search('`.*`', str1).group()
result1 = result.split(' ')

re_list = []


for item in result1:
    if len(item) > 2 and item[0] == '`' and item[-1] == '`':
        re_list.append(item.strip('`'))


print(re_list)
'''


str2 = "INSERT INTO `directional_setting_website_cate` VALUES ('3', '疫情网站222', '4', '0', '1586835534', '2020-11-29 14:44:04', '0', '1'),('4', '疫情观察333', '4', '0', '1589451309', '2020-11-29 14:43:43', '0', '1')"

result = re.findall('(?<=\().*?(?=\))', str2, flags=0)

result_list = []

for item in result:
      temp = []
      str_list = item.split(',')

      for index in range(len(str_list)):
            if index == 0 or index == 2:
                  str_temp = str_list[index]
                  str_temp = str_temp.replace(' ', '')
                  str_temp = str_temp.replace('\'', '')
                  temp.append(float(str_temp))
      result_list.append(temp)


print(result_list)