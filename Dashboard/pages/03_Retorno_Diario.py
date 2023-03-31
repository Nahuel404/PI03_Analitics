import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

df_Nvidia = pd.read_csv('datasets/nvidia_btw_2013-2023.csv')
df_AMD = pd.read_csv('datasets/amd_btw_2013-2023.csv')

st.markdown("<h3 style='text-align: center;'>Retorno Diario</h3>", unsafe_allow_html=True)

df_Nvidia['Date']=pd.to_datetime(df_Nvidia['Date'])
df_AMD['Date']=pd.to_datetime(df_AMD['Date'])


start_date = st.date_input('Start date', datetime.datetime(2013, 1, 2))
end_date = st.date_input('End date', datetime.datetime(2023, 1, 30))
end_date=end_date.strftime('%Y-%m-%d')
start_date=start_date.strftime('%Y-%m-%d')
end_date=pd.to_datetime(end_date)
start_date=pd.to_datetime(start_date)

if start_date > end_date:
    st.error('Error: La fecha final debe ser menor que la inicial')
else:
    fil_Nvidia=df_Nvidia[df_Nvidia['Date'].between(start_date, end_date)]
    fil_AMD=df_AMD[df_AMD['Date'].between(start_date, end_date)]

    end_date=end_date.date()
    start_date=start_date.date()


    sns.set_palette('dark')
    sns.set_style({"axes.facecolor": "000010", "text.color": "grey"})
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4.5))

    sns.barplot(
        x='Date', 
        y='ret_diario', 
        data=fil_Nvidia, 
        label='Nvidia', 
        color='green', 
        ax=ax1
        )
    
    sns.barplot(
        x='Date', 
        y='ret_diario', 
        data=fil_AMD, 
        label='Nvidia', 
        color='green', 
        ax=ax2
        )
    
    tick_interval = 300
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
    ax1.tick_params(axis='x', rotation=90)
    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
    ax2.tick_params(axis='x', rotation=90)

    ax1.set_title('Nvidia')
    ax2.set_title('AMD')


    st.pyplot(fig)