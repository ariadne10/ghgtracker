import streamlit as st
import pandas as pd
import numpy as np

################ Define Scope 1 Emissions (Indirect) ################

## Stationary Combustion
### What type of Stationary Combustion?
def stationary():
    emission_type = st.selectbox('Type', ('Boiler','Furnace','Turbine','Heater','Incinerator','Engine','Flare'))
    metric = st.selectbox('Period of time', ('Hour','Day','Week','Month','Year'))
    time = st.selectbox('Period of time', ('kWa','kg','Week','Month','Year'))

stationary()

##### What is the time period
# Add new

## Stationary Combustion
### Type
#### Metric
##### Time period
# Add new

## Stationary Combustion
### Type
#### Metric
##### Time period
# Add new

## Stationary Combustion
### Type
#### Metric
##### Time period
# Add new

################ Define Scope 2 Emissions (Direct) ################




################ Define Scope 3 Emissions (Indirect) ################
