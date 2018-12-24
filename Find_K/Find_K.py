import os
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

PATH = "./All_data"

def get_feature(filename):
    # 相邻两个带宽的最大值
    # MAX_Sub_trace = 0
    L = -1
    bws = []
    BTFD = []
    with open("%s/%s" % (PATH, filename)) as f:
        lines = f.readlines()
        for line in lines:
            bws.append(float(line.split(" ")[-1]))
            L += 1
            if(L > 1):
                Maxbws_temp = abs(bws[L] - bws[L-1])
                BTFD.append(Maxbws_temp)
                # MAX_Sub_trace = MAX_Sub_trace > Maxbws_temp and MAX_Sub_trace or Maxbws_temp

    MAX_Sub_BTFD = 0         
    for i in range(1,L-1):
        MaxBTFD_temp = abs(BTFD[i] - BTFD[i-1])
        MAX_Sub_BTFD = MAX_Sub_BTFD>MaxBTFD_temp and MAX_Sub_BTFD or MaxBTFD_temp
    # mean对所有元素求均值，std计算矩阵标准差
    if np.mean(bws) > 10:
        return []
    return [np.mean(bws), np.std(bws, ddof=1),np.mean(BTFD),np.std(BTFD),MAX_Sub_BTFD] 
 

if __name__ == "__main__":
    files = os.listdir(PATH)
    print("-----os.listdir   Over----")
    df_features = []
    for file in files:
        df_feature = get_feature(file)
        if len(df_feature) > 0:
            df_features.append(df_feature)
    df_features = np.array(df_features)
    print("---------Read Over----------")
    Scores = []  # 存放轮廓系数
    for k in range(2,9):
        estimator = KMeans(n_clusters=k)  # 构造聚类器
        estimator.fit(df_features)
        Scores.append(silhouette_score(df_features,estimator.labels_,metric='euclidean'))
    print("-------Deal Over-------")
    X = range(2,9)
    plt.xlabel('k')
    plt.ylabel('轮廓系数')
    plt.plot(X,Scores,'o-')
    # plt.show()
    plt.savefig("Ans_.png")
    
 
Arr = [[1,2,3],[4,5,6],[7,8,9]]
 