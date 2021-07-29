import glob
import numpy as np
import pandas as pd
import plotly.express as px
# import plotly.graph_objects as go


# path
path = '/home/z/PycharmProjects/test/label/'
filepath = 'labeling_NW0514.csv'
for i in glob.glob(path + '*.csv'):
    df = pd.read_csv(i)
    df = df[['device_field03', 'illuminance_onoff', 'device_data_reg_dtm']]
    df = df.assign(new = df['illuminance_onoff'])
    time_data = df['device_data_reg_dtm']
    label_data = df['illuminance_onoff']
    light_data = df['device_field03']
    new = df['new']
    # label_original = df['illuminance_onoff']
    # print(df2.head())

    # on_value = 30
    # off_value = 0
    # # label 0,1,9
    # for row, label in label_data.iteritems():
    #     if label == 9:
    #         df.at[row, 'illuminance_onoff'] = off_value
    #     elif label == 1:
    #         df.at[row, 'illuminance_onoff'] = on_value
    #     elif label == 0:
    #         df.at[row, 'illuminance_onoff'] = off_value

    # label 0,1,9
    on = 30
    off = -1
    prev = 0
    for row, now in label_data.iteritems():
        if now == 1 and prev == 0:
            df.at[row, 'new'] = on
        elif now == 0 and prev == 1:
            df.at[row-1, 'new'] = 0
            df.at[row, 'new'] = off
        elif now == 9:
            df.at[row, 'new'] = 0
        prev = now



    # # 9 to 0
    # flag = 0
    # for row, label in label_data.iteritems():
    #     if label == 9 and flag == 0:
    #         df.at[row, 'illuminance_onoff'] = off_value
    #     elif label == 9 and flag == 1:
    #         df.at[row, 'illuminance_onoff'] = on_value
    #     elif label == 1 and flag == 0:
    #         flag = 1
    #     elif label == 0 and flag == 1:
    #         flag = 0
    #
    # # night time filter
    # cnt = 0
    # for (row, light), (i, label), (j, time) in zip(light_data.iteritems(), label_data.iteritems(), time_data.iteritems()):
    #     t = time[11:13]
    #     if light < 5: df.at[row, 'illuminance_onoff'] = off_value
    #     if 9 < int(t) < 18: df.at[row, 'illuminance_onoff'] = off_value
    #
    # # threadhold filter
    # mx = light_data.max()
    # light = 0
    # threshold = 15
    # prev = 0
    # flag = 0
    # for row, now in light_data.iteritems():
    #     if now - prev > threshold and flag == 0:
    #         df.at[row, 'illuminance_onoff'] = on_value
    #         flag = 1
    #     elif prev - now > threshold and flag == 1:
    #         df.at[row-1, 'illuminance_onoff'] = on_value
    #         flag = 0
    #     if flag == 1:
    #         df.at[row, 'illuminance_onoff'] = on_value
    #     # elif flag == 1 and -1 < prev - now < 1:
    #     #     df.at[row, 'illuminance_onoff'] = on_value
    #     # elif flag == 0:
    #     #     df.at[row, 'illuminance_onoff'] = off_value
    #     prev = now

    # plot
    fig = px.line(df, x='device_data_reg_dtm', y=['device_field03', 'new', 'illuminance_onoff'])
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=time_data, y=new, mode='markers', name='marker'))
    # fig.add_trace(go.Scatter(x=time_data, y=label_data, mode='lines+markers', name='line+marker'))
    # fig.add_trace(go.Scatter(x=time_data, y=[light_data, label_data], mode='lines', name='line'))
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()