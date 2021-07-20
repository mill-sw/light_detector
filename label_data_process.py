import csv
import pandas as pd
import matplotlib.pyplot as plt


data_num = 7000
path = '/home/z/Downloads/label/'
filepath = 'test.csv'
df = pd.read_csv(path + filepath)
df1 = df.head(data_num)
light_data = df1['device_field03']
label_data = df1['illuminance_onoff']

flag = 0
for row, i in label_data.iteritems():
    if i == 9 and flag == 0:
        i = 0
    elif i == 9 and flag == 1:
        i = 1
    elif i == 1 and flag == 0:
        flag = 1
    elif i == 0 and flag == 1:
        flag = 0
    df1.at[row, 'illuminance_onoff'] = i

df.to_csv('test.csv')


# y = df1[['device_field03', 'illuminance_onoff']]
# plt.plot(y)
# plt.gcf().autofmt_xdate()
# plt.xlabel('time')
# plt.ylabel('intensity')
# # plt.ylim(-.01, max)
# plt.xlim(0, )
# plt.subplots_adjust(left=0.01, bottom=0.05, right=1, top=1)
# plt.show()
