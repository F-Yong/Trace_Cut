该目录下的脚本主要是把大数据（比如几百万条，几千万条）切割，切成n份。

有必要的时候切割，方便下面处理。

个人测试：300+W条的数据在txt文件中直接处理就OK  
数据类型：rtime,countrycode,httpclientIp, anchoruid,userip,useruid,cubeuid,tmpuid,isquic,tsbw,tsinterval   
保存文件的命名方式：CountryCode + '_' + TmpUid + '_' + AnchorUid + '_' + UserUid + '_' + UserIp + '_' + 'rtime-begin' + '_' + 'rtime-end'  
时间中的':'字符换成'-'
