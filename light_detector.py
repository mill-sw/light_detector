import csv
import pandas as pd


data_num = 1000
path = '/home/z/Downloads/label/'
filepath = 'labeling_NW0461.csv'
df = pd.read_csv(path + filepath)
df1 = df.head(data_num)
light_data = df1[['device_field03', 'device_data_reg_dtm', 'illuminance_onoff']]

light_data= light_data.assign(time = lambda x : x["device_data_reg_dtm"].str[10:])

#"{:.2f}".format(float(int(line1[10][11:13]) + int(line1[10][14:16])/60.0))
print(light_data)

