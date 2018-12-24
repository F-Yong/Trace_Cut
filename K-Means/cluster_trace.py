#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

PATH = "./All_data"

# get file Message
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
    for i in range(L-1):
        MaxBTFD_temp = abs(BTFD[i] - BTFD[i-1])
        MAX_Sub_BTFD = MAX_Sub_BTFD>MaxBTFD_temp and MAX_Sub_BTFD or MaxBTFD_temp
    # mean对所有元素求均值，std计算矩阵标准差
    if np.mean(bws) > 10:
        return []
    return [np.mean(bws), np.std(bws, ddof=1),np.mean(BTFD),np.std(BTFD),MAX_Sub_BTFD]  

# File Copy
def Copy(filename,filepath):
    #Create txt file
    # 如果目录不存在，创建
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    full_path = filepath + filename
    file = open(full_path, 'w')
    # Copy
    with open("%s/%s" % (PATH, filename)) as f:
        lines = f.readlines()
        for line in lines:
            file.writelines(line)
    file.close()

def main():
    files = os.listdir(PATH)

    features = []
    for file in files:
        feature = get_feature(file)
        if len(feature) > 0:
            features.append(feature)
    features = np.array(features)
    
    CLUSTER = 2
    pred = KMeans(CLUSTER).fit_predict(features)
    
    print (pred)
    Index = 0;
    for file in files:
        if(len(get_feature(file)) > 0):
            path = ".\\Select_Trace\\" + str(pred[Index]) + "\\" 
            Copy(file,path)
            Index += 1
    print(Index)
    plt.figure(figsize=(12, 12))
    plt.scatter(features[:, 0], features[:, 1], c=pred)
    plt.title("cluster result")
    #plt.show()
    plt.savefig("cluster-%d.png" % CLUSTER)

    return

if __name__ == "__main__":
    main()

