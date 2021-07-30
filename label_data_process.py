import pandas as pd
import numpy as np
import plotly.express as px
import tensorflow as tf

# path
path = 'label/'
filepath = 'labeling_NW0511.csv'
df = pd.read_csv(path + filepath)
df = df[['device_field03', 'illuminance_onoff', 'device_data_reg_dtm']]
light_data = df['device_field03']
label_data = df['illuminance_onoff']
time_data = df['device_data_reg_dtm']
on_value = 1
off_value = 0

# 9 to 0
flag = 0
for row, label in label_data.iteritems():
    if label == 9 and flag == 0:
        df.at[row, 'illuminance_onoff'] = off_value
    elif label == 9 and flag == 1:
        df.at[row, 'illuminance_onoff'] = on_value
    elif label == 1 and flag == 0:
        flag = 1
    elif label == 0 and flag == 1:
        flag = 0

# night time filter
cnt = 0
for (row, light), (i, label), (j, time) in zip(light_data.iteritems(), label_data.iteritems(), time_data.iteritems()):
    t = time[11:13]
    if light < 5: df.at[row, 'illuminance_onoff'] = off_value
    if 9 < int(t) < 18: df.at[row, 'illuminance_onoff'] = off_value

# threadhold filter
mx = light_data.max()
light = 0
threshold = 15
prev = 0
flag = 0
for row, now in light_data.iteritems():
    if now - prev > threshold and flag == 0:
        df.at[row, 'illuminance_onoff'] = on_value
        flag = 1
    elif prev - now > threshold and flag == 1:
        df.at[row-1, 'illuminance_onoff'] = on_value
        flag = 0
    # elif flag == 1 and -1 < prev - now < 1:
    #     df.at[row, 'illuminance_onoff'] = on_value
    # elif flag == 0:
    #     df.at[row, 'illuminance_onoff'] = off_value
    prev = now

data = []
label = []
temp_data = []
temp_label = []
temp_date = ""
# df = df.head(7000)
cnt = 0
c_val = 143
for row, i in df.iterrows():
    datetime = i[2]
    date = datetime[:10]
    index = (int(datetime[11:13])*6)+int(datetime[14])
    if len(temp_data) <= c_val or cnt <= c_val:
        if index == cnt:
            temp_data.append(int(i[0]))
            temp_label.append(int(i[1]))
        else:
            temp_data.append(0)
            temp_label.append(0)
    else:
        data.append(temp_data)
        label.append(temp_label)
        cnt = 0
        temp_data = list()
        temp_label = list()
    cnt += 1

print(np.shape(data), np.shape(label))

# plot
fig = px.line(df, x='device_data_reg_dtm', y=['device_field03', 'illuminance_onoff'])
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# save
# df.to_csv(path + 'test.csv', index=False)

# pd.to_datetime()