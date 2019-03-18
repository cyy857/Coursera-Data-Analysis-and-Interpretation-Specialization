
#!/usr/bin/python 
import numpy as np
import pandas as pd


#call in my dataset: Mars crater dataset 
filePath = 'marscrater_pds.csv'
marscrater = pd.read_csv(filePath,low_memory = False) 
pd.set_option('display.float_format', lambda x:'%f'%x) #display setting
pd.set_option('display.height',1000)
pd.set_option('display.max_rows',20)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

print (len(marscrater)) #number of observations (rows)
print (len(marscrater.columns)) # number of variables (columns)

#upper-case all DataFrame column names 
marscrater.columns = map(str.upper,marscrater.columns)
sub3 = marscrater.copy()

#data management for layer number
#if layer_number = 0. set it to be NaN
sub3['NUMBER_LAYERS'] = sub3['NUMBER_LAYERS'].replace([0],np.NaN)
num_layer_freq = sub3['NUMBER_LAYERS'].value_counts(sort = False, dropna = False)
num_layer_perc = sub3['NUMBER_LAYERS'].value_counts(sort = False, normalize = True,dropna = False)


#data management for diameter
def area_scale(row):
    if row['AREA'] < max_area *0.0005:
        return 1
    if row['AREA'] < max_area *0.001:
        return 2
    if row['AREA'] < max_area *0.015:
        return 3
    if row['AREA'] < max_area *0.020:
        return 4
    if row['AREA'] < max_area *0.025:
        return 5
    if row['AREA'] < max_area *0.03:
        return 6
    if row['AREA'] < max_area *0.04:
        return 7
    if row['AREA'] < max_area *0.06:
        return 8
    if row['AREA'] < max_area *0.08:
        return 9
    if row['AREA'] < max_area *0.1:
        return 10

#create asecondary variables area 
sub3['AREA'] = np.power(sub3['DIAM_CIRCLE_IMAGE'],2) * np.pi / 4.0
max_area = max(sub3['AREA'])
sub3['area_scale'] = sub3.apply(lambda row:area_scale (row), axis =1)
area_scale_freq= sub3['area_scale'].value_counts(sort = False)
area_scale_perc = sub3['area_scale'].value_counts(sort = False, normalize = True)

#data management for depth
def depth_scale(row):
    if row['depth'] < 0.05:
        return 1
    if row['depth'] < 0.2:
        return 2
    if row['depth'] < 0.4:
        return 3
    if row['depth'] < 0.7:
        return 4
    if row['depth'] < 1.0:
        return 5
    if row['depth'] < 1.3:
        return 6
    if row['depth'] < 1.6:
        return 7
    if row['depth'] < 1.9:
        return 8
    if row['depth'] < 2.2:
        return 9
    if row['depth'] < max_depth:
        return 10

sub3['depth'] = sub3['DEPTH_RIMFLOOR_TOPOG']
max_depth = max(sub3['depth'])
sub3['depth_scale'] = sub3.apply(lambda row:depth_scale (row), axis =1)
depth_scale_freq= sub3['depth_scale'].value_counts(sort = False)
depth_scale_perc = sub3['depth_scale'].value_counts(sort = False, normalize = True)

#subset data to whose attribution of "morphology ejecta *" is not a  null string
null_s = ' '
sub3a=sub3[(sub3["MORPHOLOGY_EJECTA_1"]>null_s)|(sub3["MORPHOLOGY_EJECTA_2"]>null_s)|(sub3["MORPHOLOGY_EJECTA_3"]>null_s)]

#sub3a['NUMBER_LAYERS'] = sub3a['NUMBER_LAYERS'].replace([0],np.NaN)
num_layer3a_freq = sub3a['NUMBER_LAYERS'].value_counts(sort = False, dropna = False)
num_layer3a_perc = sub3a['NUMBER_LAYERS'].value_counts(sort = False, normalize = True,dropna = False)
#show frequency table for new number layers
num_layer3a_ft = pd.DataFrame({'Frequency':num_layer3a_freq,'Percentage':num_layer3a_perc,'Cumulative Frequency':num_layer_freq,'Cumulative Percentage':num_layer_perc})
#compute missing frequency
num_layer3a_ft['Frequency Missing ='] = num_layer_freq-num_layer3a_freq
#compute total number for every column
num_layer3a_ft.loc['Total'] = num_layer3a_ft.sum(axis=0)
print '  '
print 'Frequency table for number layers'
print num_layer3a_ft 

#show frequency table for area_scale
#sub3['NUMBER_LAYERS'] = sub3['NUMBER_LAYERS'].replace(np.nan,[0])
area_scale3a_freq = sub3a['area_scale'].value_counts(sort = False, dropna = False)
area_scale3a_perc = sub3a['area_scale'].value_counts(sort = False, normalize = True,dropna = False)
area_scale3a_ft = pd.DataFrame({'Frequency':area_scale3a_freq,'Percentage':area_scale3a_perc,'Cumulative Frequency':area_scale_freq,'Cumulative Percentage':area_scale_perc})
#compute missing frequency
area_scale3a_ft['Frequency Missing ='] = area_scale_freq - area_scale3a_freq
#compute total number for every column
area_scale3a_ft.loc['Total'] = area_scale3a_ft.sum(axis=0)
print '  '
print 'Frequency table for area_scale'
print area_scale3a_ft 


#show frequency table for depth_scale
depth_scale3a_freq = sub3a['depth_scale'].value_counts(sort = False, dropna = False)
depth_scale3a_perc = sub3a['depth_scale'].value_counts(sort = False, normalize = True,dropna = False)
depth_scale3a_ft = pd.DataFrame({'Frequency':depth_scale3a_freq,'Percentage':depth_scale3a_perc,'Cumulative Frequency':depth_scale_freq,'Cumulative Percentage':depth_scale_perc})
#compute missing frequency
depth_scale3a_ft['Frequency Missing ='] = depth_scale_freq - depth_scale3a_freq
#compute total number for every column
depth_scale3a_ft.loc['Total'] = depth_scale3a_ft.sum(axis=0)
print '  '
print 'Frequency table for depth_scale'
print depth_scale3a_ft 











