import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image



st.image("https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png", width=400, use_column_width=True)

st.markdown("<h1 style='text-align: center;'>Proyecto Individual</h1>", unsafe_allow_html=True)


st.write('''
    <h1 style='text-align:center;'><span style="color:green;font-family:Arial;">Nvidia</span> vs <span style="color:red;font-family:Arial;">AMD</span></h1>

'''
    ,unsafe_allow_html=True)

st.write("""
    <div style='display: flex; justify-content: center;'>
        <div style='float: left; '>
            <img src='https://1000marcas.net/wp-content/uploads/2020/03/Logo-NVIDIA.png' width='250' height='200' />
            <p style='clear: both;'></p>
        </div>
        <div style='float: right; text-align: right;'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/AMD_Radeon_graphics_logo_2016.svg/1200px-AMD_Radeon_graphics_logo_2016.svg.png' width='200' height='200'" />
            <p style='clear: both;'></p>
        </div>
    </div>
""", unsafe_allow_html=True)

# st.slidebar.text('Información de la librería')
