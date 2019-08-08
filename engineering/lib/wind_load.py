import numpy as np 
import pandas as pd  

importance_level = int(input(" Please enter the importance level: "))
region = input("please enter region: ")
# Calculate annual probability of exceedance for wind
def r_value(importance_level, region):
    cyclonic_regions = ['C', 'D']
    # none_cyclonic_regions = 
    if region in cyclonic_regions:
        is_cyclonic = 'Y'
    else:
        is_cyclonic = 'N'

    table = [(100, 200),(500,500), (1000,1000), (2000,2000)]
    df = pd.DataFrame(table, columns =['N', 'Y'], index=[1, 2, 3, 4])
    R = df.loc[importance_level, is_cyclonic]
    
    return R
 
r=r_value(importance_level, region)
print (r)

# r=r_value()
#  def v_site(region,)
# FC1 = 1
# FC2 = 1.05
# FD1 = 1
# FD2 = 1.10
# regional_wind_speeds = [[30, 34, 26, 23, 23],
#                         [32, 39, 28, 33, 35],
#                         [34, 41, 33, 39, 43],
#                         [37, 43, 38, 45, 51],
#                         [37, 43, 39, 47, 53],
#                         [39, 45, 44, 52, 60],
#                         [41, 47, 48, 56, 66],
#                         [43, 49, 52, 61, 72],
#                         [43, 49, 53, 62, 74],
#                         [45, 51, 57, 66, 80],
#                         [46, 53, 60, 70, 85],
#                         [48, 54, 63, 73, 90],
#                         [48, 55, 64, 74, 91],
#                         [50, 56, 67, 78, 95],
#                         [51, 58, 69, 81, 99]
#  ]

# print (regional_wind_speeds)
def v_r(r, region):
    if region in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']:
        temp_region ='A'
    else:
        temp_region=region
    
    if r >= 50:
        Fc=1.05
        Fd = 1.10
    else:
        Fc=1
        Fd=1
    
    if r < 5:
        regional_wind_speeds = [[30, 34, 26, 23, 23]]
    else:
        regional_wind_speeds = [[67-41/(r**0.1),104-70/(r**(0.045)),106-92/(r**0.1),Fc*(122-104/(r**0.1)),Fd*(156-142/(r**0.1))]]
   
    
    df = pd.DataFrame(regional_wind_speeds, columns =['A', 'W', 'B', 'C','D',], index=[1])
    df = df.round(0)
    v = df.loc[1, temp_region]
    print(df.head())
    return v
