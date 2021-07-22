import pandas as pd
import matplotlib.pyplot as plt


data_num = 7000
path = '/home/z/Downloads/label/'
filepath = 'labeling_NW0461.csv'
df = pd.read_csv(path + filepath)
df1 = df.head(data_num)
light_data = df1['device_field03']
label_data = df1['illuminance_onoff']
# time_data = df2['device_data_reg_dtm']

# df1.set_index(['device_data_reg_dtm'], inplace=True)
# df2.plot()
# plt.plot(df2.index)


max = max(light_data)
light = 0
light1 = 0
# threshold = 30
threshold = max/2
print(threshold)
min_filter = 10
prev = 0
li = []
on_off = []
# ave_num = 5
# ave_list = [0,0,0,0,0]
# average = []
total_light = 0
total_light_cnt = 0
for i in light_data:
    #### new average ####
    if i > min_filter: total_light += i
    if i > min_filter: total_light_cnt += 1
total_ave = total_light / total_light_cnt

for now in light_data:
    # ave = sum(ave_list)/ave_num
    if now - prev > threshold:
        light = 50
    elif prev - now > threshold:
        light = 0
    prev = now
    # ave_list.append(now)
    # if len(ave_list) > ave_num: ave_list.pop(0)
    # average.append(ave)
    if now > total_ave*2: light1 = 50
    else: light1 = 0
    li.append(light1)
    on_off.append(light)

ax = plt.gca()
# light_data.plot(linestyle='-', color='red', ax=ax)
# label_data.plot(linestyle='--', color='black', ax=ax)
# plt.axhline(total_ave*2, color='purple', linestyle='--')
# plt.plot(average, color='green')
# plt.plot(li, color='green', linestyle='-.')
plt.plot(on_off, color='red', linestyle='-')

# x = df1['device_data_reg_dtm']
y = df1[['device_field03', 'illuminance_onoff']]
# plt.plot(x, y)
plt.plot(y)
plt.gcf().autofmt_xdate()
plt.xlabel('time')
plt.ylabel('intensity')
plt.ylim(-.01, max)
plt.xlim(0, )
plt.subplots_adjust(left=0.01, bottom=0.05, right=1, top=1)
plt.show()

