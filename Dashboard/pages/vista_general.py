import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df_Nvidia = pd.read_csv('datasets/nvidia_btw_2013-2023.csv')
df_AMD = pd.read_csv('datasets/amd_btw_2013-2023.csv')

st.markdown("<h1 style='text-align: center;'>Vista General</h1>", unsafe_allow_html=True)

sns.set_palette('dark')
sns.set_style({"axes.facecolor": "000010", "text.color": "grey"})
fig, ax = plt.subplots(figsize=(6,4))
sns.lineplot(
    x='Date', 
    y='Adj Close', 
    data=df_Nvidia, 
    label='Nvidia', 
    color='green', 
    ax=ax
    )

sns.lineplot(
    x='Date', 
    y='Adj Close', 
    data=df_AMD, 
    label='AMD', 
    color='red', 
    ax=ax
    )

tick_interval = 300
ax.xaxis.set_major_locator(mdates.DayLocator(interval=tick_interval))

plt.xticks(rotation=90)
plt.show()

st.pyplot(fig)
