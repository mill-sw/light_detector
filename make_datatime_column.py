import pandas as pd

import plotly.io as pio
import plotly.express as px
import plotly.figure_factory as ff

data_num = 40000
path = '/home/z/Downloads/label/'
filepath = 'labeling_NW0511.csv'
df = pd.read_csv(path + filepath)
df1 = df.head(data_num)
light_data = df1['device_field03']
label_data = df1['illuminance_onoff']
datetime_data = df1['device_data_reg_dtm']


fig = px.line(df1, x='device_data_reg_dtm', y=['device_field03', 'illuminance_onoff'])
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# df.to_csv('test.csv', index=False)

