import xdrlib ,sys
import xlrd
import xlwt
import time
import datetime
import os
import csv
import gc

def TXT_Read(path):
    # 打开文件
    with open(path) as f:
        print("---------------Read Over--------------")
        lines = f.readlines()
        L = len(lines)
        i = 0
        while(i < L):
            item = (' '.join(lines[i].split()).split(" "))
            # for j in range(len(item)):
                # print(type(item[j]))
                # print(item[j])
            # print("-----data type----------")
            value = item[0]+" " + item[1]
            FirstTime = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            LastTime = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S') 
            
            CountryCode = item[2]     # 国家CountryCode
            AnchorUid = item[4]       # anchoruid
            UserIp = item[5]          # useriP
            UserUid = item[6]         # useruid
            TmpUid = item[8]          # tmpuid
            # print("i = %d  AnchorUid = %s"%(i,AnchorUid))
            FileName = CountryCode + '_' + TmpUid + '_' + AnchorUid + '_' + UserUid + '_' + UserIp + '_'
            acount = 1
            
            list = []           # 文件中的数据
            T= 0.0
            # 同一用户观看的连续数据
            while(i+acount < L):
                Num = i+acount
                Index_item = (' '.join(lines[Num].split()).split(" "))
                # print("-----------Num = %d  AnchorUid = %s"%(Num,Index_item[4]))
                if (Index_item[8] == TmpUid and Index_item[4] == AnchorUid and len(Index_item) == 12):
                    Bw = Index_item[10]
                    Time = Index_item[11]
                    # 时间处理
                    
                    acount += 1
                    # 如果数据为空
                    if(Bw == '[]' or Time == '[]'):
                        continue
                    else:
                        # 处理带宽
                        Bw = Bw.replace('["','')
                        Bw = Bw.replace('"]','')
                        Bw = Bw.replace(',','')
                        Bw = Bw.split('""')
                        # 处理时长
                        Time = Time.replace('["','')
                        Time = Time.replace('"]','')
                        Time = Time.replace(',','')
                        Time = Time.split('""')
                        # 数据传给list
                        for j in range(len(Time)):
                            list.append(T/1000)
                            T += 2000 if int(Time[j]) < 2000 else int(Time[j])
                            list.append(' ')
                            list.append(Bw[j])
                            list.append('\n')
                else:
                    # print("TmpUid: %s,%s" %(TmpUid,Index_item[8]))
                    # print("AnchorUid: %s,%s" %(AnchorUid,Index_item[4]))
                    break
            item = (' '.join(lines[i+acount-1].split()).split(" "))
            value =  Index_item[0] + " " + item[1]
            LastTime = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')    
            FileName = FileName + FirstTime.strftime("%Y-%m-%d %H-%M-%S") + "_" + LastTime.strftime("%Y-%m-%d %H-%M-%S")
            # 如果观看的时间超过20分钟,并且数据大于100条,创建文件
            if(len(list) > 400 and (LastTime-FirstTime).seconds > 6*60):
                print("-------Write  File------")
                # 数据处理后的路径
                FilePath = "E:\PyFile\Work\TXT_Deal\\data\\" + CountryCode + "\\" 
                # 如果文件夹不存在，创建文件夹
                if not os.path.exists(FilePath):
                   os.makedirs(FilePath)
                print(FilePath)
                print(FileName)
               
                text_create(FilePath,FileName, list)

            i = i+acount
    #return list

# 创建txt文件
def text_create(path = "E:\PyFile\Work\TXT_Deal\\data\\",name = 'new',msg = []):
    full_path = path + name + '.txt' #创建txt文件
    file = open(full_path, 'w')
    for item in msg:
        file.write(str(item))
    file.close()
 

# 主函数
def main():
   file_name = '000000_0.txt'  # 导入xls文件名query_hive_943642.xlsx
   tables = TXT_Read(file_name)
   # for row in tables:
       # print (row)

if __name__=="__main__":
    main()
