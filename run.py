import os
import csv

import streamlit as st
import streamlit_authenticator as auth
from streamlit_option_menu import option_menu
from streamlit_extras.grid import grid
from streamlit_extras.stateful_chat import chat, add_message
from streamlit_extras.mandatory_date_range import date_range_picker
from streamlit_echarts import st_echarts
from streamlit_lottie import st_lottie

import time
from datetime import datetime, timedelta

import requests
import numpy as np
import pandas as pd
import pickle

# --- PAGE CONFIG (BROWSER TAB) ---
st.set_page_config(page_title="Emerele", page_icon=":robot_face:", layout="centered", initial_sidebar_state="expanded")


# ---- LOAD ASSETS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


# ---- MEMORY SETTINGS ----
if 'app_cache' not in st.session_state:
    st.session_state['app_cache'] = True


# --- NAVIGATION BAR ---
with st.sidebar:
    pass
    
            
# --- MAIN PAGE ---
with st.container():
    pass