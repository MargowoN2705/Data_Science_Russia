from fontTools.merge.base import merge

from Analysys_Russia.Code.Bartek.Main import russian_data,consumptuon_data,pd,np


temp_data_1 = russian_data.copy()
temp_data_2 = consumptuon_data.copy()



temp_data_1 = temp_data_1[['2019', '2020', '2021']]
temp_data_2 = temp_data_2[temp_data_2['Year'].isin([2019, 2020, 2021])]



