# Trace_Cut
对网络trace分类和处理

1. Cut目录是对数据（数据过大）的切分  
2. Work目录是在根据原始数据提取出需求的带宽和时长，按照国家保存在相应的文件夹中。  
3. Find_K目录是针对得到的数据文件查找2-9之间的的最佳K值（K-Means分类算法对trace分类）  
4. K-Means目录是通过K-means分类算法对网络trace的分类  

分类之后的的数据就可以在
https://github.com/hongzimao/pensieve
中的test_live中进行跑了。


PS:目录里面的data目录和00000_0.txt都是截取的极少量数据，请用自己的数据测试。
