import streamlit as st
import pandas as pd
import numpy as np


# Create a function that returns the options for the second dropdown based on the selected value of the first dropdown
@st.cache
def get_options_2():
    return ['FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25', 'FY26']

# Create a function that returns the options for the third dropdown based on the selected value of the second dropdown
@st.cache
def get_options_3():
    return ['Scope 1', 'Scope 2', 'Scope 3']

# Create the first dropdown
options_1 = ['VBC Osage', 'VBC Libertyville', 'Pace International', 'Mycorrhizal Applications', 'MGK', 'Valent USA']
value_1 = st.selectbox('Select an option', options_1)

# Create the second dropdown
options_2 = get_options_2()
value_2 = st.selectbox('Select an option', options_2)

# Create the third dropdown
options_3 = get_options_3()
value_3 = st.selectbox('Select an option', options_3)
