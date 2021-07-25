import pandas as pd
import plotly.express as px

path = '/home/z/Downloads/label/'
filepath = 'test.csv'
df = pd.read_csv(path + filepath)

light_data = df['device_field03']
label_data = df['illuminance_onoff']
datetime_data = df['device_data_reg_dtm']



fig = px.line(df, x='device_data_reg_dtm', y=['device_field03', 'illuminance_onoff'])
fig.update_xaxes(rangeslider_visible=True)
fig.show()


# df.to_csv(path + 'test.csv', index=False)

