import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math

df_Nvidia = pd.read_csv('datasets/nvidia_btw_2013-2023.csv')
df_AMD = pd.read_csv('datasets/amd_btw_2013-2023.csv')
df_Nvidia['Date']=pd.to_datetime(df_Nvidia['Date'])
df_AMD['Date']=pd.to_datetime(df_AMD['Date'])

st.markdown("<h3 style='text-align: center;'>Desvio Estandar</h3>", unsafe_allow_html=True)

desv_est_Nvidia = df_Nvidia['Adj_Close_norm'].std()
desv_est_AMD = df_AMD['Adj_Close_norm'].std()


st.write(f'Nvidia: {desv_est_Nvidia} | AMD: {desv_est_AMD}')

if st.checkbox('Graficar disperción de Nvidia'):
    fig, ax1 = plt.subplots(figsize=(6,4))

    sns.stripplot(data=df_Nvidia['Adj_Close_norm'], jitter=True, ax=ax1, color='green')
    st.pyplot(fig)
if st.checkbox('Graficar disperción de AMD'):
    fig1, ax1 = plt.subplots(figsize=(6,4))

    sns.stripplot(data=df_AMD['Adj_Close_norm'], jitter=True, ax=ax1, color='red')
    st.pyplot(fig1)

st.markdown("<h5 style='text-align: center;'>Volatilidad</h5>", unsafe_allow_html=True)

año=st.slider('selecciona un año: ',2013,2022,2022)
# año=
df_aux_N=df_Nvidia[df_Nvidia['Date'].dt.year==año]
desv_est_Nvidia_D=df_aux_N['Adj_Close_norm'].std()
aux=df_aux_N.shape
aux=aux[0]
st.markdown("<h5 style='text-align: center;'>Nvidia</h5>", unsafe_allow_html=True)

if st.button('Calcular para Nvidia en éste año'):
    dias = math.sqrt(aux)
    volatilidad_Nvidia=desv_est_Nvidia_D*dias
    st.write(f'la volatilidad para el año {año} es:  {volatilidad_Nvidia}')


df_aux_A=df_AMD[df_AMD['Date'].dt.year==año]
desv_est_AMD_D=df_aux_A['Adj_Close_norm'].std()
aux_a=df_aux_A.shape
aux_a=aux_a[0]
st.markdown("<h5 style='text-align: center;'>AMD</h5>", unsafe_allow_html=True)

if st.button('Calcular para AMD en éste año'):
    dias = math.sqrt(aux)
    volatilidad_AMD=desv_est_AMD_D*dias
    st.write(f'la volatilidad para el año {año} es:  {volatilidad_AMD}')