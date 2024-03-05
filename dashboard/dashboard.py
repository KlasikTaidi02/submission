import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st



df_all = pd.read_csv('dashboard/main_data.csv')


def create_averageindex_df(df):
    averageindex_df = df.groupby(['year']).mean().reset_index()

    return averageindex_df


def create_AQIresultsegment_df(df):
    AQIresultsegment_df = df.groupby(['Result']).count().reset_index()

    AQIresultsegment_df.rename(columns={'year': 'AQI Result Count'}, inplace=True)

    return AQIresultsegment_df
    

stations = df_all['station'].unique()
AQIresultsegment_df = pd.DataFrame()
averageindex_df = pd.DataFrame()
temp = ''


with st.sidebar:
    st.subheader('Select Station')

    for station in stations:

        if st.button(station):
            temp = station


if temp != '':
    df_all = df_all[(df_all['station'] == temp)]

averageindex_df = create_averageindex_df(df_all)
AQIresultsegment_df = create_AQIresultsegment_df(df_all)


st.header('Air Quality Index (AQI) Station')

st.subheader(' Average  AQI Index Station Trend')


plt.figure(figsize=(15,10))
sns.lineplot(data=averageindex_df, x='year', y='AQI Index', markersize=20, palette='tab10',linewidth=2.5)
plt.title(' Average  AQI Index Station Trend',size=20)

plt.xlabel('Time',size=20)
plt.ylabel('AQI Index',size=20)

plt.legend()

st.pyplot(plt)


st.subheader('AQI Result Segmentations')


AQIresultsegment_df.sort_values(by='AQI Result Count', ascending=False, inplace=True)

ax = sns.barplot(AQIresultsegment_df, x="AQI Result Count", y="Result", palette='tab10')
ax.bar_label(ax.containers[0], fontsize=10)
plt.title(label='Segmentasi Result Station AQI Index')
st.pyplot(plt)


