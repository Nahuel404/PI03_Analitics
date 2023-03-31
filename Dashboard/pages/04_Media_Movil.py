import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

df_Nvidia = pd.read_csv('datasets/nvidia_btw_2013-2023.csv')
df_AMD = pd.read_csv('datasets/amd_btw_2013-2023.csv')

media_movil_nvidia=df_Nvidia
media_movil_AMD=df_AMD

st.markdown("<h3 style='text-align: center;'>Media Movil</h3>", unsafe_allow_html=True)

if st.checkbox('Mostrar media movil de Nvidia'):
    if st.button('Mostrar/Ocultar dataframe'):
        st.write(media_movil_nvidia[['Media_movil', 'Date']])
    
    ventana = st.slider('Tamaño de ventana', min_value=2, max_value=50, value=10)
    media_movil_nvidia['Media_movil'] = df_Nvidia['Close'].rolling(window=ventana).mean()
    

    st.markdown("<h3 style='text-align: center;'>Media Movil</h3>", unsafe_allow_html=True)

    sns.set_palette('dark')
    sns.set_style({"axes.facecolor": "000010", "text.color": "grey"})

    fig, ax1 = plt.subplots(figsize=(6,4))

    sns.lineplot(data=media_movil_nvidia, x='Date', y='Media_movil', ax=ax1, color='green')
    
    tick_interval = 300
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
    ax1.tick_params(axis='x', rotation=90)
    st.pyplot(fig)

if st.checkbox('mostrar media movil de AMD'):
    if st.button('Mostrar/Ocultar dataframe'):
        st.write(media_movil_AMD[['Media_movil', 'Date']])

    ventana = st.slider('Tamaño de ventana', min_value=2, max_value=50, value=10)
    media_movil_AMD['Media_movil'] = df_AMD['Close'].rolling(window=ventana).mean()


    st.markdown("<h3 style='text-align: center;'>Media Movil</h3>", unsafe_allow_html=True)

    sns.set_palette('dark')
    sns.set_style({"axes.facecolor": "000010", "text.color": "grey"})

    fig, ax1 = plt.subplots(figsize=(6,4))

    sns.lineplot(data=media_movil_AMD, x='Date', y='Media_movil', ax=ax1, color='red')

    tick_interval = 300
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
    ax1.tick_params(axis='x', rotation=90)
    st.pyplot(fig)



