# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#ctr c+ctr v of jupyther notebook codes
# f = open("충청남도_아산시_CCTV_20201005_1603354225320_386246.csv", 'r')
# lines = f.readlines()
# f.close()
# 
# cnt = 1
# fileName_Num = 1
# 
# for line in lines:
#     fileName = "충청남도_아산시_CCTV_20201005_1603354225320_386246" + str(fileName_Num) + ".csv"
#     
#     fw = open(fileName, "a")
#     fw.write(line)
#     fw.close()
#     
#     #목록을 3개씩 분할함
#     if cnt == 5:
#         fileName_Num = fileName_Num + 1
#         cnt = 0
#         
#     cnt = cnt + 1

#cctv preprocessing
import pandas as pd

# cctv_data = pd.read_csv("D:\\충청남도_아산시_CCTV_20201005_1603354225320_386246.csv")
# cctv_data = cctv_data.drop(columns = ['관리기관명', '소재지도로명주소', '설치목적구분',
#                                       '카메라대수', '카메라화소수', '촬영방면정보', 
#                                       '보관일수', '설치년월', '관리기관전화번호', 
#                                       '데이터기준일자'])
# I manually removed whole useless columns with excel.


cctv_data = pd.read_csv('C:/Users/2018A00582/Desktop/manual-cctv-utf-8.csv', low_memory = False)
cctv_data.info()
cctv_data.dropna(axis = 0, how = 'any') #Remove NA values.

# security lights preprocessing
sl_data = pd.read_csv('C:/Users/2018A00582/Desktop/sl.csv', low_memory = False)
sl_data.info()
sl_data.dropna(axis = 0, how = 'any') #Remove NA values.

# Remove useless columns
sl_data = pd.read_csv('C:/Users/2018A00582/Desktop/sl.csv')
sl_data = sl_data.drop(columns = ['보안등위치명', '설치개수', '소재지도로명주소',
                                       '설치년도', '설치형태', '관리기관전화번호', 
                                       '관리기관명', '데이터기준일자'])
sl_data.info()