# Trace_Cut
对网络trace分类和处理

Cut目录是对数据的切分
Work目录是在数据文件中提取观看时间超过6分钟的带宽和时长，按照国家保存在相应的文件夹中。
Find_K目录是针对得到的数据文件查找2-9之间的的最佳K值（K-Means分类算法对trace分类）
K-Means目录是通过K-means分类算法对网络trace的分类

分类之后的的数据就可以在
https://github.com/hongzimao/pensieve
中的test_live中进行跑了。
