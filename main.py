import streamlit as st
import pandas as pd
import numpy as np


# Create a function that returns the options for the second dropdown based on the selected value of the first dropdown
@st.cache
def get_options_2(value):
    if value == 'Option 1':
        return ['Option 2.1', 'Option 2.2', 'Option 2.3']
    elif value == 'Option 2':
        return ['Option 2.4', 'Option 2.5', 'Option 2.6']
    else:
        return []

# Create a function that returns the options for the third dropdown based on the selected value of the second dropdown
@st.cache
def get_options_3(value):
    if value == 'Option 2.1':
        return ['Option 3.1', 'Option 3.2']
    elif value == 'Option 2.2':
        return ['Option 3.3', 'Option 3.4']
    else:
        return []

# Create the first dropdown
options_1 = ['Option 1', 'Option 2']
value_1 = st.selectbox('Select an option', options_1)

# Create the second dropdown
options_2 = get_options_2(value_1)
value_2 = st.selectbox('Select an option', options_2)

# Create the third dropdown
options_3 = get_options_3(value_2)
value_3 = st.selectbox('Select an option', options_3)
