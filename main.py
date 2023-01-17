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

if value_3:
    st.subheader("Please fill in the form according to the scope selected")
    with st.form():
        if value_3 == 'Scope 1':
            st.text("Scope 1 form")
            input_1 = st.text_input("Input 1")
            input_2 = st.text_input("Input 2")
        elif value_3 == 'Scope 2':
            st.text("Scope 2 form")
            input_3 = st.text_input("Input 3")
            input_4 = st.text_input("Input 4")
        else:
            st.text("Scope 3 form")
            input_5 = st.text_input("Input 5")
            input_6 = st.text_input("Input 6")
