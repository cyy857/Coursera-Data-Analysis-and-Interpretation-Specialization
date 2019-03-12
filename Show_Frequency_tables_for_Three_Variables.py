#!/usr/bin/python
#Run my first program and show the frequency tables for three variables of my dataset 
#Author: Chen, Yiyi
#Date: 2019-03-12
import numpy as np
import pandas as pd


#call in my dataset: Mars crater dataset 
filePath = 'marscrater_pds.csv'
marscrater = pd.read_csv(filePath,low_memory = False) 
pd.set_option('display.float_format', lambda x:'%f'%x) #display setting
pd.set_option('display.height',1000)
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

print (len(marscrater)) #number of observations (rows)
print (len(marscrater.columns)) # number of variables (columns)

#upper-case all DataFrame column names 
marscrater.columns = map(str.upper,marscrater.columns)

#counts and percentages (i.e. frequency distributions) for each variable in my personal codebook
"""
latitude = marscrater["LATITUDE_CIRCLE_IMAGE"]
latitude_c = latitude.value_counts(sort = False)
print 'count for latitude - before selecting conditions'
print(latitude_c)
latitude_p = latitude.value_counts(sort = False, normalize = True)
print 'percentage for latitude - before selecting conditions'
print(latitude_p)

longitude = marscrater["LONGITUDE_CIRCLE_IMAGE"]
longitude_c = longitude.value_counts(sort = False)
print 'count for longitude - before selecting conditions'
print(longitude_c)
longitude_p = longitude.value_counts(sort = False, normalize = True)
print 'percentage for longitude - before selecting conditions'
print(longitude_p)
 
morphology_ejecta_1 = marscrater["MORPHOLOGY_EJECTA_1"]
morphology_ejecta_1_c = morphology_ejecta_1.value_counts(sort = False)
print 'count for morphology_ejecta_1 - before selecting conditions'
print(morphology_ejecta_1_c)
morphology_ejecta_1_p = morphology_ejecta_1.value_counts(sort = False, normalize = True)
print 'percentage for morphology_ejecta_1 - before selecting conditions'
print(morphology_ejecta_1_p) 

morphology_ejecta_2 = marscrater["MORPHOLOGY_EJECTA_2"]
morphology_ejecta_2_c = morphology_ejecta_2.value_counts(sort = False)
print 'count for morphology_ejecta_2 - before selecting conditions'
print(morphology_ejecta_2_c)
morphology_ejecta_2_p = morphology_ejecta_2.value_counts(sort = False, normalize = True)
print 'percentage for morphology_ejecta_2 - before selecting conditions'
print(morphology_ejecta_2_p)

morphology_ejecta_3 = marscrater["MORPHOLOGY_EJECTA_3"]
morphology_ejecta_3_c = morphology_ejecta_3.value_counts(sort = False)
print 'count for morphology_ejecta_3 - before selecting conditions'
print(morphology_ejecta_3_c)
morphology_ejecta_3_p = morphology_ejecta_3.value_counts(sort = False, normalize = True)
print 'percentage for morphology_ejecta_3 - before selecting conditions'
print(morphology_ejecta_3_p) 
"""
num_layer = marscrater["NUMBER_LAYERS"]
num_layer_c = num_layer.value_counts(sort = False)
#print 'count for number layers - before selecting conditions'
#print(num_layer_c)
num_layer_p = num_layer.value_counts(sort = False, normalize = True)
#print 'percentage for number layers- before selecting conditions'
#print(num_layer_p)

diam = marscrater["DIAM_CIRCLE_IMAGE"]
diam_c = diam.value_counts(sort = False)
#print 'count for diameter - before selecting conditions'
#print(diam_c)
diam_p = diam.value_counts(sort = False, normalize =  True)
#print 'percentage for diameter - before selecting conditions'
#print(diam_p)

depth = marscrater["DEPTH_RIMFLOOR_TOPOG"]
depth_c = depth.value_counts(sort = False)
#print 'count for depth - before selecting conditions'
#print(depth_c)
depth_p = depth.value_counts(sort = False, normalize = True)
#print 'percentage for depth - before selecting conditions'
#print(depth_p)

#subset data to whose attribution of "morphology ejecta *" is not a  null string
null_s = ' '
sub1=marscrater[(marscrater["MORPHOLOGY_EJECTA_1"]>null_s)|(marscrater["MORPHOLOGY_EJECTA_2"]>null_s)|(marscrater["MORPHOLOGY_EJECTA_3"]>null_s)]

#make a copy of my new subsetted data
sub2 = sub1.copy()

# frequency distritions on new sub2 data frame
"""
latitude = sub2["LATITUDE_CIRCLE_IMAGE"]
latitude_c = latitude.value_counts(sort = False)
print 'count for latitude - after selecting conditions'
print(latitude_c) 
latitude_p = latitude.value_counts(sort = False, normalize = True)
print 'percentage for latitude - after selecting conditions'
print(latitude_p)

longitude = sub2["LONGITUDE_CIRCLE_IMAGE"]
longitude_c = longitude.value_counts(sort = False)
print 'count for longitude - after selecting conditions'
print(longitude_c)
longitude_p = longitude.value_counts(sort = False, normalize = True)
print 'percentage for longitude - after selecting conditions'
print(longitude_p)

morphology_ejecta_1 = sub2["MORPHOLOGY_EJECTA_1"]
morphology_ejecta_1_c = morphology_ejecta_1.value_counts(sort = False)
print 'count for morphology_ejecta_1 - after selecting conditions'
print(morphology_ejecta_1_c)
morphology_ejecta_1_p = morphology_ejecta_1.value_counts(sort = False, normalize = True)
print 'percentage for morphology_ejecta_1 - after selecting conditions'
print(morphology_ejecta_1_p)

morphology_ejecta_2 = sub2["MORPHOLOGY_EJECTA_2"]
morphology_ejecta_2_c = morphology_ejecta_2.value_counts(sort = False)
print 'count for morphology_ejecta_2 - after selecting conditions'
print(morphology_ejecta_2_c)
morphology_ejecta_2_p = morphology_ejecta_2.value_counts(sort = False, normalize = True)
print 'percentage for morphology_ejecta_2 - after selecting conditions'
print(morphology_ejecta_2_p)

morphology_ejecta_3 = sub2["MORPHOLOGY_EJECTA_3"]
morphology_ejecta_3_c = morphology_ejecta_3.value_counts(sort = False)
print 'count for morphology_ejecta_3 - after selecting conditions'
print(morphology_ejecta_3_c)
morphology_ejecta_3_p = morphology_ejecta_3.value_counts(sort = False, normalize = True)
print 'percentage for morphology_ejecta_3 - after selecting conditions'
print(morphology_ejecta_3_p)
"""


#displays three of  my variables as frequency tables, ft for short
#num_layer1 is the number layers data after selecting conditions
num_layer1 = sub2["NUMBER_LAYERS"]
num_layer1_c = num_layer1.value_counts(sort = False)
#print 'percentage for number layers - after selecting conditions'
#print(num_layer_c)
num_layer1_p = num_layer1.value_counts(sort = False, normalize = True)
#print 'percentage for number layers - after selecting conditions'
#print(num_layer_p)
num_layer1_ft = pd.DataFrame({'Frequency':num_layer1_c,'Percentage':num_layer1_p,'Cumulative Frequency':num_layer_c,'Cumulative Percentage':num_layer_p})
#compute missing frequency
num_layer1_ft['Frequency Missing ='] = num_layer_c-num_layer1_c
#compute total number for every column
num_layer1_ft.loc['Total'] = num_layer1_ft.sum(axis=0)
print 'Frequency table for number layers'
print num_layer1_ft[num_layer1_ft.shape[0]-5:]

#diam1 is the diameter data after selecting conditions
diam1 = sub2["DIAM_CIRCLE_IMAGE"]
diam1_c = diam1.value_counts(sort = False)
#print(diam_c)
diam1_p = diam1.value_counts(sort = False, normalize =  True)
#print 'percentage for diameter - after selecting conditions'
#print(diam_p)
diam1_ft = pd.DataFrame({'Frequency':diam1_c,'Percentage':diam1_p,'Cumulative Frequency':diam_c,'Cumulative Percentage':diam_p})
diam1_ft['Frequency Missing ='] = diam_c-diam1_c
#compute total number for every column
diam1_ft.loc['Total'] = diam1_ft.sum(axis=0)
print 'Frequency table for diameter'
print diam1_ft[diam1_ft.shape[0]-5:]
 
depth1 = sub2["DEPTH_RIMFLOOR_TOPOG"]
depth1_c = depth1.value_counts(sort = False)
#print 'count for depth - after selecting conditions'
#print(depth_c)
depth1_p = depth1.value_counts(sort = False, normalize = True)
#print 'percentage for depth - after selecting conditions'
#print(depth_p)
depth1_ft = pd.DataFrame({'Frequency':depth1_c,'Percentage':depth1_p,'Cumulative Frequency':depth_c,'Cumulative Percentage':depth_p})
depth1_ft['Frequency Missing ='] = depth_c-depth1_c
#compute total number for every column
depth1_ft.loc['Total'] = depth1_ft.sum(axis=0)
print 'Frequency table for depth'
print depth1_ft[depth1_ft.shape[0]-5:]
