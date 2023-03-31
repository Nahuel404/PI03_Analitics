import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_Nvidia = pd.read_csv('datasets/nvidia_btw_2013-2023.csv')
df_AMD = pd.read_csv('datasets/amd_btw_2013-2023.csv')


st.markdown("<h3 style='text-align: center;'>High and Low</h3>", unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
        .streamlit-slider {{
            color: red;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

exponente=st.slider('Exagerar Maximos',1,9,4)


aux2=df_AMD[['High','Low','Date']]
aux=df_Nvidia[['High','Low','Date']]
aux[['High','Low']]=aux[['High','Low']]**exponente
aux2[['High','Low']]=aux2[['High','Low']]**exponente

sns.set_palette('dark')
sns.set_style({"axes.facecolor": "000010", "text.color": "grey"})

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4.5))

sns.lineplot(
    x='Date', 
    y='High', 
    data=aux, 
    label='High', 
    color='#000FFF', 
    ax=ax1
    )

sns.lineplot(
    x='Date', 
    y='Low', 
    data=aux, 
    label='Low', 
    color='green', 
    ax=ax1
    )

sns.lineplot(
    x='Date', 
    y='High', 
    data=aux2, 
    label='High', 
    color='#000FFF', 
    ax=ax2
    )

sns.lineplot(
    x='Date', 
    y='Low', 
    data=aux2, 
    label='Low', 
    color='red', 
    ax=ax2
    )

tick_interval = 365
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
ax1.tick_params(axis='x', rotation=90)
ax2.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
ax2.tick_params(axis='x', rotation=90)

ax1.set_title('Nvidia')
ax2.set_title('AMD')

plt.show()

st.pyplot(fig2)


fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(10,4.5))

y1=df_Nvidia
y2=df_AMD
y1['dif']=df_Nvidia['High']-df_Nvidia['Low']
y2['dif']=df_AMD['High']-df_AMD['Low']
y1['Date']=df_Nvidia['Date']
y2['Date']=df_AMD['Date']

sns.barplot(
    x='Date', 
    y='dif', 
    data=y1, 
    label='High', 
    color='green', 
    ax=ax3
    )

sns.barplot(
    x='Date', 
    y='dif', 
    data=y2, 
    label='High', 
    color='red', 
    ax=ax4
    )

tick_interval = 365

ax3.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
ax3.tick_params(axis='x', rotation=90)
ax4.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))
ax4.tick_params(axis='x', rotation=90)

ax3.set_title('Nvidia')
ax4.set_title('AMD')


if st.checkbox('Ver diferencias'):
    st.pyplot(fig)
