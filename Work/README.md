该目录是从原始数据中提取出连续观看时间超过6分钟用户的网络带宽和时长。  
如果间断的时长低于2秒，按2秒计算。  
把带宽和时长存在相应的文件中，命名方式：CountryCode + '_' + TmpUid + '_' + AnchorUid + '_' + UserUid + '_' + UserIp + '_' + 'rtime-begin' + '_' + 'rtime-end'（时间中的':'字符换成'-'）  
