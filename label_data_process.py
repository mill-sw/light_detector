import pandas as pd
import matplotlib.pyplot as plt


path = '/home/z/Downloads/label/'
filepath = 'labeling_NW0511.csv'
df = pd.read_csv(path + filepath)
label_data = df['illuminance_onoff']

flag = 0
for row, i in label_data.iteritems():
    if i == 9 and flag == 0:
        df.at[row, 'illuminance_onoff'] = 0
    elif i == 9 and flag == 1:
        df.at[row, 'illuminance_onoff'] = 1
    elif i == 1 and flag == 0:
        flag = 1
    elif i == 0 and flag == 1:
        flag = 0

df.to_csv('test.csv', index=False)


# y = df[['device_field03', 'illuminance_onoff']]
# plt.plot(y)
# plt.gcf().autofmt_xdate()
# plt.xlabel('time')
# plt.ylabel('intensity')
# plt.xlim(0, )
# plt.subplots_adjust(left=0.01, bottom=0.05, right=1, top=1)
# plt.show()

